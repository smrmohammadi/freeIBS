from ibs_exceptions import *
from core.lib.general import *
from core.errors import errorText
from core.db import db_main


class User:
    """
	Base User Class
	All Types of user should inherit from this, and call this class functions when overriding em
    """
    def __init__(self, user_id, obj_type,user_attributes_obj):
	"""
	    user_id(integer): id of user
	    obj_type(string): type of user either "Normal" or "VoIP"
	    user_attribute_obj(UserAttribute instance): container of user attributes. it also take care of
							group attributes when asked for getAttr
	"""
    	self.instances=0
	self.instance_info={}
	self.attributes_obj=user_attributes_obj
	self.user_obj_type=obj_type
	self.__setInitialVariables()
	
	user_main.getUserPluginManager().callHooks("USER_INIT",self)

    def __setInitialVariables(self):
	self.initial_credit=self.getAttribute("credit")

    def __str__(self):
	return "User with id %s"&self.user_id

    def getAttr(self,attr_name):
	self.attributes_obj.getAttribute(attr_name)

    def hasAttr(self,attr_name):
	self.attributes_obj.hasAttribute(attr_name)

    def login(self,ras_msg):
	self.instances+=1
	self.instance_info["auth_ras_msg"]=ras_msg
	self.instance_info["unique_id"]=ras_msg["unique_id"]
	self.instance_info["ras_attrs"]=ras_msg.getAttrs()
	user_main.getUserPluginManager().callHooks("USER_LOGIN",self,ras_msg)
	
    def logout(self,instance,ras_msg):
	"""
	    this method calls before user logout process start
	    we call plugins now, so they'll see the correct user object
	    that not changed for logout
	"""
	user_main.getUserPluginManager().callHooks("USER_LOGOUT",self,instance,ras_msg)

#    def postLogout(self,instace):
#	"""
#	    calls after user logout proccess finished, it's children job to call this function after 
#	    they've done with logouting user
#	"""
	self.instances-=1
	_index=self.instances
	del(self.instance_info[_index])

    def canStayOnline(self):
	return reduce(lambda x,y:x+y,user_main.getUserPluginManager().callHooks("USER_CAN_STAY_ONLINE"))

    def calcCurrentCredit(self):
	return self.initial_credit - self.charge_obj.calcCreditUsage(self)

    def commit(self):
	"""
	    saves all changed user info from memory into DB
	"""
	query=reduce(lambda x,y:x+y,user_main.getUserPluginManager().callHooks("USER_COMMIT",self))
	db_main.getHandle().transactionQuery(query)
	
    def _reload(self,new_user_attributes):
	user_main.getUserPluginManager().callHooks("USER_RELOAD",self,new_user_attributes)
	self.attributes_obj=new_user_attributes

    def getRasIDAndPort(self,instance):
	"""
	    return a tuple of (ras_id,port) that instance of user logged into
	"""
	pass

