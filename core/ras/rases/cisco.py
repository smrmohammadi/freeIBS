from core.ras.ras import GeneralUpdateRas
from core.ras import ras_main
from core import defs
from core.ibs_exceptions import *
from core.lib.snmp import Snmp
import os,time,re

def init():
    ras_main.getFactory().register(CiscoRas,"Cisco")

class CiscoRas(GeneralUpdateRas):
    type_attrs={"cisco_rsh_command":"%scisco/rsh -lroot"%defs.IBS_ADDONS,"cisco_update_accounting_interval":1,"cisco_snmp_community":"public","cisco_update_inout_with_snmp":1,"csco_snmp_version":"2c","cisco_snmp_timeout":10,"cisco_snmp_retries":3}

    async_port_match=re.compile("(Async[0-9/])")

    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes):
	GeneralUpdateRas.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,self.type_attrs)
	self.port_inout_bytes={} #port => (in_bytes,out_bytes)
	self.onlines={}#port => {"username":,"in_bytes":,"out_byte":,"last_update":,"start_in_bytes":,"start_out_bytes":}
	self.port_mapping={} #port_no:port_desc
	self.port_mapping_last_update=0

	self.handle_reload=True
	self.snmp_client=self.__createSnmpClient()

    def __createSnmpClient(self):
	return Snmp(self.getRasIP(),
		    self.getAttribute("cisco_snmp_community"),
		    self.getAttribute("cisco_snmp_timeout"),
		    self.getAttribute("cisco_snmp_retries"),
		    161,
		    self.getAttribute("cisco_snmp_version"))


    def __parseAsyncPort(self,port):
    	return self.async_port_match.match(port).groups()[0]

    ############################################
    def __rcmd(self,command):
	"""
	    run "command" on cisco ras
	"""
	return self.__doRcmd(self.getRasIP(),command)
    
    def __doRcmd(self,host,command):
	"""
	    run command "command" on "host" host
	"""
	_in,out,err=os.popen3("%s %s %s"%(self.getAttribute("cisco_rsh_command"),host,command))
	err_str=self.__readAll(err)
	if not errs:
	    self.toLog("RCMD: %s"%(self.getRasIP(),"\n".join(err_str),LOG_DEBUG))
	out_str=self.__readAll(out)
	map(lambda fd:fd.close(),(_in,out,err))
	return out_str
	    
    def __readAll(self,fd):
	ret=""
	tmp=fd.read()
	while tmp!="":
	    ret+=tmp
	    tmp=fd.read()
	return ret
    #################################################
    def killUser(self,user_msg):
	"""
	    kill user based on his port
	"""
	try:
	    self.__killUserOnPort(user_msg["port"])
	except:
	    logException(LOG_ERROR)

    def __killUserOnPort(self,port):
	if port.startswith("Async"):
	    port=self.__parseAsyncPort(port)
	    self.__rcmd("clear line %s"%port[5:])
	elif port.startswith("Serial"):
	    self.__rcmd("clear interface %s"%port)
	else:
	    self.toLog("kill: Don't know how to kill port %s"%(self.getRasIP(),port),LOG_ERROR)
	    return False
	return True
####################################    
    def updateInOutBytes(self):
	if self.getAttribute("cisco_update_inout_with_snmp"):
    	    self.updateInOutBytesBySNMP()
####################################
    def isOnline(self,user_msg):
	return self.onlines.has_key(user_msg["port"]) and \
	       self.onlines[user_msg["port"]]["last_update"]>=time.time()-self.getAttribute("cisco_update_accounting_interval")*60
####################################
    def getInOutBytes(self, user_msg):
	try:
	    port=user_msg["port"]
	    if port in self.onlines:
		if port in self.port_inout_bytes and "start_in_bytes" in self.onlines[port]:
		    return (self.port_inout_bytes[0]-self.onlines[port]["start_in_bytes"],
			    self.port_inout_bytes[1]-self.onlines[port]["start_out_bytes"])
		else:
		    return (self.onlines["in_bytes"],self.onlines["out_bytes"])
	    else:
		return (0,0)
	except:
	    logException(LOG_ERROR)
	    return (-1,-1)
###################################
    def __getPortFromRadiusPacket(self,pkt):
	if pkt.has_key("Cisco-NAS-Port"):
	    port=pkt["Cisco-NAS-Port"][0]
	else:
	    port="%s%s"%(pkt["NAS-Port-Type"][0],pkt["NAS-Port"][0])
	return port

