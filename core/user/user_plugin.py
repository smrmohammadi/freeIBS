from core import defs
from core.user import user_main,can_stay_online_result
from core.errors import errorText
from core.ibs_exceptions import *
import itertools

class BaseUserPlugin:
    def __init__(self,user_obj):
	"""
	    init function called when a new instance of user created
	"""
	self.user_obj=user_obj

    ########################
    def createCanStayOnlineResult(self):
	return can_stay_online_result.CanStayOnlineResult()


class UserPlugin(BaseUserPlugin):
    def __init__(self,user_obj):
	BaseUserPlugin.__init__(self,user_obj)

    def login(self,ras_msg):
	"""
	    called when an instance of user logs in.
	    the new user instance is equal to self.user_obj.instances
	    we can raise a LoginException(reason_text) to prevent new instance from logging in
	"""
	pass

    def commit(self):
	"""
	    tell plugin to commit itself to db
	    this should be done by returning a query 
	"""
	return ""

    def logout(self,instance,ras_msg):
	"""
	    called when an instance of user logs out
	"""
	pass
	
    def canStayOnline(self):
	"""
	    called during user_obj.canStayOnline
	    we must return instance of CanStayOnlineResult
	"""
	return self.createCanStayOnlineResult()

    def _reload(self):
	"""
	    called when user_obj.reload is called
	"""
	pass

    def update(self,ras_msg):
	pass

class AttrCheckUserPlugin(BaseUserPlugin):
    """
	This is parent class for User Plugins that do the has attribute checkings automatically
	login,logout,commit,canStayOnline,update is replaced with identical names s_login,s_logut,s_commit,s_canStayOnline,s_update
	these methods are only called if user has attribute "attr_name" given in initializer
	WARNING: _reload method has no s_reload, it'll always call the plugin _reload method. Plugin reload method
	    should call this class reload method first to ensure has_attr update
    """
    def __init__(self,user_obj,attr_name):
	BaseUserPlugin.__init__(self,user_obj)
	self.has_attr_name=attr_name
	self._setHasAttr(attr_name)
	
    def __getattr__(self,name):
	if self.hasAttr() and name in ("update","login","logout","commit","canStayOnline"):
	    return getattr(self,"s_%s"%name)
	
    	    
    def _setHasAttr(self,attr_name):
	self.has_attr=self.user_obj.getLoadedUser().hasAttr(attr_name)

    def hasAttr(self):
	return self.has_attr
    
    def s_login(self,ras_msg):
	pass

    def s_commit(self):
	pass

    def s_logout(self,instance,ras_msg):
	pass
    
    def s_canStayOnline(self):
	pass

    def _reload(self):
	self._setHasAttr(self.has_attr_name)

    def s_update(self,ras_msg):
	pass

class UserPluginManager:
    def __init__(self):
	self.__plugin_classes=([],[],[],[],[],[],[],[],[],[]) #priority:[(plugin_class,plugin_name),(plugin_class,plugin_name),...]
	
    def register(self,plugin_name,plugin_class,priority=5):
	"""
	    register new plugin to be called on user hooks
	    plugin_name(string): name of plugin, plugin class instance would be accessible in user with this name(user_obj.plugin_name)
	    plugin_class(Class): class of plugin. An instance would be created for each user object
	    priority(integer): an integer between 0-9. Shows in what order methods should be called
			       smaller number favored more. For regular operations better set 5
	    
	"""
	if priority<0 or priority>9:
	    priority=5
	self.__plugin_classes[priority].append((plugin_class,plugin_name))

    def callHooks(self,hook,user_obj,args=[]):
	"""
	    run plugins methods for hook
	    args is a list of additional arguments
	"""
	if hook=="USER_INIT":
	    return self.__initPluginsForUser(user_obj)
	
	elif hook=="USER_LOGIN":
	    return self.__callPluginsMethod(user_obj,args,"login")

	elif hook=="USER_LOGOUT":
	    return self.__callPluginsMethod(user_obj,args,"logout")	    

	elif hook=="USER_COMMIT":
	    return self.__callPluginsMethod(user_obj,args,"commit")	    

	elif hook=="USER_CAN_STAY_ONLINE":
	     return self.__callPluginsMethod(user_obj,args,"canStayOnline")
	
	elif hook=="USER_RELOAD":
	    return self.__callPluginsMethod(user_obj,args,"_reload")

	elif hook=="UPDATE":
	    return self.__callPluginsMethod(user_obj,args,"update")

	raise IBSError(errorText("PLUGINS","INVALID_HOOK")%hook)

    def __initPluginsForUser(self,user_obj):
	"""
	    initialize plugin for user
	    for user plugins we'll create an object of plugin and put it
	    in user_obj with the name of plugin
	"""
	for (plugin_class,plugin_name) in apply(itertools.chain,self.__plugin_classes):
	    try:
		setattr(user_obj,plugin_name,plugin_class(user_obj))
	    except:
		logException(LOG_ERROR,"UserPluginManager.__initPluginsForUser")

    def __callPluginsMethod(self,user_obj,args,method_name):
	"""
	    call plugin method "method_name" with "args" list as argument for object "user_obj"
	"""	
	return map(lambda plugin_tuple:apply(getattr(getattr(user_obj,plugin_tuple[1]),method_name),args),
	           apply(itertools.chain,self.__plugin_classes))

	