from core.server import handler
from core.admin import admin_main
from core.lib import password_lib
from core.lib.general import *
from core.lib.sort import SortedList

class AdminHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"admin")
	self.registerHandlerMethod("addNewAdmin")
	self.registerHandlerMethod("getAdminInfo")
	self.registerHandlerMethod("changePassword")
	self.registerHandlerMethod("getAllAdminUsernames")
	self.registerHandlerMethod("updateAdminInfo")

    def addNewAdmin(self,request):
	request.checkArgs("username","password","name","comment")
	request.needAuthType(request.ADMIN)
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("ADD NEW ADMIN")
	admin_id=admin_main.getActionManager().addNewAdmin(request["username"],password_lib.Password(request["password"]),
						  request["name"],request["comment"],creator_obj.getAdminID())
	return admin_id
	

    def getAdminInfo(self,request):
	request.checkArgs("admin_username")
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("SEE ADMIN INFO")
	admin_info=admin_main.getLoader().getAdminByName(request["admin_username"]).getAdminInfo()
	admin_info["deposit"]=str(admin_info["deposit"])
	return admin_info
	

    def getAllAdminUsernames(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("SEE ADMIN INFO")
	usernames=admin_main.getLoader().getAllUsernames()
	sorted=SortedList(usernames)
	sorted.sort(0)
	return sorted.getList()

    def changePassword(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("admin_username","new_password")
	if request.auth_name!=request["admin_username"]:
	    request.getAuthNameObj().canDo("CHANGE ADMIN PASSWORD")
	return admin_main.getActionManager().changePassword(request["admin_username"],password_lib.Password(request["new_password"].strip()))

    def updateAdminInfo(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE ADMIN INFO")
	request.checkArgs("admin_username","name","comment")
	return admin_main.getActionManager().updateInfo(request["admin_username"],request["name"],request["comment"])
	