from core.ras.ras import GeneralUpdateRas
from core.ras import ras_main
from core import defs
from core.ibs_exceptions import *
import os

def init():
    ras_main.getFactory().register(PPPDRas,"pppd")

class PPPDRas(GeneralUpdateRas):
    type_attrs={"pppd_kill_port_command":"%s/pppd/kill"%defs.IBS_ADDONS,"pppd_list_users_command":"%s/pppd/list_users"%defs.IBS_ADDONS}

    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,attributes):
	GeneralUpdateRas.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,attributes,self.type_attrs)
	self.onlines={}

    def killUser(self,user_msg):
	"""
	    kill user, this will call "kill_port_command" attribute, 
	    with user ppp interface numbers as argument
	"""
	try:
	    return os.system("%s %s"%(self.getAttribute("kill_port_command"),user_msg["port"]))
	except:
	    logException(LOG_ERROR)


    def getOnlines(self):
	"""
	    return a dic of onlines users in format {port_name:{"username":username,"in_bytes":in_bytes,"out_bytes":out_bytes}}

	    this will call "list_users_command" attribute, and read its output.
	    output of the command should be in format:

	    port_no username in_bytes out_bytes

	"""
	try:
	    fd=os.popen(self.getAttribute("pppd_list_users_command"))
	    out_lines=fd.readlines()
	    fd.close()
	    online_list={}
	    for line in out_lines:
		sp=line.strip().split()
		if len(sp)!=4:
		    toLog("PPPd getonlines: invalid line %s"%line,LOG_ERROR)
		    continue
		online_list[sp[0]]={"username":None,"in_bytes":sp[2],"out_bytes":sp[3]}
	except:
	    logException(LOG_ERROR)
	return online_list

    def updateInOutBytes(self):
	self.onlines=self.getOnlines()

    def isOnline(self,user_msg):
	return self.onlines.has_key(user_msg["port"])
	
    def getInOutBytes(self, user_msg):
	try:
	    port=user_msg["port"]
	    if port in self.onlines.keys():
	    	return (self.onlines[port]["in_bytes"],self.onlines[port]["out_bytes"])
	    else:
		return (0,0)
	except:
	    logException(LOG_ERRROR)
	    return (-1,-1)

    def handleRadAuthPacket(self,ras_msg):
	ras_msg.setInAttrs({"User-Name":"username","port":"NAS-Port","unique_id":"port"})
	ras_msg.setInAttrsIfExists({"User-Password":"pap_password","CHAP-Password":"chap_password"})
	ras_msg.setAction("INTERNET_AUTHENTICATE")

    def handleRadAcctPacket(self,ras_msg):
	status_type=ras_msg.getRequestAttr("Acct-Status-Type")[0]
	if status_type=="Start":
	    ras_msg.setInAttrs({"User-Name":"username","NAS-Port":"port","Framed-IP-Address":"remote_ip","Acct-Session-Id":"session_id"})
	    ras_msg.setAction("INTERNET_UPDATE")
	elif status_type=="Stop":
	    ras_msg.setInAttrs({"User-Name":"username","NAS-Port":"port","Framed-IP-Address":"remote_ip","Acct-Session-Id":"session_id","Acct-Output-Octets":"in_bytes","Acct-Input-Octets":"out_bytes"})
	    ras_msg.setAction("INTERNET_STOP")
	else:
	    toLog("PPPDRas: handleRadAcctPacket: invalid status_type %s"%status_type,LOG_ERROR)
