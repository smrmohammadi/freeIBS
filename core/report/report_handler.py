from core.server import handler
from core.ibs_exceptions import *
from core.errors import errorText
from core.report import online,connection,credit
from core.lib import report_lib

class ReportHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"report")
	self.registerHandlerMethod("getOnlineUsers")
	self.registerHandlerMethod("getConnections")
	self.registerHandlerMethod("getCreditChanges")



    def getOnlineUsers(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("sort_by","desc")
	requester=request.getAuthNameObj()
	if requester.hasPerm("SEE ONLINE USERS"):
	    admin_perm_obj=requester.getPerms()["SEE ONLINE USERS"]
	elif requester.isGod():
	    admin_perm_obj=None
	else:
	    raise GeneralException(errorText("GENERAL","ACCESS_DENIED"))
	onlines=online.sortOnlineUsers(online.getFormattedOnlineUsers(request.getDateType()),
				       request["sort_by"],
				       request["desc"])
	
	if admin_perm_obj!=None and admin_perm_obj.isRestricted():
	    onlines=filter(lambda online_dic:online_dic["owner_id"]==requester.getAdminID(),onlines)
	return onlines
	
    def getConnections(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("conds","from","to","sort_by","desc")
	requester=request.getAuthNameObj()
	requester.canDo("SEE CONNECTION LOGS")
	conds=report_lib.fixConditionsDic(request["conds"])
	searcher=connection.ConnectionSearcher(conds,requester)
	return searcher.getConnectionLog(request["from"],request["to"],request["sort_by"],request["desc"],request.getDateType())

    def getCreditChanges(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("conds","from","to","sort_by","desc")
	requester=request.getAuthNameObj()
	requester.canDo("SEE CREDIT CHANGES")
	conds=report_lib.fixConditionsDic(request["conds"])
	searcher=credit.CreditSearcher(conds,requester)
	return searcher.getCreditChanges(request["from"],request["to"],request["sort_by"],request["desc"],request.getDateType())
    