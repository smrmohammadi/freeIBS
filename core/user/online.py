from core.user import user_main,normal_user,loading_user,user

class OnlineUsers:
    def __init__(self):
	self.user_onlines={}#user_id=>user_obj
	self.ras_onlines={}#(ras_id,unique_id)=>user_obj
	self.loading_user=loading_user.LoadingUser()

    def __loadUserObj(self,loaded_user,obj_type):
	return user.User(loaded_user,obj_type)

    def __addToOnlines(self,user_obj):
	self.user_onlines[user_obj.getUserID()]=user_obj
	self.ras_onlines[user_obj.getGlobalUniqueID()]=user_obj

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
	user_obj=self.getNormalUserObj(ras_msg["username"])
	if user_obj==None:
	    toLog("Got internet stop for user %s, but he's not online"%ras_msg["username"],LOG_DEBUG)
	    return
	self.loading_user.loadingStart(user_obj.getUserID())
	try:
	    instance=user_obj.getInstanceFromRasMsg(ras_msg)
	    if instance==None:
		raise LoginException(errorText("USER","CANT_FIND_INSTANCE")%(user_obj.getUserID(),ras_msg.getRasID(),ras_msg.getUniqueIDValue()))
	    user_obj.logout(instance,ras_msg)
	finally:
	    self.loading_user.loadingEnd(user_obj.getUserID())
    

    	