from core.user import user_plugin,user_main,attribute
from core.ippool import ippool_main
from core.errors import *
from core.ibs_exceptions import *

def init():
    user_main.getUserPluginManager().register("ippool",IPpoolUserPlugin)
    
class IPpoolUserPlugin(user_plugin.UserPlugin):
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
 
    def logout(self,instance,ras_msg):
	auth_ras_msg=self.user_obj.getInstanceInfo(instance)["auth_ras_msg"]
	if auth_ras_msg.hasAttr("ippool_id"):
	    ippool_main.getLoader().getIPpoolByID(auth_ras_msg["ippool_id"]).freeIP(auth_ras_msg["ippool_assigned_ip"])
	
    def update(self,ras_msg):
	if "ippool_id" in ras_msg["update_attrs"]:
	    instance=self.user_obj.getInstanceFromUniqueID(ras_msg.getRasID(),ras_msg.getUniqueIDValue())
	    if instance==None:
		raise IBSError("Got Update ippool info for user %s while he has no instance online on %s %s"%
												(self.user_obj.getUserID(),
												ras_msg.getRasID(),
												ras_msg.getUniqueIDValue()))
	    instance_info=self.user_obj.getInstanceInfo(instance)
	    instance_info["attrs"]["ippool_id"]=ras_msg["ippool_id"]
	    instance_info["attrs"]["ippool_assigned_ip"]=ras_msg["ippool_assigned_ip"]
	
	if "remote_ip" in ras_msg["update_attrs"]:
	    instance=self.user_obj.getInstanceFromUniqueID(ras_msg.getRasID(),ras_msg.getUniqueIDValue())
	    self.user_obj.getInstanceInfo(instance)["attrs"]["remote_ip"]=ras_msg["remote_ip"]