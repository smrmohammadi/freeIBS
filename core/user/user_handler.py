from core.server import handler
from core.user import user_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.multi_strs import MultiStr
from core.lib.general import *


class UserHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"user")
	self.registerHandlerMethod("addNewUsers")
	self.registerHandlerMethod("getUserInfo")
	self.registerHandlerMethod("updateUserAttrs")
	self.registerHandlerMethod("normalUsernameExists")
	
    def addNewUsers(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("count","credit","owner_name","group_name","credit_comment")
	requester=request.getAuthNameObj()
	requester.canDo("ADD NEW USER")
	if request["owner_name"]!=requester.getUsername():
	    requester.canDo("CHANGE USERS OWNER")
	try:
	    _count=int(request["count"])
	except ValueError:
	    raise GeneralException(errorText("USER_ACTIONS","COUNT_NOT_INTEGER"))

	try:
	    credit=float(request["credit"])
	except ValueError:
	    raise GeneralException(errorText("USER_ACTIONS","CREDIT_NOT_FLOAT"))
	    
	return user_main.getActionManager().addNewUsers(_count,credit,request["owner_name"],requester.getUsername(),
							request["group_name"],request.getRemoteAddr(),
							request["credit_comment"])

##########################################################
    def getUserInfo(self,request):
	"""
	    return user information in a list of dics in format
	    [{"basic_info":{basic_user_info},"attrs":{user_attributes}},{"basic_info":{basic_user_info},"attrs":{user_attributes}},...]
	    if requester is admin, he can specify user_id or normal_username, user_id or normal_username can be multi strings
	    if requirter is user, no argument will be parsed and auth_name is used
	"""
	if request.hasAuthType(request.ADMIN):
	    if request.has_key("user_id"):
		loaded_users=user_main.getActionManager().getLoadedUsersByUserID(MultiStr(request["user_id"]))
	    elif request.has_key("normal_username"):
		loaded_users=user_main.getActionManager().getLoadedUsersByNormalUsername(MultiStr(request["normal_username"]))
	    else:
		raise request.raiseIncompleteRequest("user_id")

	    admin_obj=request.getAuthNameObj()
	    map(admin_obj.canAccessUser,loaded_users)
	    
	elif request.hasAuthType(request.NORMAL_USER):
	    loaded_users=[request.getAuthNameObj()]
	else:
	    raise request.raiseIncompleteRequest("auth_type")
	
	return user_main.getActionManager().getUserInfosFromLoadedUsers(loaded_users,request.getDateType())

#########################################################
    def updateUserAttrs(self,request):
	"""
	    update user attributes
	    
	    user_id(string): user ids that should be updated, can be multi strings
	    attrs(dic): dictionary of attr_name:attr_value. We say we want attr_name value to be attr_value
	    to_del_attrs(dic): dic of attributes that should be deleted 
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("user_id","attrs","to_del_attrs")
	loaded_users=user_main.getActionManager().getLoadedUsersByUserID(MultiStr(request["user_id"]))
	admin_obj=request.getAuthNameObj()
        map(admin_obj.canChangeUser,loaded_users)

	to_del_attrs=requestDicToList(request["to_del_attrs"])
	return user_main.getActionManager().updateUserAttrs(loaded_users,
							    request.getAuthNameObj(),
							    request["attrs"],
							    to_del_attrs
							    )
############################################################
    def normalUsernameExists(self,request):
	"""
	    check if normal_username multi str arg is exists, and return a list of existing users if any
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("normal_username")
	request.getAuthNameObj().canDo("CHANGE NORMAL USER ATTRIBUTES")
	return user_main.getActionManager().normalUsernameExists(MultiStr(request["normal_username"]))

############################################################
    