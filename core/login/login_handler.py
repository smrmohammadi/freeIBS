from core.server import handler
from core.admin import admin_main
from core.lib.password_lib import Password

class LoginHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"login")
	self.registerHandlerMethod("login")
    
    def login(self,request):
	request.checkArgs("login_auth_name","login_auth_type","login_auth_pass")
	if request["login_auth_type"]==request.ADMIN:
	    admin_main.getLoader().getAdminByName(request["login_auth_name"]).checkAuth(Password(request["login_auth_pass"]),\
				      request.getRemoteAddr())
	elif request["login_auth_type"]==request.NORMAL_USER:
	    pass
	elif request["login_auth_type"]==request.VOIP_USER:
	    pass
	elif request["login_auth_type"]==request.MAIL:
	    pass
	elif request["login_auth_type"]==request.ANONYMOUS:
	    pass
	else:
	    return request.returnErrorResponse(errorText("GENERAL","ACCESS_DENIED"))
	return 1
		