from core.server import handler
from core.ras import ras_main,ras
from core.lib.sort import SortedList
from core.lib.general import *
from core.lib.multi_strs import MultiStr


class RasHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"ras")
	self.registerHandlerMethod("addNewRas")
	self.registerHandlerMethod("getRasInfo")
	self.registerHandlerMethod("getActiveRasIPs")
	self.registerHandlerMethod("getInActiveRases")
	self.registerHandlerMethod("getRasTypes")
	self.registerHandlerMethod("getRasAttributes")
	self.registerHandlerMethod("getRasPorts")
	self.registerHandlerMethod("updateRasInfo")
	self.registerHandlerMethod("updateAttributes")
	self.registerHandlerMethod("resetAttributes")
	self.registerHandlerMethod("getPortTypes")
	self.registerHandlerMethod("addPort")
	self.registerHandlerMethod("delPort")
	self.registerHandlerMethod("updatePort")
	self.registerHandlerMethod("deActiveRas")
	self.registerHandlerMethod("reActiveRas")
	self.registerHandlerMethod("getRasPortInfo")


    def addNewRas(self,request):
	request.needAuthType(request.ADMIN)
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("CHANGE RAS")
    	request.checkArgs("ras_ip","ras_type","radius_secret")
	ras_id=ras_main.getActionManager().addNewRas(request["ras_ip"],request["ras_type"],
						  request["radius_secret"])
	return ras_id

    def getRasInfo(self,request):
	request.needAuthType(request.ADMIN)
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("GET RAS INFORMATION")
    	request.checkArgs("ras_ip")
	ras_obj=ras_main.getLoader().getRasByIP(request["ras_ip"])
	return {"ras_ip":ras_obj.getRasIP(),
		"ras_id":ras_obj.getRasID(),
		"radius_secret":ras_obj.getRadiusSecret(),
		"ras_type":ras_obj.getType(),
		"port":ras_obj.getPorts(),
		"attrs":ras_obj.getSelfAttributes()}

    def getActiveRasIPs(self,request):
	request.needAuthType(request.ADMIN)
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("LIST RAS")
	sorted=SortedList(ras_main.getLoader().getAllRasIPs())
	sorted.sort(False)
	return sorted.getList()

    def getInActiveRases(self,request):
	request.needAuthType(request.ADMIN)
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("LIST RAS")
	return ras_main.getActionManager().getInActiveRases()

    def getRasTypes(self,request):
	"""
	    return a list of all available ras types
	"""
	request.needAuthType(request.ADMIN)
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("GET RAS INFORMATION")
	return ras_main.getFactory().getAllTypes()
	
    def getRasAttributes(self,request):	
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip")
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("GET RAS INFORMATION")
	return ras_main.getLoader().getRasByIP(request["ras_ip"]).getAllAttributes()

    def getRasPorts(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip")
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("GET RAS INFORMATION")
	sorted=SortedList(ras_main.getLoader().getRasByIP(request["ras_ip"]).getPorts().values())
	sorted.sortByPostText("[\"port_name\"]",0)
	return sorted.getList()
    
    def updateRasInfo(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_id","ras_ip","ras_type","radius_secret")
	creator_obj=request.getAuthNameObj()
	creator_obj.canDo("CHANGE RAS")
	return ras_main.getActionManager().updateRas(to_int(request["ras_id"],"Ras ID"),request["ras_ip"],
						     request["ras_type"],request["radius_secret"])

    def updateAttributes(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip","attrs")

	return ras_main.getActionManager().updateAttribute(request["ras_ip"],request["attrs"])


    def resetAttributes(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().delAttributes(request["ras_ip"])

    def addPort(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip","port_name","phone","type","comment")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().addPort(request["ras_ip"],
						   MultiStr(request["port_name"]),
						   request["type"],
						   MultiStr(request["phone"]),
						   MultiStr(request["comment"]))

    def getPortTypes(self,request):	
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras.PORT_TYPES

    def delPort(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip","port_name")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().delPort(request["ras_ip"],
						   MultiStr(request["port_name"]))

    def updatePort(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip","port_name","phone","type","comment")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().updatePort(request["ras_ip"],
						   MultiStr(request["port_name"]),
						   MultiStr(request["phone"]),
						   request["type"],
						   MultiStr(request["comment"]))

    def deActiveRas(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().deActiveRas(request["ras_ip"])

    def reActiveRas(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().reActiveRas(request["ras_ip"])

    def getRasPortInfo(self,request):
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("GET RAS INFORMATION")
    	request.checkArgs("ras_ip","port_name")
	return ras_main.getActionManager().getRasPortInfo(request["ras_ip"],MultiStr(request["port_name"]))

    def getRasIPpools(self,request):    
	request.needAuthType(request.ADMIN)
	request.getAuthNameObj().canDo("GET RAS INFORMATION")
    	request.checkArgs("ras_ip")
	return ras_main.getLoader().getRasByIP(request["ras_ip"]).getIPpools()

	
    def addPort(self,request):
	request.needAuthType(request.ADMIN)
    	request.checkArgs("ras_ip","port_name","phone","type","comment")
	request.getAuthNameObj().canDo("CHANGE RAS")
	return ras_main.getActionManager().addPort(request["ras_ip"],
						   MultiStr(request["port_name"]),
						   request["type"],
						   MultiStr(request["phone"]),
						   MultiStr(request["comment"]))
