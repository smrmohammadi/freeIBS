from core.charge import charge_main
from core.threadpool import thread_main
from core.user import user_main
from core.lib.time_lib import *
import time
import copy

class NormalUser:
    def __init__(self,user_obj):
	self.user_obj=user_obj

##############################################
    def getInOutBytes(self,instance):
	user_msg=self.user_obj.createUserMsg(instance,"GET_INOUT_BYTES")
	return user_msg.send()

##############################################
    def killInstance(self,instance):
	user_msg=self.user_obj.createUserMsg(instance,"KILL_USER")
	thread_main.runThread(user_msg.send,[])

##############################################
    def getCharge(self):
	return self.charge_obj

##############################################
    def logout(self,instance,ras_msg,used_credit):
	return self.logToConnectionLog(instance,used_credit)

##############################################
    def logToConnectionLog(self,instance,used_credit):
	instance_info=self.user_obj.getInstanceInfo(instance)
	return user_main.getConnectionLogManager().logConnectionQuery(self.user_obj.getUserID(),
							       used_credit,
							       dbTimeFromEpoch(instance_info["auth_ras_msg"].getTime()),
							       dbTimeFromEpoch(self.__getLogoutTime(instance_info)),
							       instance_info["successful_auth"],
							       "internet",
							       instance_info["auth_ras_msg"].getRasID(),
							       self.__filter(instance,instance_info["attrs"])
							      )
							       
    def __getLogoutTime(self,instance_info):
	if instance_info.has_key("logout_ras_msg"):
	    return instance_info["logout_ras_msg"].getTime()
	elif not instance_info["successful_auth"]: #Failed Authentication
	    return instance_info["auth_ras_msg"].getTime()
	else:
	    return time.time()

    def __filter(self,instance,attrs):
	inout=self.getInOutBytes(instance)
	attrs["in_bytes"]=inout[0]
	attrs["out_bytes"]=inout[1]
	return attrs
##############################################
    def getOnlineReportDic(self,instance):
	"""
	    return a dic of name=>values to be appended to onlines user dic, when we are asked for 
	    online users report
	"""
	(in_bytes,out_bytes)=self.getInOutBytes(instance)
    	return {"in_bytes":in_bytes,"out_bytes":out_bytes,"normal_username":self.user_obj.getUserAttrs()["normal_username"]}