from core.server import handler
from core.group import group_main
from core.admin import admin_main
from core.user	import user_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *

class GroupHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"group")
	self.registerHandlerMethod("addNewGroup")
	self.registerHandlerMethod("listGroups")
	self.registerHandlerMethod("getGroupInfo")
	self.registerHandlerMethod("updateGroup")
	self.registerHandlerMethod("updateGroupAttrs")
	
	
    def addNewGroup(self,request):
	"""
	    add a new group
	    group_name(string): name of new group, group_name is unique	for each group
	    comment(string):
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("group_name","comment")
	requester=request.getAuthNameObj()
	requester.canDo("ADD NEW GROUP")
	return group_main.getActionManager().addGroup(request["group_name"],request["comment"],requester.getAdminID())

    def listGroups(self,request):
	"""
	    return a list of group names, that requester admin has access to
	"""
	request.needAuthType(request.ADMIN)
	requester=request.getAuthNameObj()
	group_names=group_main.getLoader().getAllGroupNames()
	return filter(requester.canUseGroup,group_names)	


    def getGroupInfo(self,request):
	"""
	    group_name(string): group name to return info for
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("group_name")
	requester=request.getAuthNameObj()
	if not requester.canUseGroup(request["group_name"]):
	    raise GeneralException(errorText("GROUPS","ACCESS_TO_GROUP_DENIED"))
	group_obj=group_main.getLoader().getGroupByName(request["group_name"])
	return {"group_id":group_obj.getGroupID(),
		"group_name":group_obj.getGroupName(),
		"comment":group_obj.getComment(),
		"owner_id":group_obj.getOwnerID(),
		"owner_name":admin_main.getLoader().getAdminByID(group_obj.getOwnerID()).getUsername(),
		"raw_attrs":group_obj.getAttrs(),
		"attrs":user_main.getAttributeManager().parseAttrs(group_obj.getAttrs())
	       }

    def updateGroup(self,request):
	"""
	    update group information
	    
	    group_id(integer): id of group that will be updated
	    group_name(string): new group name
	    comment(string): new group comment
	    owner_name(strin): name of admin owner of group
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("group_id","group_name","comment","owner_name")
	request.getAuthNameObj().canDo("CHANGE GROUP",request["group_name"])
	return group_main.getActionManager().updateGroup(to_int(request["group_id"],"group id"),request["group_name"],request["comment"],request["owner_name"])


    def updateGroupAttrs(self,request):
	"""
	    update group attributes
	    
	    group_name(string): group name that attributes will be changed
	    attrs(dic): dictionary of attr_name:attr_value. We say we want attr_name value to be attr_value
	    to_del_attrs(dic): dic of attributes that should be deleted 
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("group_name","attrs","to_del_attrs")
	request.getAuthNameObj().canDo("CHANGE GROUP",request["group_name"])
	to_del_attrs=request["to_del_attrs"]
	if type(to_del_attrs)==types.DictType:
	    to_del_attrs=to_del_attrs.values()
	return group_main.getActionManager().updateGroupAttrs(request["group_name"],
							      request["attrs"],
							      to_del_attrs,
							      request.getAuthNameObj())
	
	