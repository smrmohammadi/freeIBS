from core.user import user_plugin,user_main,attribute
from core.charge import charge_main
from core.errors import *
from core.ibs_exceptions import *
import time

def init():
    user_main.getUserPluginManager().register("charge",ChargeUserPlugin,6)
    
class ChargeUserPlugin(user_plugin.UserPlugin):
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
	self.charge_defined=True
	self.charge_initialized=0 #number of instances with initialized charge
	try:
	    if user_obj.isNormalUser():
	    	self.charge_id=int(user_obj.getUserAttrs()["normal_charge"])
	    elif user_obj.isVoIPUser():
		self.charge_id=int(user_obj.getUserAttrs()["voip_charge"])
	    	    
	except GeneralException:
	    self.charge_defined=False
	    
	if self.charge_defined:
	    self.charge_obj=charge_main.getLoader().getChargeByID(self.charge_id)

 
    def login(self,ras_msg):
	if not self.charge_defined:
	    raise GeneralException(errorText("USER_LOGIN","NO_CHARGE_DEFINED")%self.user_obj.getType())
	self.__initCharge()

	if ras_msg.hasAttr("called_number"):
	    self.__setCalledNumber(ras_msg)

	if ras_msg.hasAttr("start_accounting"):
	    self.__startAccounting(ras_msg)

    def __initCharge(self):
	self.charge_obj.initUser(self.user_obj)
	self.charge_initialized+=1
	
    def __startAccounting(self,ras_msg):
	instance=self.user_obj.getInstanceFromRasMsg(ras_msg)
	self.charge_obj.startAccounting(self.user_obj,instance)
	self.user_obj.getInstanceInfo(instance)["start_accounting"]=time.time()

    def __setCalledNumber(self,ras_msg):
	instance=self.user_obj.getInstanceFromRasMsg(ras_msg)
	self.user_obj.getInstanceInfo(instance)["attrs"]["called_number"]=ras_msg["called_number"]

	if ras_msg.hasAttr("single_session_h323") and ras_msg["single_session_h323"]:
	    ras_msg.getRasObj().setSingleH323CreditTime(ras_msg.getReplyPacket(), \
					self.charge_obj.checkLimits(self.user_obj,True).getRemainingTime())
#	    ras_msg.getReplyPacket()["H323-credit-time"]=str(int(self.charge_obj.checkLimits(self.user_obj,True).getRemainingTime()))
#	    print ras_msg.getReplyPacket()["H323-credit-time"]

    def update(self,ras_msg):

	if "called_number" in ras_msg["update_attrs"]:
	    self.__setCalledNumber(ras_msg)

	if ras_msg.hasAttr("start_accounting"):
	    self.__startAccounting(ras_msg)
	    return True

    def logout(self,instance,ras_msg):
	if instance<=self.charge_initialized:

	    self.charge_obj.logout(self.user_obj,instance,self.user_obj.getInstanceInfo(instance)["no_commit"])
	    self.charge_initialized-=1

    def canStayOnline(self):
	if self.charge_initialized:
	    return self.charge_obj.checkLimits(self.user_obj)

    def calcCreditUsage(self,round_result):
	if self.charge_initialized:
	    return self.charge_obj.calcCreditUsage(self.user_obj,round_result)
	return 0

    def calcInstanceCreditUsage(self,instance,round_result):
	if instance<=self.charge_initialized:
    	    return self.charge_obj.calcInstanceCreditUsage(self.user_obj,instance,round_result)
	return 0
