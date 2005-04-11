from core.charge.charge import ChargeWithRules
import time

class VoipCharge(ChargeWithRules): 

    def checkLimits(self,user_obj):
	"""
	    Check Limits and return a CanStayOnlineResult
	    The remaining time returned is the time until one of instances should be killed
	    This works for no-multilogin and multilogin rases
	"""
	result=CanStayOnlineResult()

	credit=user_obj.calcCurrentCredit()
	if credit<=0: #now set reasons for all instances to credit finished
 	    result.setKillForAllInstances(errorText("USER_LOGIN","CREDIT_FINISHED"),user_obj.instances)
	    return result

	start=time.time()

	playing={}
	for instance in range(1,user_obj.instances+1):
	    if user_obj.charge_info.accounting_started[instance-1]:
		playing[instance]={"call_start_time":user_obj.getCallStartTime(instance)}
		playing[instance]["call_start_rule"]=self._getEffectiveRuleForTime(user_obj,instance,plying[instance]["call_start_time"])
		playing[instance]["call_start_prefix"]=playing[instance]["call_start_rule"].getPrefixObj(user_obj,instance)

	#playing instances, those who have accounting started
    	
	remaining_time=0
	first_iter=True #is this the first iteration? first iteration is important because it examines current state of user
	break_loop=False
	while not break_loop: #continue until one of instances should be killed
			      #this works well on single login sessions, that we want to know when user should
			      #be killed at start of session
	    credit_usage_per_second=0
	    credit_finish_time=defs.MAXLONG
	    earliest_rule_end=defs.MAXLONG
	    next_more_applicable=defs.MAXLONG
	    free_seconds_end=defs.MAXLONG #if user has free seconds remaining from first rule

	    seconds_from_morning=secondsFromMorning(start)

	    for instance in playing.keys():

	        try:
		    effective_rule = self._getEffectiveRuleForTime(user_obj,instance,start)
	        except LoginException,e:
		    if first_iter:
			result.addInstanceToKill(instance,str(e))
			del(playing[instance])
		    else:
			break_loop=True
		    continue
	
		if first_iter:
		    #change effective rule
		    cur_rule=user_obj.charge_info.effective_rules[instance-1]
		    if  cur_rule!= effective_rule:

	    	        cur_rule.end(user_obj, instance)
	    		effective_rule.start(user_obj,instane)

			user_obj.charge_info.effective_rules[instance] = effective_rule
			
		    
		# if effective_rule ras or port are wildcards
	        if effective_rule.priority < 3: 
		    #check if a more applicable rule (ras or ports are specified) 
	            #can be used before this rule ends
		    next_more_applicable_rule=self._getNextMoreApplicableRuleForTime(user_obj,instance,start) 
		    if next_more_applicable_rule!=None:
			next_more_applicable=min(next_more_applicable_rule.interval.getStartSeconds()-seconds_from_morning,next_more_applicable)
			
		earliest_rule_end=min(earliest_rule_end,effective_rule.interval.getEndSeconds()-seconds_from_morning+1)#+1 to ensure we don't run at 23:59:59 or such times

		#check free seconds
		if start - playing[instance]["call_start_time"] < playing[instance]["call_start_prefix"].getFreeSeconds():
		    free_seconds_end=min(free_seconds_end,playing[instance]["call_start_prefix"].getFreeSeconds() + playing[instance]["call_start_time"] )
		else:
		    credit_usage_per_second += effective_rule.getPrefixObj(user_obj,instance).getCPM() / 60.0
	    #end for
	    
	    if credit_usage_per_second:
		credit_finish_time = start + credit / credit_usage_per_second
		
	    next_event = min(earliest_rule_end,next_more_applicable,credit_finish_time,free_seconds_end)
	
	    #reduce the temp credit
	    if credit_usage_per_second:
		credit -= (next_event - start) * credit_usage_per_second
		if credit <= 0:
		    break_loop=True
	
	    remaining_time += next_event - start
	    # don't go for more than 1 week, who can talk for one week? ;)
	    # this may happen if cpm is 0
	    if remaining_time > 7 * 24 * 3600 : 
		break_loop=True

	    first_iter=False

	#end while
	result.newRemainingTime(remaining_time)
	return result


    ###########################################################
    def calcInstanceCreditUsage(self,user_obj,instance,round_result):
	"""
	    check lazy_charge in instance info, if it's set, calc the credit from start to end again
	"""
	if not user_obj.charge_info.accounting_started[instance-1]:
	    return 0

	instance_info=user_obj.getInstanceInfo(instance)
	if instance_info.has_key("lazy_charge") and not instance_info["lazy_charge"]:
	    return self.calcInstanceCreditUsageFromStart(user_obj,instance,round_result)
	else:
	    return Charge.calcInstanceCreditUsage(self,user_obj,instance,round_result)
		
    def calcInstanceRuleCreditUsage(self,user_obj,instance,round_result):
	"""
	    calculate and return amount of credit that this instance of user consumed
	    during --EFFECTIVE-- rule only
	    This is lazy mode of calculating user usage
	"""
	now = user_obj.getTypeObj().getCallEndTime(instance)
	effective_rule = user_obj.charge_info.effective_rules[instance-1]

	rule_duration=max(now - user_obj.charge_info.rule_start[instance-1] - user_obj.charge_info.remaining_free_seconds[instance-1],0)
	if rule_duration>0 and round_result:
	    round_to=effective_rule.getPrefixObj(user_obj,instance).getRoundTo()
	    if round_to:
		duration = now - user_obj.getTypeObj().getCallStartTime(instance)
		rule_duration += round_to - (duration % round_to)
		
	cpm=effective_rule.getPrefixObj(user_obj,instance).getCPM()

	usage=0
	if cpm>0:
	    usage=cpm * rule_duration / 60.0

	return usage

    ##########################################################    
    def calcInstanceCreditUsageFromStart(self,user_obj,instance,round_result):
	"""
	    calculate instance credit usage from call start_time to now again
	    This method is useful for rases that send us the real start accounting time, after user login
	    or on user logout. this way we can calculate the correct time
	"""
	start_time = user_obj.getTypeObj().getCallStartTime(instance)
	end_time = user_obj.getTypeObj().getCallEndTime(instance)
	effective_rule = self._getEffectiveRuleForTime(user_obj,instance,start_time)

	cur_time = start_time + effective_rule.getPrefixObj(user_obj,instance).getFreeSeconds() #current working time

	credit_usage = 0
	cpm = 0
	
	while cur_time < end_time:
    	    effective_rule = self._getEffectiveRuleForTime(user_obj,instance,cur_time)
	    next_event = min(cur_time + effective_rule.intervel.getEndTime() - getSecondsFromMorning(cur_time),
			     end_time)
	    cpm = effective_rule.effective_rule.getPrefixObj(user_obj,instance).getCPM()
	    if cpm > 0:
		credit_usage += cpm * (next_event - cur_time) / 60.0
	
	if round_result: #cpm and effective_rule have their last value here
	    round_to=effective_rule.getPrefixObj(user_obj,instance).getRoundTo()
	    if round_to:
		duration = end_time - start_time
		credit_usage += cpm * (round_to - (duration % round_to)) / 60.0

	return credit_usage
    ###########################################################
    def getPrefixObj(self,user_obj,instance):
	return user_obj.charge_info.effective_rules[instance].getPrefixObj(user_obj,instance)
	