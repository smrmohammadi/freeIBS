from core.server import handler
from core.user import user_main
from core.ibs_exceptions import *
from core.errors import errorText


class UserHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"user")
	self.registerHandlerMethod("addNewUsers")
	
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

