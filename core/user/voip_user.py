from core.user import user_type
import time

class VoIPUser(user_type.UserType):
    def getCalledNumber(self,instance):
	return self.user_obj.getInstanceInfo(instance)["called_number"]

    def getCallStartTime(self,instance):
	instance_info=self.user_obj.getInstanceInfo(instance)
	if instance_info.has_key("start_accounting"):
	    return instance_info["start_accounting"]
	else:
	    return instance_info["login_time"]
	
    def getCallEndTime(self,instance):
	instance_info=self.user_obj.getInstanceInfo(instance)
	if instance_info.has_key("call_end_time"):
	    return instance_info["call_end_time"]
	else:
	    return time.time()
    
    def logout(self,instance):
	instance_info=self.user_obj.getInstanceInfo(instance)
	if instance_info.has_key("min_duration") and self.getCallEndTime() - self.getCallStartTime() < instance_info["min_duration"]:
	    user_credit=0
	    self.user_obj.setKillReason(instance,"Missed Call")
	else:
	    used_credit=self.charge.calcInstanceCreditUsage(instance,True)

	if self.getInstanceInfo(instance)["successful_auth"]:
	    query+=self.commit(used_credit)
    
	return self.logToConnectionLog(instance,used_credit)

    def getOnlineReportDic(self,instance):
	return {"voip_username":self.user_obj.getUserAttrs()["voip_username"]}
