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