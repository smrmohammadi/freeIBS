class RasMsgDispatcher:
    def dispatch(self,ras_msg):
	dispatch_methods={"INTERNET_AUTHENTICATE":self._internetAuthenticate,
			  "INTERNET_STOP":self._internetStop}
	action=ras_msg.getAction()
	return apply(dispatch_methods[action],[ras_msg])

    def _internetAuthenticate(self,ras_msg):
	user_main.getOnline().internetAuthenticate(ras_msg)

    def _internetStop(self,ras_msg):
	user_main.getOnline().internetStop(ras_msg)
	
	    
	    