from core import defs

class CanStayOnlineResult:
    def __init__(self):
	self.remaining_time=defs.MAXLONG
	self.kill_dic={}#{instance:"kill_reason"}

    def __add__(self,can_stay_online_result):
	"""
	    merge this object with another can_stay_online object.
	    this is done, by choosing minimum remaining_time and merge kill_dics
	"""
	self.setNew(can_stay_online_result.getRemainingTime(),can_stay_online_result.getKillDic())
	return self

    def setNew(self,remaining_time,kill_dic):
	"""
	    add new values to object, by calling self.newRemainingTime and self.addInstanceToKill
	"""
	self.newRemainingTime(remaining_time)
	self.__mergeKillDic(kill_dic)

    def setKillForAllInstances(self,kill_reason,instances):
	"""
	    set kill for all instances of user with reason "kill_reason"
	    returned remaining time will be set to 0, so no new event for user will set
	"""
	self.newRemainingTime(0)
	def createReasonList(_index): 
	    self.addInstanceToKill(_index+1,kill_reason)
	map(creadteReasonList,range(user_obj.instances))
	

    def getRemainingTime(self):
	return remaining_time

    def getKillDics(self):
	return kill_dic
    
    def newRemainingTime(self,new_remaining_time):
	"""
	    new_remaining_time(integer): new calculated remaining time in seconds
	    add another remaining time to object. we check the new remaining time
	    against previous remaining times, and choose the minimum
	"""
	self.remaining_time=min(self.remaining_time,new_remaining_time)
    
    def addInstanceToKill(self,instance,kill_reason):
	"""
	    instance(integer): instance of user
	    kill_reason(text): reason of killing user
	    add a new instance to kill.
	"""
	if self.kill_dics.has_key(instance):
	    self.kill_dics[instance]="%s, %s"%(self.kill_dics[instance],kill_reason)
	else:
	    self.kill_dics[instance]=kill_reason
    
    
    def __mergeKillDic(self,kill_dic):
	for instance in kill_dic:
	    self.addInstanceToKill(instance,kill_dic[instance])

	    