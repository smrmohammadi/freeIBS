from core.charge.charge import ChargeWithRules
from core.user.can_stay_online_result import CanStayOnlineResult
from core import defs
from core.lib.time_lib import *
from core.ibs_exceptions import *
from core.errors import errorText

import time
CHARGE_DEBUG=True

class InternetCharge(ChargeWithRules):
    def checkLimits(self,user_obj):
	result=CanStayOnlineResult()

	credit=user_obj.calcCurrentCredit()
	if credit<=0: #now set reasons for all instances to credit finished
 	    result.setKillForAllInstances(errorText("USER_LOGIN","CREDIT_FINISHED",False),user_obj.instances)
	    return result

	credit_usage_per_second=0
	earliest_rule_end=defs.MAXLONG
	next_more_applicable=defs.MAXLONG
	seconds_from_morning=secondsFromMorning()
	
	for _index in range(user_obj.instances):
	    cur_rule = user_obj.charge_info.effective_rules[_index]
	    
	    # find new rule
	    try:
		effective_rule = self.getEffectiveRule(user_obj,_index+1)
	    except LoginException,e:
		result.addInstanceToKill(instance,str(e))
		continue
	    
	    if cur_rule != effective_rule:

		cur_rule.end(user_obj, _index+1)
		effective_rule.start(user_obj,_index+1)
	
	
	    # if effective_rule ras or port are wildcards
	    if effective_rule.priority < 3: 
		#check if a more applicable rule (ras or ports are specified) 
	        #can be used before this rule ends
		next_more_applicable_rule=self.getNextMoreApplicableRule(user_obj,_index+1) 
		if next_more_applicable_rule!=None:
		    next_more_applicable=min(next_more_applicable_rule.interval.getStartSeconds()-seconds_from_morning,next_more_applicable)
		    
	    #change current effective rule
	    user_obj.charge_info.effective_rules[_index] = effective_rule
	
	    earliest_rule_end=min(earliest_rule_end,effective_rule.interval.getEndSeconds()-seconds_from_morning+1)#+1 to ensure we don't run at 23:59:59 or such times

	    credit_usage_per_second += effective_rule.cpm / 60.0 + \
					effective_rule.cpk * effective_rule.assumed_kps

	#endfor
	
	remained_time = credit / credit_usage_per_second

	if CHARGE_DEBUG:
	    toLog("user_id: %s remained_time: %s earliest_rule_end: %s next_more_applicable: %s seconds_from_morning: %s"%
	    (user_obj.getUserID(),remained_time,earliest_rule_end,next_more_applicable,seconds_from_morning),LOG_DEBUG)


	if remained_time<=0: 
 	    result.setKillForAllInstances(errorText("USER_LOGIN","CREDIT_FINISHED"),user_obj.instances)
	else:
	    result.newRemainingTime(min(remained_time,earliest_rule_end,next_more_applicable,seconds_from_morning))
	return result
	
    def calcInstanceRuleCreditUsage(self,user_obj,instance):
	"""
	    calculate and return amount of credit that this instance of user consumed
	    during --EFFECTIVE-- rule only
	"""
	if not user_obj.charge_info.accounting_started[instance-1]:
	    return 0
	
	now=time.time()
	effective_rule=user_obj.charge_info.effective_rules[instance-1]
	in_out=user_obj.getTypeObj().getInOutBytes(instance)
	credit_used=0
	if effective_rule.cpm>0:
	    credit_used+=effective_rule.cpm * (now - user_obj.charge_info.rule_start[instance-1])/60
	if effective_rule.cpk>0:
	    credit_used+=effective_rule.cpk * (effective_rule.calcRuleTransferUsage(user_obj,instance))/1024.0
	return credit_used
