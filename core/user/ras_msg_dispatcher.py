from core.ibs_exceptions import *
from core.user import user_main

class RasMsgDispatcher:

    def dispatch(self,ras_msg):
	dispatch_methods={"INTERNET_AUTHENTICATE":self._internetAuthenticate,
		    	  "INTERNET_STOP":self._internetStop,
		          "INTERNET_UPDATE":self._internetUpdate,
		          "PERSISTENT_LAN_AUTHENTICATE":self._planAuthenticate,
		          "PERSISTENT_LAN_STOP":self._planStop
			 }

	action=ras_msg.getAction()
	return apply(dispatch_methods[action],[ras_msg])

    def _internetAuthenticate(self,ras_msg):
	try:
	    user_main.getOnline().internetAuthenticate(ras_msg)
	    return True
	except IBSError:
#	    logException(LOG_DEBUG,"Authenticate for user %s"%ras_msg["username"])
	    return False
	    

    def _internetStop(self,ras_msg):
	user_main.getOnline().internetStop(ras_msg)
	
    def _internetUpdate(self,ras_msg):
	user_main.getOnline().updateUser(ras_msg)

    def _planAuthenticate(self,ras_msg):
	try:
	    user_main.getOnline().persistentLanAuthenticate(ras_msg)
	    return True
	except IBSError:
#	    logException(LOG_DEBUG,"Authenticate for user %s"%ras_msg["mac"])
	    return False

    def _planStop(self,ras_msg):
	user_main.getOnline().persistentLanStop(ras_msg)
