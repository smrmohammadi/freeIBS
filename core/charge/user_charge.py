class UserCharge:
    """
	Instances of this class will keep charge related information
	inf user object, normally with name "charge_info"
	no charging logic here! just variable manipulations
    """
    def __init__(self):
	self.credit_prev_usage=0 #previous usage of logged off users
	self.credit_prev_usage_instance=[] #previous usage of currently online instances
	self.effective_rules=[]
	self.rule_start=[]
	self.rule_start_inout=[]

    def login(self,effective_rule,instance):
    	self.effective_rules.append(effective_rule)
	self.rule_start.append(time.time())
	self.rule_start_inout.append([0,0])
	self.credit_prev_usage_instance.append(0)

    def logout(self,instance):
	_index=instance-1
	del(self.effective_rules[_index])
	del(self.rule_start[_index])
	del(self.rule_start_inout[_index])
	del(self.credit_prev_usage_instance[_index])