####################################
    def handleRadAuthPacket(self,ras_msg):
	ras_msg["unique_id"]="port"
	ras_msg["port"]=self.__getPortFromRadiusPacket(ras_msg.getRequestPacket())
	ras_msg.setInAttrs({"User-Name":"username"})
	ras_msg.setInAttrsIfExists({"User-Password":"pap_password",
				    "CHAP-Password":"chap_password",
				    "MS-CHAP-Response":"ms_chap_response",
				    "MS-CHAP2-Response":"ms_chap2_response",
				    "Calling-Station-Id":"caller_id"
				    })
	ras_msg.setAction("INTERNET_AUTHENTICATE")

####################################
    def handleRadAcctPacket(self,ras_msg):
	status_type=ras_msg.getRequestAttr("Acct-Status-Type")[0]
	ras_msg["unique_id"]="port"
	if status_type=="Start":
	    ras_msg.setInAttrs({"User-Name":"username","Framed-IP-Address":"remote_ip","Acct-Session-Id":"session_id"})
	    ras_msg["port"]=self.__getPortFromRadiusPacket(ras_msg.getRequestPacket())
	    ras_msg["start_accounting"]=True
	    ras_msg["update_attrs"]=["remote_ip","start_accounting"]
	    ras_msg.setAction("INTERNET_UPDATE")
	elif status_type=="Stop":
	    ras_msg.setInAttrs({"User-Name":"username","Framed-IP-Address":"remote_ip","Acct-Session-Id":"session_id","Acct-Output-Octets":"in_bytes","Acct-Input-Octets":"out_bytes"})
	    ras_msg["port"]=self.__getPortFromRadiusPacket(ras_msg.getRequestPacket())
	    self.__updateInOnlines(ras_msg.getRequestPacket())
	    ras_msg.setAction("INTERNET_STOP")
	elif status_type=="Alive":
	    self.__updateInOnlines(ras_msg.getRequestPacket())
	else:
	    self.toLog("handleRadAcctPacket: invalid status_type %s"%status_type,LOG_ERROR)
####################################
    def __addInOnlines(self,auth_pkt,port):
	self.onlines[port]=auth_pkt["User-Name"][0]
	self.onlines[port]["last_update"]=time.time()
	self.onlines[port]["in_bytes"]=0
	self.onlines[port]["out_bytes"]=0
	try:
	    self.onlines[port]["start_in_bytes"]=self.port_in_out_bytes[port][0]
	    self.onlines[port]["start_out_bytes"]=self.port_in_out_bytes[port][1]
	except KeyError:
	    self.toLog("In/Out Byte is not available for port %s"%port)
    
    def __updateInOnlines(self,update_pkt):	
	port=self.__getPortFromRadiusPacket(update_pkt)
	if port in self.onlines and update_pkt["User-Name"][0]==self.onlines["username"]:
	    self.onlines["last_update"]=time.time()
	    self.onlines["in_bytes"]=update_pkt["Acct-Output-Octets"]
	    self.onlines["out_bytes"]=update_pkt["Acct-Input-Octets"]
	else:
	    self.toLog("Received Alive/Logout packet for user %s, while he's not in my online list"%update_pkt["User-Name"])

####################################
    def _reload(self):
	GeneralUpdateRas._reload(self)
	self.snmp_client=self.__createSnmpClient()
	self.port_mapping_last_update=0
####################################
    def updateInOutBytesBySNMP(self):
	if self.port_mapping_last_update<time.time()-60*60*5:#5 hours
	    self.__updatePortMapping()
	self.port_inout_bytes=self.__createPortInOutBytesDic(snmp_in_bytes,snmp_out_bytes)
	
    def __updatePortMapping(self):
	snmp_mapping=self.snmp_client.walk(".1.3.6.1.2.1.2.2.1.2")
	if snmp_mapping:
	    self.port_mapping=self.__createPortMappingDic(snmp_mapping)
	    self.port_mapping_last_update=time.time()
    
    def __createPortMappingDic(self,snmp_dic):
	mapping={}
	for oid in snmp_dic:
	    mapping[oid[oid.rfind(".")+1:]]=snmp_dic[oid]
	return mapping

    def __createPortInOutBytesDic(self,snmp_in_bytes,snmp_out_bytes):
	in_bytes_oid=".1.3.6.1.2.1.2.2.1.16"
	out_bytes_oid=".1.3.6.1.2.1.2.2.1.10"
	snmp_in_bytes=self.snmp_client.walk(in_bytes_oid)
	snmp_out_bytes=self.snmp_client.walk(out_bytes_oid)

	inout_bytes={}
	for oid in snmp_in_bytes:
	    port_no=oid[oid.rfind(".")+1:]
	    try:
	        inout_bytes[self.port_mapping[port_no]]=(snmp_in_bytes[oid],snmp_out_bytes["%s.%s"%(out_bytes_oid,port_no)])
	    except KeyError,key:
		self.toLog("Unable to update port inout bytes, key %s missing"%key)
	return inout_bytes
