from core.charge import charge_main
from core.threadpool import thread_main
from core.user import user_main,user_type
from core.lib.time_lib import *
from core.ibs_exceptions import *
from core.errors import errorText
from core.db import ibs_query
import time
import copy

class NormalUser(user_type.UserType):
    def getLoginTime(self,instance):
	return self.user_obj.getInstanceInfo(instance)["login_time"]

#############################################
    def isPersistentLanClient(self,instance):
	return self.user_obj.getInstanceInfo(instance)["attrs"].has_key("persistent_lan") \
	       and self.user_obj.getInstanceInfo(instance)["attrs"]["persistent_lan"]

##############################################
    def getInOutBytes(self,instance):
	"""
	    return (rx_bytes,tx_bytes) tuple of send/receive of "instance" of user
	"""
	user_msg=self.user_obj.createUserMsg(instance,"GET_INOUT_BYTES")
	return user_msg.send()
#############################################
    def getClientAddr(self,instance):
	"""
	    return ip address of "instance" of user
	"""
	user_attrs=self.user_obj.getInstanceInfo(instance)["attrs"]
	if user_attrs.has_key("remote_ip"):
	    return user_attrs["remote_ip"]
	elif user_attrs.has_key("ip_pool_assigned_ip"):
	    return user_attrs["ip_pool_assigned_ip"]
    	else:
	    raise GeneralException(errorText("USER_LOGIN","USER_IP_NOT_AVAILABLE")%self.user_obj.getUserID())

##############################################
    def killInstance(self,instance):
	user_msg=self.user_obj.createUserMsg(instance,"KILL_USER")
	thread_main.runThread(user_msg.send,[])

##############################################
    def getCharge(self):
	return self.charge_obj

##############################################
    def logout(self,instance,ras_msg):
	used_credit=0
	query=ibs_query.IBSQuery()

        no_commit=False #no commit flag
        if ras_msg.hasAttr("no_commit") and ras_msg["no_commit"]:
	    no_commit=True

	if self.user_obj.getInstanceInfo(instance)["successful_auth"] and not no_commit:
	    used_credit=self.user_obj.charge.calcInstanceCreditUsage(instance,True)
	    query+=self.user_obj.commit(used_credit)
    
	self.user_obj.getInstanceInfo(instance)["used_credit"]=used_credit
	self.user_obj.getInstanceInfo(instance)["no_commit"]=no_commit
	
	return query+self.logToConnectionLog(instance,used_credit)

##############################################
    def logToConnectionLog(self,instance,used_credit):
	instance_info=self.user_obj.getInstanceInfo(instance)
	return user_main.getConnectionLogManager().logConnectionQuery(self.user_obj.getUserID(),
							       used_credit,
							       dbTimeFromEpoch(instance_info["login_time"]),
							       dbTimeFromEpoch(self.__getLogoutTime(instance_info)),
							       instance_info["successful_auth"],
							       "internet",
							       instance_info["ras_id"],
							       self.__filter(instance,instance_info["attrs"])
							      )
							       
    def __getLogoutTime(self,instance_info):
	if instance_info.has_key("logout_ras_msg"):
	    return instance_info["logout_ras_msg"].getTime()
	elif not instance_info["successful_auth"]: #Failed Authentication
	    return instance_info["login_time"]
	else:
	    return time.time()

    def __filter(self,instance,attrs):
	inout=self.getInOutBytes(instance)
	attrs["bytes_in"]=inout[0]
	attrs["bytes_out"]=inout[1]
	return attrs
##############################################
    def getOnlineReportDic(self,instance):
	"""
	    return a dic of name=>values to be appended to onlines user dic, when we are asked for 
	    online users report
	"""
	(in_bytes,out_bytes)=self.getInOutBytes(instance)
    	return {"in_bytes":str(in_bytes),
		"out_bytes":str(out_bytes),
		"normal_username":self.user_obj.getUserAttrs()["normal_username"]}
	