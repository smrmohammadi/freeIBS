from core.user import user_plugin,user_main,attribute
from core.user.info_holder import InfoHolder
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *

info_holder_name="multi login"
def init():
    user_main.getAttributeManager().registerHandler(MultiLoginAttrHandler(),["multi_login"])

class MultiLogin(user_plugin.UserPlugin): ### XXX To ChecK!
    def __init__(self,user_obj):
	user_plugin.UserPlugin(self,user_obj)
	self.multilogin=1
	if user_obj.user_obj_type == "normal":
	    if user_obj.extended_attrs.has_key("MULTILOGIN"):
		self.multilogin=user_obj.extended_attrs["MULTILOGIN"]
	
    def login(self,args):
	if self.instances>self.multilogin:
	    if self.user_obj.user_obj_type == "normal":
		error_text=errorText("NORMAL_USER_LOGIN","MAX_CONCURRENT")
	    elif self.user_obj.user_obj_type == "voip":
		error_text=errorText("VOIP_USER_LOGIN","MAX_CONCURRENT")
	
	raise loginException(error_text)

class MultiLoginInfoHolder(InfoHolder):
    def __init__(self,multi_login):
	InfoHolder.__init__(self,info_holder_name)
	try:
	    self.multi_login=int(multi_login)
	except:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_MULTI_LOGIN"))

	if self.multi_login < 0 or self.multi_login > 255:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_MULTI_LOGIN"))

	self.useGenerateQuery({"multi_login":self.multi_login})

	

class MultiLoginAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,info_holder_name)
	self.registerInfoHandlerClass(MultiLoginInfoHolder,["multi_login"])

