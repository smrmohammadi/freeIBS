from core.server import handler
from core.user import user_main
from core.ibs_exceptions import *
from core.errors import errorText


class UserHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"user")
	self.registerHandlerMethod("addNewUsers")
	self.registerHandlerMethod("getUserInfo")
	
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
	    return user information in a dic of {"basic_info":{basic_user_info},"attrs":{user_attributes}}
	    if requester is admin, he can specify user_id or normal_username
	    if requirter is user, no argument will be parsed and auth_name is used
	"""
	if request.hasAuthType(request.ADMIN):
	    if request.has_key("user_id"):
	    	loaded_user=user_main.getUserPool().getUserByUserID(to_int(request["user_id"]))
	    elif request.has_key("normal_username"):
		loaded_user=user_main.getUserPool().getUserByNormalUsername(to_int(request["user_id"]))
	    else:
		raise HandlerException(errorText("GENERAL","INCOMPLETE_REQUEST")%"user_id")

	    request.getAuthNameObj().canAccessUser(loaded_user)
	    
	elif request.hasAuthType(request.NORMAL_USER):
	    loaded_user=request.getAuthNameObj()
	
	return self.__getUserInfoFromLoadedUser(loaded_user)
	
    def __getUserInfoFromLoadedUser(self,loaded_user):
	return {"basic_info":loaded_user.getBasicUser.getInfo(),
		"attrs":loaded_user.getUserAttrs().getAllAttributes()
	       }	
############################################################


