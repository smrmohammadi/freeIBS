from core.user import user_plugin,user_main,attribute
from core.errors import *
from core.ibs_exceptions import *

def init():
    user_main.getUserPluginManager().register("password",PasswordUserPlugin,1)
    
class PasswordUserPlugin(user_plugin.UserPlugin):
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
 
    def login(self,ras_msg):
	if ras_msg.hasAttr("pap_password"):
	    if ras_msg.getRequestPacket().PwDecrypt(ras_msg["pap_password"])!=self.user_obj.getUserAttrs()["normal_password"]:
		self.__raiseIncorrectPassword()
	elif ras_msg.hasAttr("chap_password"):
	    if not ras_msg.getRequestPacket().checkChapPassword(self.user_obj.getUserAttrs()["normal_password"]):
		self.__raiseIncorrectPassword()
	else:
	    toLog("Unknown Password checking method",LOG_DEBUG)
	    self.__raiseIncorrectPassword()

    def __raiseIncorrectPassword(self):
	raise LoginException(errorText("USER","WRONG_PASSWORD"))
