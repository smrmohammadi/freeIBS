from core import defs
from core.user import user_main
from core.errors import errorText

class UserPlugin:
    def __init__(self,user_obj):
	"""
	    init function called when a new instance of user created
	"""
	self.user_obj=user_obj

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
	    this can be done by returning a query 
	"""
	pass

    def logout(self,instance):
	"""
	    called when an instance of user logs out
	"""
	pass
	
    def canStayOnline(self):
	"""
	    called during user_obj.canStayOnline
	    we must return instance of CanStayOnlineResult
	"""
	return (defs.MAXLONG,{})

    def _reload(self,new_attributes):
	"""
	    called when user_obj.reload is called
	    new_attributes(UserAttributes instance): new attributes that will be replaced with current ones
		during calling of reload hooks, self.attributes are old values
	"""
	pass

class UserPluginManager:
    def __init__(self):
	self.__plugin_classes={} #hash {plugin_name:plugin_class}
	
    def register(self,plugin_name,plugin_class):
	"""
	    register new plugin to be called on user hooks
	"""
	self.__plugin_classes[plugin_name]=plugin_class

    def callHooks(self,hook,user_obj,args):
	"""
	    run plugins methods for hook
	    args is a list of additional arguments
	"""
	if hook=="USER_INIT":
	    return self.__initPluginsForUser(self,user_obj)
	
	elif hook=="USER_LOGIN":
	    return self.__callPluginsMethod(self,user_obj,args,"login")

	elif hook=="USER_LOGOUT":
	    return self.__callPluginsMethod(self,user_obj,args,"logout")	    

	elif hook=="USER_COMMIT":
	    return self.__callPluginsMethod(self,user_obj,args,"commit")	    

	elif hook=="USER_CAN_STAY_ONLINE":
	     return self.__callPluginsMethod(self,user_obj,args,"canStayOnline")
	
	elif hook=="USER_RELOAD":
	    return self.__callPluginsMethod(self,user_obj,args,"_reload")

	raise generalException(errorText("PLUGINS","INVALID_HOOK")%hook)

    def __initPluginsForUser(self,user_obj):
	"""
	    initialize plugin for user
	    for user plugins we'll create an object of plugin and put it
	    in user_obj with the name of plugin
	"""
	for plugin_name in self.__plugin_classes:
	    try:
		setattr(user_obj,plugin_name,self.__plugin_classes[plugin_name](user_obj))
	    except:
		logException("UserPluginManager.__initPluginsForUser")

    def __callPluginsMethod(self,user_obj,args,method_name):
	"""
	    call plugin method "method_name" with "args" list as argument for object "user_obj"
	"""	
	ret_vals=[]
	for plugin_name in self.__plugin_classes:
		ret_vals.append(apply(getattr(getattr(user_obj,plugin_name),method_name),args))

	return ret_vals
	