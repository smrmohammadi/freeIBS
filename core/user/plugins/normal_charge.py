from core.user import user_plugin,user_main,attribute
from core.user.info_holder import InfoHolder
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *
from core.charge import charge_main

info_holder_name="normal charge"
def init():
    user_main.getAttributeManager().registerHandler(MultiLoginAttrHandler(),["normal_charge"],["normal_charge"])

class NormalChargeInfoHolder(InfoHolder):
    def __init__(self):
	InfoHolder.__init__(self,info_holder_name)

    def changeInit(self,normal_charge):
	self.charge_name=normal_charge
	self.useGenerateQuery({"charge_name":self.charge_name})

    def deleteInit(self):
	self.useGenerateQuery(["charge_name"])

    def checkInput(self,src,action,dargs):
	charge_main.getLoader().checkChargeName(self.charge_name)
	dargs["admin_obj"].canDo("CHANGE NORMAL USER ATTRIBUTES")
	dargs["admin_obj"].canUserCharge(self.charge_name)



class NormalChargeAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,info_holder_name)
	self.registerInfoHandlerClass(NormalChargeInfoHolder,["normal_charge"])

