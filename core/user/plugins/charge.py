from core.user import user_plugin,user_main,attribute
from core.charge import charge_main
from core.errors import *
from core.ibs_exceptions import *

def init():
    user_main.getUserPluginManager().register("charge",ChargeUserPlugin)
    
class ChargeUserPlugin(user_plugin.UserPlugin):
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
	self.charge_defined=True
	try:
	    if user_obj.isNormalUser():
	    	self.charge_id=int(user_obj.getUserAttrs()["normal_charge"])
	    
	except GeneralException:
	    self.charge_defined=False
	    
	if self.charge_defined:
	    self.charge_obj=charge_main.getLoader().getChargeByID(self.charge_id)

 
    def login(self,ras_msg):
	if not self.charge_defined:
	    raise GeneralException(errorText("USER_LOGIN","NO_CHARGE_DEFINED")%self.user_obj.getType())

	self.charge_obj.initUser(self.user_obj)

    def logout(self,instance,ras_msg):
	self.charge_obj.logout(self.user_obj,instance)

    def canStayOnline(self):
	return self.charge_obj.checkLimits(self.user_obj)

    def calcCreditUsage(self):
	return self.charge_obj.calcCreditUsage(self.user_obj)

    def calcInstanceCreditUsage(self,instance):
	return self.charge_obj.calcInstanceCreditUsage(self.user_obj,instance)
