from core.charge.charge import ChargeWithRules

class VoipCharge(ChargeWithRules): #XXX NOT CHANGED YET

    def checkLimits(self,user_obj):
	pass
		
    def calcInstanceRuleCreditUsage(self,user_obj,instance):
	"""
	    calculate and return amount of credit that this instance of user consumed
	    during --EFFECTIVE-- rule only
	"""
	pass	
