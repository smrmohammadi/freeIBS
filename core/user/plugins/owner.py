"""
    This is not really an attribute, owner_name belongs to basic_info, this file is used just for updating 
    owner of user
"""
from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.admin import admin_main
from core.db import ibs_db

attr_handler_name="owner name"
def init():
    user_main.getAttributeManager().registerHandler(OwnerNameAttrHandler(),["owner_name"],[],[])


class OwnerNameAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)

    def checkInput(self,src,action,arg_dic):
	admin_obj=arg_dic["admin_obj"]
	def checkChangeOwnerPerms(loaded_user):
	    if admin_obj.getUsername()!=self.admin_name:
		admin_obj.canDo("CHANGE USERS OWNER")

	map(checkChangeOwnerPerms,arg_dic["users"])
	admin_main.getLoader().checkAdminName(self.admin_name)	

    def updateQuery(self,ibs_query,src,action,**args):
	admin_obj=admin_main.getLoader().getAdminByName(self.admin_name)
	for user in args["users"]:
	    ibs_query+=ibs_db.createUpdateQuery("users",{"admin_id":admin_obj.getAdminID()})
	return ibs_query

    def changeInit(self,owner_name):
        self.admin_name=owner_name
	self.registerQuery("user","change",self.updateQuery,[])


class OwnerNameAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(OwnerNameAttrUpdater,["owner_name"])

