from core.charge import charge_main
class NormalUser:
    def __init__(self,user_obj):
	self.user_obj=user_obj

    def getInOutBytes(self,instance):
	return (0,0)

    def killInstance(self,instance):
	pass

    def getCharge(self):
	return self.charge_obj
