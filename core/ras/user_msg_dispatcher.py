from core.ras import ras_main

class UserMsgDispatcher:
    
    def dispatch(self,user_msg):
	dispatch_methods={"GET_INOUT_BYTES":self._getInOutBytes,"KILL_USER":self._killUser,"SIMPLE_BANDWIDTH_LIMIT":self._applySimpleBwLimit}
	action=user_msg.getAction()
	if dispatch_methods.has_key(action):
	    return apply(dispatch_methods[action],[user_msg])
	else:
	    return self._dispatchByRas(user_msg)

    def _getInOutBytes(self,user_msg):
	return ras_main.getLoader().getRasByID(user_msg["ras_id"]).getInOutBytes(user_msg)

    def _killUser(self,user_msg):
	return ras_main.getLoader().getRasByID(user_msg["ras_id"]).killUser(user_msg)

    def _applySimpleBwLimit(self,user_msg):
	return ras_main.getLoader().getRasByID(user_msg["ras_id"]).applySimpleBwLimit(user_msg)

    def _dispatchByRas(self,user_msg):
	return ras_main.getLoader().getRasByID(user_msg["ras_id"]).dispatch(user_msg)