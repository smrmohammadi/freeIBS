from core.user import user_type,user_main
from core.lib.time_lib import *
from core.db import ibs_query
import time

class VoIPUser(user_type.UserType):
    def getLoginTime(self,instance):
	return self.getCallStartTime(instance)

    def getCalledNumber(self,instance):
	return self.user_obj.getInstanceInfo(instance)["attrs"]["called_number"]

    def getCallStartTime(self,instance):
	instance_info=self.user_obj.getInstanceInfo(instance)
	if instance_info.has_key("call_start_time"):
	    return instance_info["call_start_time"]
	else:
	    return instance_info["login_time"]
	
    def getCallEndTime(self,instance):
	instance_info=self.user_obj.getInstanceInfo(instance)
	if instance_info.has_key("call_end_time"):
	    return instance_info["call_end_time"]
	else:
	    return time.time()
    
    ###########################################
    def logout(self,instance,ras_msg):
	instance_info = self.user_obj.getInstanceInfo(instance)
    
	query=ibs_query.IBSQuery()
	#setup call_start_time and call_end_time
	self.__setTimes(ras_msg,instance_info)
    
	if instance_info.has_key("min_duration") and self.getCallEndTime(instance) - self.getCallStartTime(instance) < instance_info["min_duration"]:
	    used_credit=0
	    self.user_obj.setKillReason(instance,"Missed Call")
	else:
	    used_credit=self.user_obj.charge.calcInstanceCreditUsage(instance,True)

	if instance_info["successful_auth"]:
	    query+=self.user_obj.commit(used_credit)
    
	query+=self.logToConnectionLog(instance,used_credit)
	return query


    def __setTimes(self,ras_msg,instance_info):
	"""
	    check for connect_time and disconnect_time in ras_msg attribute, and assign
	    them to call_start_time and call_end_time in instance_info
	"""
	if ras_msg.hasAttr("connect_time"):
	    instance_info["call_start_time"] = ras_msg["connect_time"]
	    #make charge smarty, by using correct call_start_time
	    instance_info["lazy_charge"] = False 
	    
	
	if ras_msg.hasAttr("disconnect_time"):
	    instance_info["call_end_time"] = ras_msg["disconnect_time"]


    ###################################
    
    def getOnlineReportDic(self,instance):
	online_dic={"voip_username":self.user_obj.getUserAttrs()["voip_username"]}
	instance_info=self.user_obj.getInstanceInfo(instance)

	if instance_info["attrs"].has_key("called_number"):
	    online_dic["called_number"]=instance_info["attrs"]["called_number"]
	else:
	    online_dic["called_number"]="N/A"

	if instance_info["attrs"].has_key("prefix_name"):
	    online_dic["prefix_name"]=instance_info["attrs"]["prefix_name"]
	else:
	    online_dic["prefix_name"]="N/A"
	return online_dic    

    ########################################
    def logToConnectionLog(self,instance,used_credit):
	instance_info=self.user_obj.getInstanceInfo(instance)
	return user_main.getConnectionLogManager().logConnectionQuery(self.user_obj.getUserID(),
							       used_credit,
							       dbTimeFromEpoch(self.getCallStartTime(instance)),
							       dbTimeFromEpoch(self.getCallEndTime(instance)),
							       instance_info["successful_auth"],
							       "voip",
							       instance_info["ras_id"],
							       self.__filter(instance,instance_info["attrs"])
							      )
    def __filter(self,instance,attrs):
	return attrs
