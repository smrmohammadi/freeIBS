from core.ibs_exceptions import *
from core.lib.general import *
from core.errors import errorText
from core.db import db_main,ibs_db
from core.user import normal_user,user_main
from core.ras.msgs import UserMsg
import operator


class User:
    """
	Base User Class, for online users
    """
    remove_ras_attrs=["pap_password","chap_password","ms_chap_response","ms_chap2_response","start_accounting"]

    def __init__(self, loaded_user, _type):
	"""
	    loaded_user(LoadedUser instance): Loaded user instance
	    o_type(string): type of user either "Normal" or "VoIP"
	"""
    	self.instances=0
	self.__instance_info=[]
	self.loaded_user=loaded_user
	self.__type=_type
	self.__type_obj=self.__loadTypeObj(_type)
	self.__setInitialVariables()
	
	user_main.getUserPluginManager().callHooks("USER_INIT",self)

    def __loadTypeObj(self,_type):
	if _type=="Normal":
	    return normal_user.NormalUser(self)

    def __setInitialVariables(self):
	self.__setInitialCredit()

    def __setInitialCredit(self):
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
    
    def isNormalUser(self):
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
	return self.getInstanceFromUniqueID(ras_id,unique_id_val)
	
    def getInstanceFromUniqueID(self,ras_id,unique_id_val):
	for instance in range(1,self.instances+1):
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
    def createUserMsg(self,instance,action):
	"""
	    create a UserMsg ready to send to a ras.
	    Information necessary for ras will be set from user "instance" information
	"""
	instance_info=self.getInstanceInfo(instance)
	msg=UserMsg()
	msg["ras_id"]=instance_info["ras_id"]
	msg["unique_id"]=instance_info["unique_id"]
	msg[instance_info["unique_id"]]=instance_info["unique_id_val"]
	msg["user_obj"]=self
	msg["instance"]=instance
	msg.setAction(action)
	return msg

##################################################
    def setKillReason(self,instance,reason):
	instance_info=self.getInstanceInfo(instance)
	if instance_info["attrs"].has_key("kill_reason"):
	    instance_info["attrs"]["kill_reason"]+=", %s"%reason
	else:
	    instance_info["attrs"]["kill_reason"]=reason

##################################################
    def __filterRasAttrs(self,attrs):
	cattrs=attrs.copy()
	for attr_name in self.remove_ras_attrs:
	    if cattrs.has_key(attr_name):
		del(cattrs[attr_name])
	return cattrs
##################################################
    def login(self,ras_msg):
	self.instances+=1
	self.__instance_info.append({})
	instance_info=self.getInstanceInfo(self.instances)
	instance_info["auth_ras_msg"]=ras_msg
	instance_info["unique_id"]=ras_msg["unique_id"]
	instance_info["unique_id_val"]=ras_msg.getUniqueIDValue()
	instance_info["attrs"]=self.__filterRasAttrs(ras_msg.getAttrs())
	instance_info["ras_id"]=ras_msg.getRasID()
	instance_info["check_online_fails"]=0
	instance_info["login_time"]=time.time()
	try:
	    user_main.getUserPluginManager().callHooks("USER_LOGIN",self,[ras_msg])
	except Exception,e:
	    instance_info["successful_auth"]=False
	    self.setKillReason(self.instances,str(e))
#	    self.getTypeObj().logToConnectionLog(self.instances,0).runQuery()
#	    self.instances-=1
	    self.logout(self.instances,ras_msg)
	    raise
	instance_info["successful_auth"]=True
	
    def logout(self,instance,ras_msg):
	"""
	    this method calls before user logout process start
	    we call plugins now, so they'll see the correct user object
	    that not changed for logout
	"""
	self.getInstanceInfo(instance)["logout_ras_msg"]=ras_msg
	used_credit=self.charge.calcInstanceCreditUsage(instance)
	query=self.getTypeObj().logout(instance,ras_msg,used_credit)
	if self.instances==1:
	    query+=self.commit(self.charge.calcCreditUsage())
	query.runQuery()
	user_main.getUserPluginManager().callHooks("USER_LOGOUT",self,[instance,ras_msg])
	self.instances-=1
	del(self.__instance_info[self.instances])

    def update(self,ras_msg):
	"""
	    plugins can update themeselves whenever we recieved an update packet, with updated info 
	    from radius server
	    They can return True to cause a recalcEvent for user
	"""
	ret=user_main.getUserPluginManager().callHooks("UPDATE",self,[ras_msg])
	if True in ret:
	    return True
	return False

    def canStayOnline(self):
	results=filter(lambda x:x!=None,user_main.getUserPluginManager().callHooks("USER_CAN_STAY_ONLINE",self))
	return reduce(operator.add,results)

    def commit(self,used_credit):
	"""
	    saves all changed user info from memory into DB
	"""
	query=reduce(operator.add,filter(lambda x:x!=None,user_main.getUserPluginManager().callHooks("USER_COMMIT",self)))
	query+=self.__commitCreditQuery(used_credit)
	return query
	
    def __commitCreditQuery(self,used_credit):
	return ibs_db.createUpdateQuery("users",{"credit":"credit - %s"%used_credit},"user_id=%s"%self.getUserID())
    
    def _reload(self):
	self.__setInitialCredit()
	user_main.getUserPluginManager().callHooks("USER_RELOAD",self)

