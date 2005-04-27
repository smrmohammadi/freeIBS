from core.server import handler
from core.user import user_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.multi_strs import MultiStr
from core.lib.general import *
from core.lib import report_lib
import string
import itertools

class UserHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"user")
	self.registerHandlerMethod("addNewUsers")
	self.registerHandlerMethod("getUserInfo")
	self.registerHandlerMethod("updateUserAttrs")
	self.registerHandlerMethod("changeCredit")
	self.registerHandlerMethod("searchUser")
	self.registerHandlerMethod("delUser")
	self.registerHandlerMethod("killUser")

		
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
	    elif request.has_key("voip_username"):
		loaded_users=user_main.getActionManager().getLoadedUsersByVoIPUsername(MultiStr(request["voip_username"]))
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
    def changeCredit(self,request):
	"""
	    change credit of user
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("user_id","credit","credit_comment")
	requester=request.getAuthNameObj()
	user_id_multi=MultiStr(request["user_id"])
	loaded_users=user_main.getActionManager().getLoadedUsersByUserID(user_id_multi)
	map(self.__canChangeCredit,loaded_users,itertools.repeat(requester,len(loaded_users)))
	return user_main.getActionManager().changeCredit(user_id_multi,
							 to_float(request["credit"],"credit"),
							 requester.getUsername(),
							 request.getRemoteAddr(),
							 request["credit_comment"],
							 loaded_users)

    def __canChangeCredit(self,loaded_user,requester):
	requester.canDo("CHANGE USER CREDIT",loaded_user.getUserID(),loaded_user.getBasicUser().getOwnerObj().getAdminID())
############################################################
    def searchUser(self,request):
	"""
	    return (count_of_result,user_id_lists)
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("conds","from","to","order_by","desc")
	admin_obj=request.getAuthNameObj()
	conds=self.__searchUserFixConds(request["conds"])

	if admin_obj.isGod(): pass
	elif admin_obj.hasPerm("GET USER INFORMATION"):
	    if admin_obj.getPerms()["GET USER INFORMATION"].isRestricted():
		conds["owner_name"]=[admin_obj.getAdminID()]
	else:
	    raise PermissionException(errorText("GENERAL","ACCESS_DENIED"))
		
	return user_main.getActionManager().searchUsers(conds,request["from"],request["to"],request["order_by"],request["desc"],admin_obj)

    def __searchUserFixConds(self,conds):
	"""
	    convert integer key dictionaries to lists. It takes care of other dics so it won't convert 
	    other dics
	"""
	return report_lib.fixConditionsDic(conds)
##########################################################
    def delUser(self,request):
	"""
	    delete users
	"""
	request.needAuthType(request.ADMIN)
	request.checkArgs("user_id","delete_comment","del_connection_logs")
	requester=request.getAuthNameObj()
	user_id_multi=MultiStr(request["user_id"])
	loaded_users=user_main.getActionManager().getLoadedUsersByUserID(user_id_multi)
	map(self.__canDeleteUser,loaded_users,itertools.repeat(requester,len(loaded_users)))
	return user_main.getActionManager().delUser(user_id_multi,
						    request["delete_comment"],
						    request["del_connection_logs"],
						    requester.getUsername(),
						    request.getRemoteAddr()
						    )

    def __canDeleteUser(self,loaded_user,requester):
	requester.canDo("DELETE USER",loaded_user.getUserID(),loaded_user.getBasicUser().getOwnerObj().getAdminID())
##############################################################
    def killUser(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("user_id","ras_ip","unique_id_val","kill")
	requester=request.getAuthNameObj()
	user_id=to_int(request["user_id"],"user_id")
	loaded_user=user_main.getUserPool().getUserByID(user_id)
	if request["kill"]:
	    self.__canKillUser(loaded_user,requester)
	else:
	    self.__canClearUser(loaded_user,requester)
	return user_main.getActionManager().killUser(user_id,
						     request["ras_ip"],
						     request["unique_id_val"],
						     request["kill"],requester.getUsername())

    def __canKillUser(self,loaded_user,requester):
	requester.canDo("KILL USER",loaded_user.getUserID(),loaded_user.getBasicUser().getOwnerObj().getAdminID())

    def __canClearUser(self,loaded_user,requester):
	requester.canDo("CLEAR USER",loaded_user.getUserID(),loaded_user.getBasicUser().getOwnerObj().getAdminID())
	