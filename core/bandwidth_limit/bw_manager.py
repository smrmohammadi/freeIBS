from core.bandwidth_limit import bw_main
from core.ibs_exceptions import *

class BWManager:
    def __init__(self):
	self.user_leaves={} #ipaddr=>(Send User Leaf instance,Recv User Leaf instance)

    def applyBwLimit(self,ip_addr,send_leaf_id,recv_leaf_id):
	send_user_leaf=bw_main.getLoader().getLeafByID(send_leaf_id).createUserLeaf(ip_addr,"send")
	recv_user_leaf=bw_main.getLoader().getLeafByID(recv_leaf_id).createUserLeaf(ip_addr,"receive")
	self.__addToLeaves(ip_addr,send_user_leaf,recv_user_leaf)
	send_user_leaf.addToTC()
	recv_user_leaf.addToTC()
	
    def __addToLeaves(self,ip_addr,send_user_leaf,recv_user_leaf):
	if ip_addr in self.user_leaves:
	    toLog("ip address %s is already in bw manager user leaves",LOG_ERROR)
	self.user_leaves[ip_addr]=(send_user_leaf,recv_user_leaf)


    def removeBwLimit(self,ip_addr):
	try:
	    send_user_leaf,recv_user_leaf=self.user_leaves[ip_addr]
	    send_user_leaf.delFromTC()
	    recv_user_leaf.delFromTC()
	    del(self.user_leaves[ip_addr])
	except KeyError:
	    logException(LOG_ERROR,"ip address %s is not bw manager user leaves")
