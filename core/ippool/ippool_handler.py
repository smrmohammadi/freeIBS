from core.server import handler
from core.ippool import ippool_main

class IPpoolHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"ippool")
	self.registerHandlerMethod("addNewIPpool")
	self.registerHandlerMethod("updateIPpool")
	self.registerHandlerMethod("getIPpoolNames")
	self.registerHandlerMethod("getIPpoolInfo")
	self.registerHandlerMethod("deleteIPpool")
	self.registerHandlerMethod("delIPfromPool")
	self.registerHandlerMethod("addIPtoPool")

    def addNewIPpool(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE IPPOOL")
    	request.checkArgs("ippool_name","comment")
	ippool_id=ippool_main.getActionsManager().addNewPool(request["ippool_name"],request["comment"])

    def updateIPpool(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE IPPOOL")
    	request.checkArgs("ippool_id","ippool_name","comment")
	ippool_id=ippool_main.getActionsManager().updatePool(request["ippool_id"],request["ippool_name"],request["comment"])

    def getIPpoolNames(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("LIST IPPOOL")
	sorted=SortedList(ippool_main.getLoader().getAllIPpoolNames())
	sorted.sort(False)
	return sorted.getList()
    
    def getIPpoolInfo(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("LIST IPPOOL")
    	request.checkArgs("ippool_name")
	return ippool_main.getLoader().getIPpoolByName(request["ippool_name"]).getInfo()
    
    def deleteIPpool(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE IPPOOL")
    	request.checkArgs("ippool_name")
	ippool_main.getActionsManager().deletePool(request["ippool_name"])
    	
    def delIPfromPool(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE IPPOOL")
    	request.checkArgs("ippool_name","ip")
	ippool_main.getActionsManager().addIPtoPool(request["ippool_name"],request["ip"])
    
    def addIPtoPool(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE IPPOOL")
    	request.checkArgs("ippool_name","ip")
	ippool_main.getActionsManager().delIPfromPool(request["ippool_name"],request["ip"])

