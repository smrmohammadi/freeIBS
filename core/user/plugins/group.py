"""
    This is not really an attribute, group_name belongs to basic_info, this file is used just for updating 
    group of user
"""
from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.group import group_main
from core.db import ibs_db

attr_handler_name="group name"
def init():
    user_main.getAttributeManager().registerHandler(GroupNameAttrHandler(),["group_name"],[],[])


class GroupNameAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)

    def checkInput(self,src,action,arg_dic):#XXX check access of admin to this group
	group_main.getLoader().checkGroupName(self.group_name)	

    def updateQuery(self,ibs_query,src,action,**args):
	group_obj=getLoader().getGroupByName(self.group_name)
	for user in args["users"]:
	    ibs_query+=ibs_db.createUpdateQuery("users",{"group_id":group_obj.getGroupID()})
	return ibs_query

    def changeInit(self,group_name):
        self.group_name=group_name
	self.registerQuery("user","change",self.updateQuery,[])


class GroupNameAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(GroupNameAttrUpdater,["group_name"])

