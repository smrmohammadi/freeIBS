from core.ibs_exceptions import *
from core.lib.general import *
from core.errors import errorText
from core.db import db_main
from core.user import normal_user
import operator

class User:
    """
	Base User Class, for online users
    """
    def __init__(self, loaded_user, _type):
	"""
	    loaded_user(LoadedUser instance): Loaded user instance
	    o_type(string): type of user either "Normal" or "VoIP"
	"""
    	self.instances=0
	self.__instance_info={}
	self.loaded_user=loaded_user_instance
	self.__type=_type
	self.__type_obj=self.__loadTypeObj(_type)
	self.__setInitialVariables()
	
	user_main.getUserPluginManager().callHooks("USER_INIT",self)

    def __loadTypeObj(self,_type):
	if _type=="Normal":
	    return normal_user.NormalUser(self)

    def __setInitialVariables(self):
	self.initial_credit=self.getLoadedUser().getBasicUser().getInitialCredit()

    def __str__(self):
	return "User with id %s"%self.getLoadedUser().getUserID()

    def getLoadedUser(self):
	return self.loaded_user

    def getUserID(self):
	return self.getLoadedUser().getUserID()

    def getUserAttrs(self):
	return self.getLoadedUser().getUserAttrs()	

    def getType(self):
	return self.__type

    def getTypeObj(self):
	return self.__type_obj
    
    def isNormalUser():
	return self.getType()=="Normal"

###################################################
    def getInstanceInfo(self,instance):
	return self.__instance_info[instance-1]

    def getRasID(self,instance):
	return self.getInstanceInfo(instance)["ras_id"]

    def getUniqueIDValue(self,instance):
	return self.getInstanceInfo(instance)["unique_id_val"]
	
    def getGlobalUniqueID(self,instance):
	return (self.getRasID(instance),self.getUniqueIDValue(instance))

##################################################
    def getInstanceFromRasMsg(self,ras_msg):
	ras_id=ras_msg.getRasID()
	unique_id_val=ras_msg.getUniqueIDValue()
	for instance in self.instances:
	    instance_info=self.getInstanceInfo(instance)
	    if instance_info["ras_id"]==ras_id and instance_info["unique_id_val"]==unique_id_val:
		return instance
	return None
	
##################################################
    def calcCurrentCredit(self):
	return self.initial_credit - self.charge.calcCreditUsage()

    def calcInstanceCreditUsage(self,instance):
	return self.charge.calcInstanceCreditUsage(instance)
##################################################

    def login(self,ras_msg):
	self.instances+=1
	self.instance_info["auth_ras_msg"]=ras_msg
	self.instance_info["unique_id"]=ras_msg["unique_id"]
	self.instance_info["unique_id_val"]=ras_msg.getUniqueIDValue()
	self.instance_info["ras_attrs"]=ras_msg.getAttrs()
	self.instance_info["ras_id"]=ras_msg.getRasID()
	user_main.getUserPluginManager().callHooks("USER_LOGIN",self,ras_msg)
	
    def logout(self,instance,ras_msg):
	"""
	    this method calls before user logout process start
	    we call plugins now, so they'll see the correct user object
	    that not changed for logout
	"""
	user_main.getUserPluginManager().callHooks("USER_LOGOUT",self,instance,ras_msg)
	self.instances-=1
	_index=self.instances
	del(self.instance_info[_index])

    def update(self,ras_msg):
	"""
	    plugins can update themeselved whenever we recieved an update packet, with updated info 
	    from radius server
	"""
	user_main.getUserPluginManager().callHooks("UPDATE",self,instance,ras_msg)

    def canStayOnline(self):
	return reduce(operator.add,user_main.getUserPluginManager().callHooks("USER_CAN_STAY_ONLINE"))

    def commit(self):
	"""
	    saves all changed user info from memory into DB
	"""
	query=reduce(operator.add,user_main.getUserPluginManager().callHooks("USER_COMMIT",self))
	db_main.getHandle().transactionQuery(query)
	
    def _reload(self):
	user_main.getUserPluginManager().callHooks("USER_RELOAD",self)

