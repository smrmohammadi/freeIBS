from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_holder import AttrHolder
from core.user.attr_searcher import AttrSearcher
from core.ippool import ippool_main
from core.errors import *
from core.ibs_exceptions import *

attr_handler_name="ippool"
def init():
    user_main.getUserPluginManager().register("ippool",IPpoolUserPlugin,9)
    user_main.getAttributeManager().registerHandler(IPpoolAttrHandler(),["ippool"],["ippool"],["ippool"])

class IPpoolUserPlugin(user_plugin.UserPlugin):
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
 
    def login(self,ras_msg):
	if self.user_obj.getUserAttrs().hasAttr("ippool"):
	    ippool_id=int(self.user_obj.getUserAttrs()["ippool"])
	    ip=ippool_main.getLoader().getIPpoolByID(ippool_id).setIPInPacket(ras_msg.getReplyPacket())
	    if ip!=None:
	        self.__updateInstanceInfo(self.user_obj.instances,ippool_id,ip)

	if ras_msg.hasAttr("remote_ip"):
	    self.__setRemoteIP(ras_msg)

    def logout(self,instance,ras_msg):
	if self.user_obj.getInstanceInfo(instance)["attrs"].has_key("ippool_id"):
	    ippool_main.getLoader().getIPpoolByID(self.user_obj.getInstanceInfo(instance)["attrs"]["ippool_id"]).freeIP(self.user_obj.getInstanceInfo(instance)["attrs"]["ippool_assigned_ip"])
	
    def update(self,ras_msg):
	if "ippool_id" in ras_msg["update_attrs"]:
	    instance=self.user_obj.getInstanceFromUniqueID(ras_msg.getRasID(),ras_msg.getUniqueIDValue())
	    if instance==None:
		raise IBSError("Got Update ippool info for user %s while he has no instance online on %s %s"%
												(self.user_obj.getUserID(),
												ras_msg.getRasID(),
												ras_msg.getUniqueIDValue()))

	    self.__updateInstanceInfo(instance,ras_msg["ippool_id"],ras_msg["ippool_assigned_ip"])

	if "remote_ip" in ras_msg["update_attrs"]:
	    self.__setRemoteIP(ras_msg)

    def __updateInstanceInfo(self,instance,ippool_id,ip):
	instance_info=self.user_obj.getInstanceInfo(instance)
	instance_info["attrs"]["ippool_id"]=ippool_id
	instance_info["attrs"]["ippool_assigned_ip"]=ip
	
    def __setRemoteIP(self,ras_msg):
	instance=self.user_obj.getInstanceFromUniqueID(ras_msg.getRasID(),ras_msg.getUniqueIDValue())
	self.user_obj.getInstanceInfo(instance)["attrs"]["remote_ip"]=ras_msg["remote_ip"]

class IPpoolAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)

    def changeInit(self,ippool_name):
	self.ippool_name=ippool_name
	self.useGenerateQuery({"ippool":ippool_main.getLoader().getIPpoolByName(self.ippool_name).getIPpoolID()})

    def deleteInit(self):
	self.useGenerateQuery(["ippool"])

class IPpoolAttrHolder(AttrHolder):
    def __init__(self,ippool_id):
	self.ippool_id=int(ippool_id)

    def getParsedDic(self):
	return {"ippool":ippool_main.getLoader().getIPpoolByID(self.ippool_id).getIPpoolName()}

class IPpoolAttrSearcher(AttrSearcher):
    def run(self):
	self.exactSearchOnUserAndGroupAttrs("ippool","ippool",lambda x:ippool_main.getLoader().getIPpoolByName(x).getIPpoolID())

class IPpoolAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(IPpoolAttrUpdater,["ippool"])
	self.registerAttrHolderClass(IPpoolAttrHolder,["ippool"])
	self.registerAttrSearcherClass(IPpoolAttrSearcher)
