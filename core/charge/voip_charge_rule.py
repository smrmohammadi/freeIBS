from core.charge.charge_rule import ChargeRule

class VoipChargeRule(ChargeRule): #XXX
    def __init__(self,rule_id,charge_obj,time_limit,day_of_week,start,end,country_list_id,formula,ras_id,ports):
	"""
	    rule_id (integer) : unique id of this rule

	    time_limit (integer): time limit for this rule, if set to -1 it's unlimit, if zero or positive user can be online 
			maximum of time_limit

	    day_of_week (integer): Day Of Week of this rule 

	    start (integer):      Rule start time, seconds from 00:00:00

	    end (integer):        Rule end Time, seconds from 00:00:00
	    
	    country_list_id (integer): country list which we try to find cpm from
	    
	    formula (text): formula that apply to country list cpm, to calculate rule cpm
	    
	    ras_id (integer):	ras id, this rule will apply to users that login on this ras_id , if set to None, if there wasn't
			any exact match for user, this rule will be used

	    ports (list): List of ports belongs to ras_id that this rule will apply to. if ras_id matches
			and port not matched, the total result is not match and we look for another rule or wildcard rule(None)
			if Ports is an empty array, it'll be used for all not matched users
	"""
	ChargeRule.__init__(self,rule_id,charge_obj,time_limit,day_of_week,start,end,ras_id,ports)
	self.transfer_limit=transfer_limit
	self.bandwidth_limit=bandwidth_limit
	self.assumed_kps=assumed_kps
	self.cpm=cpm
	self.cpk=cpk

    def __str__(self):
	return "VoIP Charge Rule with id %s belongs to charge %s"%(self.rule_id,self.charge_obj.getName())


    def start(self,user_obj,instance):
	"""
	    called when this rule starts for user_obj
	    
	    user_obj (User.User instance): object of user that this rule change for
	    instance (integer): instance number of user 
	"""
	ChargeRule.start(self,user_obj,instance)
	user_obj.charge_info.rule_start_inout[instance-1]=user_obj.getInOutBytes(instance)

	if self.bandwidth_limit>=0:
	    bandwidth_limit.applyLimitOnUser(user_obj,instance,self.bandwidth_limit)


    def end(self,user_obj,instance):
	"""
	    called when this rule ends for user_obj	
	    
	    user_obj (User.User instance): object of user that this rule change for	    
	    instance (integer): instance number of user 	    
	"""
	ChargeRule.end(self,user_obj,instance)
	if self.bandwidth_limit>=0:
	    bandwidth_limit.removeLimitOnUser(user_obj,instance)

	inout_usage=self.calcRuleInOutUsage(user_obj,instance)
	user_obj.charge_info.rule_prev_inout_usage[self][0]+=inout_usage[0]
	user_obj.charge_info.rule_prev_inout_usage[self][1]+=inout_usage[1]


    def calcRuleInOutUsage(self,user_obj,instance):
	"""
	    returns (in_bytes,out_bytes) usage for this instance of user during this rule
	    assuming this rule is the effective rule for this instance
	"""
	cur_in_out=user_obj.getInOutBytes(instance)
	return (cur_in_out[0]-user_obj.rule_start_inout[0],cur_in_out[1]-user_obj.rule_start_inout[1])

    def calcRuleTransferUsage(self,user_obj,instance):
	"""
	    return amount of user transfer in bytes
	"""
	cur_rule_inout=self.calcRuleInOutUsage(self,user_obj,instance)
	return cur_rule_inout[0]+cur_rule_inout[1]
    
