from core.ras.ras import GeneralUpdateRas
from core.ras import ras_main
from core import defs
from core.ibs_exceptions import *
import os

def init():
    ras_main.getFactory().register(PPPDRas,"pppd")

class PPPDRas(GeneralUpdateRas):
    type_attrs={"pppd_kill_port_command":"%s/pppd/kill"%defs.IBS_ADDONS,"pppd_list_users_command":"%s/pppd/list_users"%defs.IBS_ADDONS,"pppd_apply_bandwidth_limit":"%s/pppd/apply_bw_limit"%defs.IBS_ADDONS,"pppd_remove_bandwidth_limit":"%s/pppd/remove_bw_limit"%defs.IBS_ADDONS}

    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes):
	GeneralUpdateRas.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,self.type_attrs)
	self.onlines={}# dic in format port=>{"username":,"in_bytes":,"out_bytes":}

####################################
    def killUser(self,user_msg):
	"""
	    kill user, this will call "kill_port_command" attribute, 
	    with user ppp interface numbers as argument
	"""
	try:
	    return os.system("%s %s"%(self.getAttribute("pppd_kill_port_command"),user_msg["port"]))
	except:
	    logException(LOG_ERROR)

####################################
    def getOnlines(self):
	"""
	    return a dic of onlines users in format {port_name:{"username":username,"in_bytes":in_bytes,"out_bytes":out_bytes}}

	    this will call "list_users_command" attribute, and read its output.
	    output of the command should be in format:

	    port_no username in_bytes out_bytes

	"""
	lines=self.__getOnlinesFromCLI()
	return self.__parseCLIOnlines(lines)
    
    def __getOnlinesFromCLI(self):
	fd=os.popen(self.getAttribute("pppd_list_users_command"))
	out_lines=fd.readlines()
	fd.close()
	return out_lines
	
    def __parseCLIOnlines(self,lines):
	try:
	    online_list={}
	    for line in lines:
		sp=line.strip().split()
		if len(sp)!=4:
		    toLog("PPPd getOnlines: Can't line %s"%line,LOG_ERROR)
		    continue
		online_list[int(sp[0])]={"username":None,"in_bytes":long(sp[2]),"out_bytes":long(sp[3])}
	except:
	    logException(LOG_ERROR)
	return online_list
####################################
    def updateOnlines(self):
	self.onlines=self.getOnlines()
	
####################################    
    def updateInOutBytes(self):
	self.updateOnlines()
####################################
    def isOnline(self,user_msg):
	return self.onlines.has_key(user_msg["port"])
####################################
    def getInOutBytes(self, user_msg):
	try:
	    port=user_msg["port"]
	    if port in self.onlines.keys():
	    	return (self.onlines[port]["in_bytes"],self.onlines[port]["out_bytes"])
	    else:
		return (0,0)
	except:
	    logException(LOG_ERROR)
	    return (-1,-1)
####################################
    def handleRadAuthPacket(self,ras_msg):
	ras_msg["unique_id"]="port"
	ras_msg.setInAttrs({"User-Name":"username","NAS-Port":"port"})
	ras_msg.setInAttrsIfExists({"User-Password":"pap_password",
				    "CHAP-Password":"chap_password",
				    "MS-CHAP-Response":"ms_chap_response",
				    "MS-CHAP2-Response":"ms_chap2_response",
				    })
	ras_msg.setAction("INTERNET_AUTHENTICATE")

####################################
    def handleRadAcctPacket(self,ras_msg):
	status_type=ras_msg.getRequestAttr("Acct-Status-Type")[0]
	ras_msg["unique_id"]="port"
	if status_type=="Start":
	    ras_msg.setInAttrs({"User-Name":"username","NAS-Port":"port","Framed-IP-Address":"remote_ip","Acct-Session-Id":"session_id"})
	    request_pkt=ras_msg.getRequestPacket()
	    ras_msg["update_attrs"]=["remote_ip"]
	    ras_msg.setAction("INTERNET_UPDATE")
	elif status_type=="Stop":
	    ras_msg.setInAttrs({"User-Name":"username","NAS-Port":"port","Framed-IP-Address":"remote_ip","Acct-Session-Id":"session_id","Acct-Output-Octets":"in_bytes","Acct-Input-Octets":"out_bytes"})
	    ras_msg.setAction("INTERNET_STOP")
	else:
	    toLog("PPPDRas: handleRadAcctPacket: invalid status_type %s"%status_type,LOG_ERROR)
####################################
    def applySimpleBwLimit(self,user_msg):
	"""
	    run apply/remove limit script. Name of script is in "pppd_apply_bandwidth_limit" attribute.
	    Parameters ras_ip port limit_rate_kbytes will be passed to script. If ras is on seperate machin,
	    Admin can change the script to apply limit on another ras or change pppd_apply_bandwidth_limit attribute
	    
	    WARNING: return Success even if script fails
	    WARNING: script should not sleep or wait, it should return immediately
	"""
	if user_msg["action"]=="apply":
	    try:
		return os.system("%s %s %s %s"%(self.getAttribute("pppd_apply_bandwidth_limit"),self.getRasIP(),user_msg["port"],user_msg["rate_kbytes"]))
	    except:
		logException(LOG_ERROR)
		return False
		
	elif user_msg["action"]=="remove":
	    try:
		return os.system("%s %s %s"%(self.getAttribute("pppd_remove_bandwidth_limit"),self.getRasIP(),user_msg["port"]))
	    except:
		logException(LOG_ERROR)
		return False
		
	return True
	