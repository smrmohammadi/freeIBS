from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_holder import AttrHolder
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *
from core.charge import charge_main

attr_handler_name="normal charge"
def init():
    user_main.getAttributeManager().registerHandler(NormalChargeAttrHandler(),["normal_charge"],["normal_charge"],["normal_charge"])

class NormalChargeAttrHolder(AttrHolder):
    def __init__(self,normal_charge_id):
	self.normal_charge_id=int(normal_charge_id)

    def getParsedDic(self):
	return {"normal_charge":charge_main.getLoader().getChargeByID(self.normal_charge_id).getChargeName()}

class NormalChargeAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)

    def changeInit(self,normal_charge):
	self.charge_name=normal_charge
	self.useGenerateQuery({"normal_charge":charge_main.getLoader().getChargeByName(self.charge_name).getChargeID()})

    def deleteInit(self):
	self.useGenerateQuery(["normal_charge"])

    def checkInput(self,src,action,dargs):
	dargs["admin_obj"].canDo("CHANGE NORMAL USER ATTRIBUTES")
	if hasattr(self,"charge_name"):
	    dargs["admin_obj"].canUseCharge(self.charge_name)


class NormalChargeAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(NormalChargeAttrUpdater,["normal_charge"])
	self.registerAttrHolderClass(NormalChargeAttrHolder,["normal_charge"])
	
