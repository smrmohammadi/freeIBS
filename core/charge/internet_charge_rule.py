from core.charge.charge_rule import ChargeRule

class InternetChargeRule(ChargeRule):
    def __init__(self,rule_id,charge_obj,cpm,cpk,day_of_weeks,start,end,bandwidth_limit,assumed_kps,ras_id,ports):
	"""
	    rule_id (integer) : unique id of this rule

	    cpm (integer):        Charge Per Minute
	    
	    cpk (integer):	  Charge Per KiloByte

	    day_of_weeks (DayOfWeekIntContainer instance): Days Of Week of this rule 

	    start (integer):      Rule start time, seconds from 00:00:00

	    end (integer):        Rule end Time, seconds from 00:00:00

	    bandwidth_limit (integer): bandwidth limit KiloBytes, now useful for lan (vpn) users only
	
	    assumed_kps (integer): assumed (maximum) transfer rate for this rule in KiloBytes per seconds
				   this is used to determine maximum user transfer rate and the soonest time
				   that user with this rule can consume a limited amount of allowed transfer 
	    
	    ras_id (integer):	ras id, this rule will apply to users that login on this ras_id , if set to self.ALL, if there wasn't
			any exact match for user, this rule will be used

	    ports (list): List of ports belongs to ras_id that this rule will apply to. if ras_id matches
			and port not matched, the total result is not match and we look for another rule or wildcard rule(self.ALL)
			if Ports is an empty array, it'll be used for all not matched users
	"""
	ChargeRule.__init__(self,rule_id,charge_obj,day_of_weeks,start,end,ras_id,ports)
	self.bandwidth_limit=bandwidth_limit
	self.assumed_kps=assumed_kps
	self.cpm=cpm
	self.cpk=cpk


    def __str__(self):
	return "Internet Charge Rule with id %s belongs to charge %s"%(self.rule_id,self.charge_obj.getChargeName())


    def getInfo(self):
	dic=ChargeRule.getInfo(self)
	dic["type"]="Internet"
	dic["bandwidth_limit"]=self.bandwidth_limit
	dic["assumed_kps"]=self.assumed_kps
	dic["cpm"]=self.cpm
	dic["cpk"]=self.cpk
	return dic
    
    def start(self,user_obj,instance):
	"""
	    called when this rule starts for user_obj
	    
	    user_obj (User.User instance): object of user that this rule change for
	    instance (integer): instance number of user 
	"""
	ChargeRule.start(self,user_obj,instance)
	user_obj.charge_info.rule_start_inout[instance-1]=user_obj.getTypeObj().getInOutBytes(instance)

	if self.bandwidth_limit>0:
	    bandwidth_limit.applyLimitOnUser(user_obj,instance,self.bandwidth_limit)


    def end(self,user_obj,instance):
	"""
	    called when this rule ends for user_obj	
	    
	    user_obj (User.User instance): object of user that this rule change for	    
	    instance (integer): instance number of user 	    
	"""
	ChargeRule.end(self,user_obj,instance)
	if self.bandwidth_limit>0:
	    bandwidth_limit.removeLimitOnUser(user_obj,instance)

    def calcRuleInOutUsage(self,user_obj,instance):
	"""
	    returns (in_bytes,out_bytes) usage for this instance of user during this rule
	    assuming this rule is the effective rule for this instance
	"""
	cur_in_out=user_obj.getTypeObj().getInOutBytes(instance)
	return (cur_in_out[0]-user_obj.charge_info.rule_start_inout[instance-1][0],cur_in_out[1]-user_obj.charge_info.rule_start_inout[instance-1][1])

    def calcRuleTransferUsage(self,user_obj,instance):
	"""
	    return amount of user transfer in bytes
	"""
	cur_rule_inout=self.calcRuleInOutUsage(user_obj,instance)
	return cur_rule_inout[0]+cur_rule_inout[1]
    
