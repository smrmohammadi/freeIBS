import os
from core import defs
from core.ibs_exceptions import *

class IPTables:
    def addMark(self,mark_id,ip_addr,direction,leaf_service):
	"""
	    add a rule to iptables mangle table to mark packets from "direction" of "ip_addr" with conditions 
	    in leaf_service, with "mark_id"
	    mark_id(int): mark to set for packets
	    ip_addr(str): ip address of source or destination, depends on direction
	    direction(str): can be "send" or "receive"
	    leaf_service(Leaf instance or None): leaf service to create conditions
						 currently we just add protocol from leafservice
						 and filter should be in iptables syntax without -- prefix
	"""
	self.runIPTables("-t mangle -A PREROUTING %s -j MARK --set-mark %s"%
			    (self.__createCondition(ip_addr,direction,leaf_service),mark_id))

    def delMark(self,mark_id,ip_addr,direction,leaf_service):
	"""
	    delete a mark rule from iptables, same as addMark
	"""
	self.runIPTables("-t mangle -D PREROUTING %s -j MARK --set-mark %s"%
			    (self.__createCondition(ip_addr,direction,leaf_service),mark_id))

    def __createCondition(self,ip_addr,direction,leaf_service):
	if direction=="send":
	    cond="-s"
	else:
	    cond="-d"
	cond+=" %s "%ip_addr
	if leaf_service!=None:
	    protocol=leaf_service.getProtocol()
	    if protocol in ("udp","tcp"):
		cond+=" -m multiport "
	    cond+=" -p %s --%s"%(ip_addr,protocol,leaf_service.getFilter())
	return cond

    def runIPTables(self,command):
	ret_val=os.system("%s %s"%(defs.BW_IPTABLES_COMMAND,command))
	if ret_val!=0:
	    toLog("iptables command '%s %s' returned non zero value %s"%(defs.BW_IPTABLES_COMMAND,command,ret_val),LOG_DEBUG)
    