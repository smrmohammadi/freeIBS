from core.charge.charge import ChargeWithRules

class VoipCharge(ChargeWithRules): #XXX NOT CHANGED YET

    def checkLimits(self,user_obj):

	credit=user_obj.calcCurrentCredit()
	if credit<=0: #now set reasons for all instances to credit finished
	    dic={}
	    def createReasonList(instance): 
		dic[instance]="Credit has finished"
	    map(creadteReasonList,range(user_obj.instances))
    	    return (0,dic)
	    

	credit_usage_per_second=0
	rule_usage_count={}
	rule_usage_sum={}
	rule_inout_usage_sum={}
	rule_instances={} #user instances using each rule
	earliest_rule_end=0
	next_more_applicable=defs.MAXLONG
	seconds_from_morning=secondsFromMorning()
	kill_users={}
	
	for _index in range(user_obj.instances):
	    cur_rule = user_obj.effective_rules[_index]
	    
	    # find new rule
	    effective_rule = self.getEffectiveRule(user_obj,_index+1)
	    
	    if cur_rule != effective_rule:

		cur_rule.end(user_obj, _index+1)
		effective_rule.start(user_obj,_index+1)
	
	
	    # if effective_rule ras or port are wildcards
	    if effective_rule.priority < 3: 
		#check if a more applicable rule (ras or ports are specified) 
	        #can be used before this rule ends
		next_more_applicable_rule=self.nextMoreApplicableRule(user_obj,_index+1) 
		if next_more_applicable_rule!=None:
		    next_more_applicable=min(next_more_applicable_rule.interval.get_start()-now,next_more_applicable)
		    
	    #change current effective rule
	    user_obj.effective_rules[_index] = effective_rule
	
	    if earliest_rule_end > effective_rule.interval.get_end():
		earliest_rule_end = effective_rule.interval.get_end()

	    credit_usage_per_second += effective_rule.cpm / 60.0 + \
					effective_rule.cpk * effective_rule.assumed_kps

	    if effective_rule not in rule_usage_count:
		rule_usage_count[effective_rule] = 1
		rule_usage_sum[effective_rule] = rule.calcRuleUsage(user_obj,_index+1)
		rule_inout_usage_sum[effective_rule] = rule.calcRuleInOutUsage(user_obj,_index+1)
		rule_instances[effective_rule] = [_index+1]
	    else:
		rule_usage_count[effective_rule] += 1
		rule_usage_sum[effective_rule] += rule.calcRuleUsage(user_obj,_index+1)	
		inout_usage=rule.calcRuleInOutUsage(user_obj,_index+1)
		rule_inout_usage_sum[effective_rule][0]+=inout_usage[0]
		rule_inout_usage_sum[effective_rule][1]+=inout_usage[1]
		rule_instances[effective_rule].append(_index+1)
	#endfor
	
	#check rule usage times and inouts
	min_rule_usage_end=defs.MAXLONG
	
	for rule in rule_usage_count:
	    if rule.time_limit >=0:
		rule_available_time=rule.time_limit - rule_usage_sum[rule]
	    else:
		rule_available_time=defs.MAXLONG
	
	    if rule.transfer_limit >=0:
		rule_available_transfer=rule.transfer_limit - (rule_inout_usage_sum[rule][0] + rule_inout_usage_sum[rule][1])
	    else:
		rule_available_transfer=defs.MAXLONG
	
	    if rule_available_time<=0:
		for instance in rule_instances:
		    kill_users[instance]="Rule Time limit exceeded"

	    elif rule.available_transfer<=0:
		for instance in rule_instances:
		    kill_users[instance]="Rule Transfer limit exceeded"
	    
	    else:
		min_rule_usage_end=min(min_rule_usage_end,rule_available_time/rule_usage_count[rule],rule_available_bandwidth/(rule_usage_count[rule]*rule.assumed_kps))
	
	
	remained_time = credit / credit_usage_per_second
	min_all=min(remained_time,min_rule_usage_end,earliest_rule_end,next_more_applicable,seconds_from_morning)
	return (min_all,kill_users)
	
    def calcInstanceRuleCreditUsage(self,user_obj,instance):
	"""
	    calculate and return amount of credit that this instance of user consumed
	    during --EFFECTIVE-- rule only
	"""
	
	effective_rule=user_obj.effective_rules[instance-1]
	now=time.time()
	in_out=user_obj.getInOutbytes(instance)
	credit_used=0
	if effective_rule.cpm>0:
	    credit_used+=effective_rule.cpm * (now - user_obj.rule_start[instance-1])/60
	if effective_rule.cpk>0:
	    credit_used+=effective_rule.cpk * (in_out[0] - user_obj.rule_start_inout[0] + in_out[1] -\
					   user_obj.rule_start_inout[1])/1024.0
	return credit_used

