import itertools
import types
from core.bandwidth_limit import bw_main
from core.bandwidth_limit.user_leaf import UserLeaf

class Leaf:
    def __init__(self,leaf_id,leaf_name,parent_id,interface_id,total_bw_kbits,default_bw_kbits,services):
	"""
	    services(list of LeafService Instances): services belongs to this leaf
	"""
	self.leaf_id=leaf_id
	self.leaf_name=leaf_name
	self.parent_id=parent_id
	self.interface_id=interface_id
	self.total_bw_kbits=total_bw_kbits
	self.default_bw_kbits=default_bw_kbits
	self.services=services
	
    def getLeafID(self):
	return self.leaf_id

    def getLeafName(self):
	return self.leaf_name

    def getServices(self):
	return self.services
	
    def getTotalBwLimit(self):
	return self.total_bw_kbits

    def getDefaultBwLimit(self):
	return self.default_bw_kbits
    #########################
    def getParentNode(self):
	return bw_main.getLoader().getNodeByID(self.getParentNodeID())	

    def getParentNodeID(self):
	return self.parent_id
    ##########################
    def getInterfaceID(self):
	return self.interface_id

    def getInterface(self):
	return bw_main.getLoader().getInterfaceByID(self.getInterfaceID())

    def getInterfaceName(self):
	return self.getInterface().getInterfaceName()
    ###########################
    def createUserLeaf(self,ip_addr,direction):
	return UserLeaf(self,ip_addr,direction)
    ###########################
    def hasService(self,service_tuple):
	"""
	    check if this leaf has a service with this protocol and filter
	    service_tuple(tuple): (protocol,filter)
	"""
	for service in self.getServices():
	    if service.hasOverLap(service_tuple):
		return True
	return False
    ############################
    def hasServiceID(self,service_id):
	for service in self.getServices():
	    if service.getLeafServiceID()==service_id:
		return True
	return False
    ###########################
    def registerInParent(self):
	"""
	    register ourself in parent node
	"""
	bw_main.getLoader().getNodeByID(self.getParentNodeID()).registerLeaf(self.getLeafID())

    def unregisterInParent(self):
	"""
	    unregister ourself in parent node, useful when a leaf has been deleted
	"""
	bw_main.getLoader().getNodeByID(self.getParentNodeID()).unregisterLeaf(self.getLeafID())

    ###########################
    def getInfo(self):
	return {"leaf_id":self.getLeafID(),
		"leaf_name":self.getLeafName(),
		"parent_id":self.getParentNodeID(),
		"interface_id":self.getInterfaceID(),
		"interface_name":self.getInterfaceName(),
		"total_limit_kbits":self.getTotalBwLimit(),
		"default_limit_kbits":self.getDefaultBwLimit(),
		"services":map(lambda service:service.getInfo(),self.getServices())}

#########################################################################################
	
class LeafService:
    def __init__(self,leaf_service_id,leaf_id,protocol,_filter,limit_kbytes):
	"""
	    _filter(string): until now, it has two parts, a type and a value
			     type is filter identifier like sport,dport,icmp-type and value
			     is port numbers or icmp type
	"""
	self.leaf_service_id=leaf_service_id
	self.leaf_id=leaf_id
	self.protocol=protocol
	self._filter=_filter
	self.limit_kbytes=limit_kbytes


    def getBwLimit(self):
	return self.limit_kbytes

    def getProtocol(self):
	return self.protocol
    
    def getFilter(self):
	return self._filter

    def getLeafServiceID(self):
	return self.leaf_service_id

    def getLeafID(self):
	return self.leaf_id

    def getLeafName(self):
	return bw_main.getLoader().getLeafByID(self.getLeafID()).getLeafName()

    def getInfo(self):
	return {"leaf_service_id":self.getLeafServiceID(),
		"filter":self.getFilter(),
		"protocol":self.getProtocol(),
		"limit_kbits":self.getBwLimit(),
		"leaf_id":self.getLeafID(),
		"leaf_name":self.getLeafName()}


    def hasOverLap(self,other):
	"""
	    check if this service has overlap with "other" service
	    other can be another LeafService Instance or a tuple containing (protocol,filter)
	"""
	if type(other) in [types.TupleType,types.ListType]:
	    return other[0]==self.getProtocol() and self.__filterHasOverlap(other[1],self.getFilter())
	else:
	    return other.getProtocol()==self.getProtocol() and self.__filterHasOverLap(other.getFilter(),self.getFilter())

    def __filterHasOverLap(self,filter1,filter2):
	sp1=filter1.split()
	sp2=filter2.split()
	if sp1[0]!=sp2[0]:
	    return False
	ports1=sp1.split(",")
	ports2=sp2.split(",")
	for port in ports1:
	    if port in ports2:
		return True
	return False

#########################################################################################
