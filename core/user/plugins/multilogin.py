from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_searcher import AttrSearcher
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *

attr_handler_name="multi login"
def init():
    user_main.getUserPluginManager().register("multi_login",MultiLogin)
    user_main.getAttributeManager().registerHandler(MultiLoginAttrHandler(),["multi_login"],["multi_login"],[])

class MultiLogin(user_plugin.UserPlugin): 
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
	self.multi_login=1
	if user_obj.getUserAttrs().hasAttr("multi_login"):
	    self.multi_login=int(user_obj.getUserAttrs()["multi_login"])
	
    def login(self,args):
	if self.user_obj.instances>self.multi_login:
	    raise LoginException(errorText("USER_LOGIN","MAX_CONCURRENT"))
	
class MultiLoginAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)

    def changeInit(self,multi_login):
	try:
	    self.multi_login=int(multi_login)
	except:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_MULTI_LOGIN"))

	if self.multi_login < 0 or self.multi_login > 255:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_MULTI_LOGIN"))

	self.useGenerateQuery({"multi_login":self.multi_login})

    def deleteInit(self):
	self.useGenerateQuery(["multi_login"])	

class MultiLoginAttrSearcher(AttrSearcher):
    def run(self):
	self.ltgtSearchOnUserAndGroupAttrs("multi_login","multi_login_op","multi_login")

class MultiLoginAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(MultiLoginAttrUpdater,["multi_login"])
	self.registerAttrSearcherClass(MultiLoginAttrSearcher)
