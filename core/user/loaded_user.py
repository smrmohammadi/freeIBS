from core.user import user_main

class LoadedUser:
    """
	Loaded User instances are keep in memory and user pool
	Loaded User is a container of user information, and should be reloadable.
	All of information we contain maybe changed so implemention should consider this
    """
    def __init__(self,basic_user,user_attrs,user_locks):
	"""
	    basic_user(BasicUser instance): basic user information
	    user_attrs(UserAttributes instance): user attribute instance
	    user_locks(list of UserLock instances): 
	"""
	self.basic_user=basic_user
	self.user_attrs=user_attrs
	self.user_locks=user_locks

    def getBasicUser(self):
	return self.basic_user
	
    def getUserAttrs(self):
	return self.user_attrs

    def getUserID(self):
	return self.getBasicUser().getUserID()

    def hasNormalLogin(self):
	return self.user_attrs.hasAttribute("normal_username")
    
    def getNormalUsername(self):
	return self.user_attrs.getAttribute("normal_username")
	
    def hasAttr(self,attr_name):
	self.getUserAttrs().hasAttribute(attr_name)

    def getUserInfo(self):
	"""
	    return a dic of user informations, useful for passing to interface
	"""
	return {"basic_info":self.getBasicUser().getInfo(),
		"attrs":user_main.getAttributeManager().parseAttrs(self.getUserAttrs().getAllAttributes()),
		"raw_attrs":self.getUserAttrs().getAllAttributes()
	       }	
    
    