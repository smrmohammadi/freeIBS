from core.ras import ras_main

class UserMsgDispatcher:
    
    def dispatch(self,user_msg):
	dispatch_methods={"GET_INOUT_BYTES":self._getInOutBytes,"KILL_USER":self._killUser}
	action=user_msg.getAction()
	return apply(dispatch_methods[action],[user_msg])

    def _getInOutBytes(self,user_msg):
	return ras_main.getLoader().getRasByID(user_msg["ras_id"]).getInOutBytes(user_msg)

    def _killUser(self,user_msg):
	return ras_main.getLoader().getRasByID(user_msg["ras_id"]).killUser(user_msg)
	