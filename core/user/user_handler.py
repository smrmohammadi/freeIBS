from core.server import handler
from core.user import user_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.multi_strs import MultiStr


class UserHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"user")
	self.registerHandlerMethod("addNewUsers")
	self.registerHandlerMethod("getUserInfo")
	self.registerHandlerMethod("updateUser")
	
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
############################################################
    def updateUser(self,request):
	"""
	    update user basic information
	    args: user_id(MultStr),owner_name,group_name
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("user_id","owner_name","group_name")
	user_ids=MultiStr(request["user_id"])
	loaded_users=user_main.getActionManager().getLoadedUsersByUserID(user_ids)
	admin_obj=request.getAuthNameObj()
	def updateUserCheckPerms(loaded_user):
	    admin_obj.canChangeUser(loaded_user)
	    if admin_obj.getUsername()!=request["owner_name"]:
		admin_obj.canDo("CHANGE USERS OWNER")
	    
	map(updateUserCheckPerms,loaded_users)
	return user_main.updateUsers(loaded_users,user_ids,request["owner_name"],request["group_name"])

