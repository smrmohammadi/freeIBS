from core.user import user_main,normal_user,loading_user,user
from core.ibs_exceptions import *
import copy

class OnlineUsers:
    def __init__(self):
	self.user_onlines={}#user_id=>user_obj
	self.ras_onlines={}#(ras_id,unique_id)=>user_obj
	self.loading_user=loading_user.LoadingUser()

    def __loadUserObj(self,loaded_user,obj_type):
	return user.User(loaded_user,obj_type)

##############################################
    def __addToOnlines(self,user_obj):
	self.user_onlines[user_obj.getUserID()]=user_obj
	self.ras_onlines[user_obj.getGlobalUniqueID(user_obj.instances)]=user_obj

    def __removeFromOnlines(self,user_obj,global_unique_id):
	del(self.user_onlines[user_obj.getUserID()])
	del(self.ras_onlines[global_unique_id])
	

############################################
    def getUserOnlines(self):
	return copy.copy(self.user_onlines)

############################################
    def reloadUser(self,user_id):
	self.loading_user.loadingStart(loaded_user.getUserID())
	try:
	    user_obj=getUserObj(user_id)
	    if user_obj==None:
		toLog("Reload User called while user is not online",LOG_ERROR)
	    else:
		user_obj._reload()
	finally:
	    self.loading_user.loadingEnd(loaded_user.getUserID())

############################################
    def isUserOnline(self,user_id):
	return self.user_onlines.has_key(user_id)

    def getUserObj(self,user_id):
	"""
	    return User instance of online user, or None if no user is online
	"""
	try:
	    return self.user_onlines[user_id]
	except KeyError:
	    return None

#############################################
    def internetAuthenticate(self,ras_msg):
	loaded_user=user_main.getUserPool().getUserByNormalUsername(ras_msg["username"],True)
	self.loading_user.loadingStart(loaded_user.getUserID())
	try:
	    try:
	        user_obj=self.getUserObj(loaded_user.getUserID())
		if user_obj==None:
		    user_obj=self.__loadUserObj(loaded_user,"Normal")
	        user_obj.login(ras_msg)
		self.internetAuthenticateSuccessfull(user_obj)
	    except:
		loaded_user.setOnlineFlag(False)
		#log to connection log
		raise
	finally:
	    self.loading_user.loadingEnd(loaded_user.getUserID())
	    
    def internetAuthenticateSuccessfull(self,user_obj):
	self.__addToOnlines(user_obj)
############################################
    def internetStop(self,ras_msg):
	loaded_user=user_main.getUserPool().getUserByNormalUsername(ras_msg["username"])
	self.loading_user.loadingStart(loaded_user.getUserID())
	try:
	    user_obj=self.getUserObj(loaded_user.getUserID())
	    if user_obj==None:
		toLog("Got internet stop for user %s, but he's not online"%ras_msg["username"],LOG_DEBUG)
	        return
	    instance=user_obj.getInstanceFromRasMsg(ras_msg)
	    if instance==None:
		raise LoginException(errorText("USER","CANT_FIND_INSTANCE")%(loaded_user.getUserID(),ras_msg.getRasID(),ras_msg.getUniqueIDValue()))

	    global_unique_id=user_obj.getGlobalUniqueID(user_obj.instances)
	    user_obj.logout(instance,ras_msg)
	    if user_obj.instances==0:
		self.__removeFromOnlines(user_obj,global_unique_id)
	finally:
	    self.loading_user.loadingEnd(loaded_user.getUserID())
    
############################################
    	