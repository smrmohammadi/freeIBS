from core.bandwidth_limit import bw_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *
from core.lib.multi_strs import MultiStr
from core.db import db_main,ibs_db
from core.bandwidth_limit.node import Node
from core.charge import charge_main

class BWActions:
    def __checkLimitKbits(self,limit_kbits):
	if not isInt(limit_kbits) or limit_kbits <=0 or limit_kbits > 1024*1024:
	    raise GeneralException(errorText("BANDWIDTH","INVALID_LIMIT_KBITS")%limit_kbits)

    #############################################
    def getTree(self,interface_name):
	int_obj=bw_main.getLoader().getInterfaceByName(interface_name)
	return self.getSubTree(int_obj.getRootNodeID())

    def getSubTree(self,node_id):
	node_obj=bw_main.getLoader().getNodeByID(node_id)
	children=map(lambda child:self.getSubTree(child),node_obj.getChildren())
	leaf_children=map(lambda leaf:bw_main.getLoader().getLeafByID(leaf).getLeafName(),node_obj.getLeafChildren())
	return [node_id,children,leaf_children]

    ##############################################
    def addInterface(self,interface_name,comment):
	self.__addInterfaceCheckInput(interface_name,comment)
	interface_id=self.__getNewInterfaceID()
	self.__addInterfaceDB(interface_id,interface_name,comment)
	bw_main.getLoader().loadInterface(interface_id)
	self.addNode(interface_name,None,1024*100,1024*100)
	bw_main.getLoader().getInterfaceByName(interface_name).createTree()

    def __addInterfaceCheckInput(self,interface_name,comment):
	if bw_main.getLoader().interfaceNameExists(interface_name):
	    raise GeneralException(errorText("BANDWIDTH","INTERFACE_NAME_ALREADY_EXISTS")%interface_name)
	if not isValidName(interface_name):
	    raise GeneralException(errorText("BANDWIDTH","INVALID_INTERFACE_NAME")%interface_name)

    def __addInterfaceDB(self,interface_id,interface_name,comment):
	db_main.getHandle().transactionQuery(self.__addInterfaceQuery(interface_id,interface_name,comment))
	
    def __getNewInterfaceID(self):
	return db_main.getHandle().seqNextVal("bw_interface_interface_id_seq")

    def __addInterfaceQuery(self,interface_id,interface_name,comment):
	return ibs_db.createInsertQuery("bw_interface",{"interface_id":interface_id,
							"interface_name":dbText(interface_name),
							"comment":dbText(comment)})

    #############################################
    def addNode(self,interface_name,parent_id,rate_kbits,ceil_kbits):
	self.__addNodeCheckInput(interface_name,parent_id,rate_kbits,ceil_kbits)
	int_obj=bw_main.getLoader().getInterfaceByName(interface_name)
	node_id=self.__getNewNodeID()
	self.__addNodeDB(node_id,int_obj.getInterfaceID(),parent_id,rate_kbits,ceil_kbits)
	bw_main.getLoader().loadNode(node_id)
	node_obj=bw_main.getLoader().getNodeByID(node_id)
	node_obj.registerInParent()
	node_obj.createSubTree()
	
    def __addNodeCheckInput(self,interface_name,parent_id,rate_kbits,ceil_kbits):
	int_obj=bw_main.getLoader().getInterfaceByName(interface_name)
	if parent_id!=None:
	    bw_main.getLoader().getNodeByID(parent_id)
	elif int_obj.getRootNode()!=None:
	    raise GeneralException(errorText("BANDWIDTH","INTERFACE_HAS_ROOT_NODE")%interface_name)

	self.__checkLimitKbits(rate_kbits)
	self.__checkLimitKbits(ceil_kbits)


    def __getNewNodeID(self):
	return db_main.getHandle().seqNextVal("bw_node_node_id_seq")

    def __addNodeDB(self,node_id,interface_id,parent_id,rate_kbits,ceil_kbits):
	db_main.getHandle().transactionQuery(self.__addNodeQuery(node_id,interface_id,parent_id,rate_kbits,ceil_kbits))

    def __addNodeQuery(self,node_id,interface_id,parent_id,rate_kbits,ceil_kbits):
	if parent_id==None:
	    parent_id="NULL"
	return ibs_db.createInsertQuery("bw_node",{ "node_id":node_id,
						    "interface_id":interface_id,
						    "parent_id":parent_id,
						    "rate_kbits":rate_kbits,
						    "ceil_kbits":ceil_kbits})
    #################################################
    def addLeaf(self,leaf_name,parent_id,default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits):
	self.__addLeafCheckInput(leaf_name,parent_id,default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits)
	node_obj=bw_main.getLoader().getNodeByID(parent_id)
	leaf_id=self.__getNewLeafID()
	self.__addLeafDB(leaf_id,leaf_name,parent_id,node_obj.getInterfaceID(),default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits)
	bw_main.getLoader().loadLeaf(leaf_id)
	bw_main.getLoader().getLeafByID(leaf_id).registerInParent()

    def __addLeafCheckInput(self,leaf_name,parent_id,default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits):
	bw_main.getLoader().getNodeByID(parent_id)
	if bw_main.getLoader().leafNameExists(leaf_name):
	    raise GeneralException(errorText("BANDWIDTH","LEAF_NAME_ALREADY_EXISTS")%leaf_name)

	if not isValidName(leaf_name):
	    raise GeneralException(errorText("BANDWIDTH","INVALID_LEAF_NAME")%leaf_name)
	
	self.__checkLimitKbits(default_rate_kbits)
	self.__checkLimitKbits(default_ceil_kbits)

	if not isInt(total_rate_kbits):
	    raise GeneralException(errorText("BANDWIDTH","INVALID_TOTAL_LIMIT_KBITS")%total_rate_kbits)

	if not isInt(total_ceil_kbits):
	    raise GeneralException(errorText("BANDWIDTH","INVALID_TOTAL_LIMIT_KBITS")%total_ceil_kbits)
	
	if total_rate_kbits*total_ceil_kbits<0:
	    raise GeneralException(errorText("BANDWIDTH","INVALID_TOTAL_LIMIT_KBITS")%"%s,%s"%(total_rate_kbits,total_ceil_kbits))
	
    def __getNewLeafID(self):
	return db_main.getHandle().seqNextVal("bw_leaf_leaf_id_seq")

    def __addLeafDB(self,leaf_id,leaf_name,parent_id,interface_id,default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits):
	db_main.getHandle().transactionQuery(
	    self.__addLeafQuery(leaf_id,leaf_name,parent_id,interface_id,default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits))

    def __addLeafQuery(self,leaf_id,leaf_name,parent_id,interface_id,default_rate_kbits,default_ceil_kbits,total_rate_kbits,total_ceil_kbits):
	return ibs_db.createInsertQuery("bw_leaf",{ "leaf_id":leaf_id,
						    "leaf_name":dbText(leaf_name),
						    "parent_id":parent_id,
						    "interface_id":interface_id,
						    "default_rate_kbits":default_rate_kbits,
						    "default_ceil_kbits":default_ceil_kbits,
						    "total_rate_kbits":total_rate_kbits,
						    "total_ceil_kbits":total_ceil_kbits})

    ########################################
    def addLeafService(self,leaf_name,protocol,_filter,rate_kbits,ceil_kbits):
	(filter_type,filter_value)=self.__parseFilter(_filter)
	self.__addLeafServiceCheckInput(leaf_name,protocol,_filter,rate_kbits,ceil_kbits,filter_type,filter_value)
	leaf_obj=bw_main.getLoader().getLeafByName(leaf_name)
	leaf_service_id=self.__getNewLeafServiceID()
	self.__addLeafServiceDB(leaf_service_id,leaf_obj.getLeafID(),protocol,filter_type,filter_value,rate_kbits,ceil_kbits)
	bw_main.getLoader().loadLeaf(leaf_obj.getLeafID())

    def __addLeafServiceCheckInput(self,leaf_name,protocol,_filter,rate_kbits,ceil_kbits,filter_type,filter_value):
	leaf_obj=bw_main.getLoader().getLeafByName(leaf_name)
	if leaf_obj.hasService((protocol,"%s %s"%(filter_type,filter_value))):
	    raise GeneralException(errorText("BANDWIDTH","LEAF_HAS_THIS_FILTER")%(leaf_name,_filter,protocol))
	if protocol not in ["tcp","udp","icmp"]:
	    raise GeneralException(errorText("BANDWIDTH","INVALID_PROTOCOL")%protocol)
	
	self.__checkFilter(_filter,filter_type,filter_value,protocol)
	self.__checkLimitKbits(rate_kbits)
	self.__checkLimitKbits(ceil_kbits)
	
    def __getNewLeafServiceID(self):
	return db_main.getHandle().seqNextVal("bw_leaf_services_leaf_service_id_seq")

    def __parseFilter(self,_filter):
	sp=re.split("\s+",_filter)
	if len(sp)!= 2:
	    raise GeneralException(errorText("BANDWIDTH","INVALID_FILTER")%_filter)
	return sp[0],",".join(MultiStr(sp[1],False))

    def __checkFilter(self,_filter,filter_type,filter_value,protocol):
	if filter_type in ["sport","dport"] and protocol in ["tcp","udp"]:
	    for port in filter_value.split(","):
		try:
		    port=int(port)
		    if port>65536 or port<0:
		        raise GeneralException(errorText("BANDWIDTH","INVALID_FILTER")%_filter)
		except ValueError:
		    raise GeneralException(errorText("BANDWIDTH","INVALID_FILTER")%_filter)
		
	elif sp[0] == "icmp-type" and protocol == "icmp":
	    pass
	else:
	    raise GeneralException(errorText("BANDWIDTH","INVALID_FILTER")%_filter)
	
    def __addLeafServiceDB(self,leaf_service_id,leaf_id,protocol,filter_type,filter_value,rate_kbits,ceil_kbits):
	_filter="%s %s"%(filter_type,filter_value)
	db_main.getHandle().transactionQuery(self.__addServiceQuery(leaf_service_id,leaf_id,protocol,_filter,rate_kbits,ceil_kbits))

    def __addServiceQuery(self,leaf_service_id,leaf_id,protocol,_filter,rate_kbits,ceil_kbits):
	return ibs_db.createInsertQuery("bw_leaf_services",{"leaf_service_id":leaf_service_id,
							    "leaf_id":leaf_id,
							    "protocol":dbText(protocol),
							    "filter":dbText(_filter),
							    "rate_kbits":rate_kbits,
							    "ceil_kbits":ceil_kbits})
    ###################################
    def delLeafService(self,leaf_name,leaf_service_id):
	"""
	    delete leaf service with id "leaf_service_id" that belongs to "leaf_name"
	"""
	self.__delLeafServiceCheckInput(leaf_name,leaf_service_id)
	leaf_obj=bw_main.getLoader().getLeafByName(leaf_name)
	self.__delLeafServiceDB(leaf_service_id)
	bw_main.getLoader().loadLeaf(leaf_obj.getLeafID())

    def __delLeafServiceCheckInput(self,leaf_name,leaf_service_id):
	leaf_obj=bw_main.getLoader().getLeafByName(leaf_name)
	if not leaf_obj.hasServiceID(leaf_service_id):
	    raise GeneralException(errorText("BANDWIDTH","LEAF_DOESNT_HAVE_SERVICE")%(leaf_name,leaf_service_id))
	
	
    def __delLeafServiceDB(self,leaf_service_id):
	db_main.getHandle().transactionQuery(self.__delLeafServiceQuery(leaf_service_id))

    def __delLeafServiceQuery(self,leaf_service_id):
	return ibs_db.createDeleteQuery("bw_leaf_services","leaf_service_id=%s"%leaf_service_id)
    ###################################
    def delNode(self,node_id,delete_root_node=False):
	self.__delNodeCheckInput(node_id,delete_root_node)
	node_obj=bw_main.getLoader().getNodeByID(node_id)
	self.__delNodeDB(node_id)
	node_obj.unregisterInParent()
	node_obj.delFromTC()
	bw_main.getLoader().unloadNode(node_id)
	
    def __delNodeCheckInput(self,node_id,delete_root_node):
	node_obj=bw_main.getLoader().getNodeByID(node_id)
	self.__checkNodeChildren(node_obj)
	if not delete_root_node and node_obj.getParentID()==None:
	    raise GeneralException(errorText("BANDWIDTH","CANT_DELETE_ROOT_NODE"))
    
    def __checkNodeChildren(self,node_obj):
	"""
	    check if node has children and raise an exception if has so
	"""
	if len(node_obj.getChildren()) or len(node_obj.getLeafChildren()):
	    raise GeneralException(errorText("BANDWIDTH","NODE_HAS_CHILDREN"))

    def __delNodeDB(self,node_id):
	db_main.getHandle().transactionQuery(self.__delNodeQuery(node_id))

    def __delNodeQuery(self,node_id):
	return ibs_db.createDeleteQuery("bw_node","node_id=%s"%node_id)
    ##################################
    def delLeaf(self,leaf_name):
	self.__delLeafCheckInput(leaf_name)
	leaf_obj=bw_main.getLoader().getLeafByName(leaf_name)
	self.__delLeafDB(leaf_obj.getLeafID())
	leaf_obj.unregisterInParent()
	bw_main.getLoader().unloadLeaf(leaf_obj.getLeafID())
	
    def __delLeafCheckInput(self,leaf_name):
	leaf_obj=bw_main.getLoader().getLeafByName(leaf_name)
	if len(leaf_obj.getServices())!=0:
	    raise GeneralException(errorText("BANDWIDTH","LEAF_HAS_SERVICES"))
	self.__leafUsedInCharge(leaf_obj.getLeafID())

    def __leafUsedInCharge(self,leaf_id):
	def checkLeafInChargeObj(charge_obj):
	    for rule_obj in charge_obj.getRules().itervalues():
		if rule_obj.bw_tx_leaf_id==leaf_id or rule_obj.bw_rx_leaf_id==leaf_id:
		    raise GeneralException(errorText("BANDWIDTH","LEAF_USED_IN_CHARGE")%charge_obj.getChargeName())


	charge_main.getLoader().runOnAllCharges(checkLeafInChargeObj)	

    def __delLeafDB(self,leaf_id):
	db_main.getHandle().transactionQuery(self.__delLeafQuery(leaf_id))
    
    def __delLeafQuery(self,leaf_id):
	return ibs_db.createDeleteQuery("bw_leaf","leaf_id=%s"%leaf_id)	
    
    ##################################
    def delInterface(self,interface_name):
	self.__delInterfaceCheckInput(interface_name)
	int_obj=bw_main.getLoader().getInterfaceByName(interface_name)
	self.__delInterfaceDB(int_obj)
	bw_main.getLoader().unloadInterface(int_obj.getInterfaceID())

    def __delInterfaceCheckInput(self,interface_name):
	int_obj=bw_main.getLoader().getInterfaceByName(interface_name)
	self.__checkNodeChildren(int_obj.getRootNode())

    def __delInterfaceDB(self,int_obj):
	query=self.__delNodeQuery(int_obj.getRootNodeID())
	query+=self.__delInterfaceQuery(int_obj.getInterfaceID())
	db_main.getHandle().transactionQuery(query)

    def __delInterfaceQuery(self,int_id):
	return ibs_db.createDeleteQuery("bw_interface","interface_id=%s"%int_id)
    ####################################
    def updateInterface(self,interface_id,interface_name,comment):	
	self.__updateInterfaceCheckInput(interface_id,interface_name,comment)
	int_obj=bw_main.getLoader().getInterfaceByID(interface_id)
	self.__updateInterfaceDB(interface_id,interface_name,comment)
	if interface_name!=int_obj.getInterfaceName():
    	    bw_main.getLoader().unloadInterface(interface_id)
	    bw_main.getLoader().loadInterface(interface_id)
	    int_obj=bw_main.getLoader().getInterfaceByID(interface_id)
	    self.__reRegisterRootNode(interface_id)
	    int_obj.createTree()
	else:
	    int_obj.changeComment(comment)

    def __reRegisterRootNode(self,interface_id):
	for node_id in bw_main.getLoader().getAllNodeIDs():
	    node_obj=bw_main.getLoader().getNodeByID(node_id)
	    if node_obj.getInterfaceID()==interface_id and node_obj.getParentID()==None:
		node_obj.registerInParent()
		return

    def __updateInterfaceCheckInput(self,interface_id,interface_name,comment):
	int_obj=bw_main.getLoader().getInterfaceByID(interface_id)
	if int_obj.getInterfaceName()!=interface_name:
	    self.__addInterfaceCheckInput(interface_name,comment)
	
    def __updateInterfaceDB(self,interface_id,interface_name,comment):
	db_main.getHandle().transactionQuery(
				self.__updateInterfaceQuery(interface_id,interface_name,comment))

    def __updateInterfaceQuery(self,interface_id,interface_name,comment):
	return ibs_db.createUpdateQuery("bw_interface",{"interface_name":dbText(interface_name),
					 "comment":dbText(comment)},"interface_id=%s"%interface_id)
	    
    ######################################
    def updateNode(self,node_id,rate_kbits,ceil_kbits):
	self.__updateNodeCheckInput(node_id,rate_kbits,ceil_kbits)
	self.__updateNodeDB(node_id,rate_kbits,ceil_kbits)
	node_obj=bw_main.getLoader().getNodeByID(node_id)
	node_obj.update(rate_kbits,ceil_kbits)
    
    def __updateNodeCheckInput(self,node_id,rate_kbits,ceil_kbits):
	bw_main.getLoader().getNodeByID(node_id)

	self.__checkLimitKbits(rate_kbits)
	self.__checkLimitKbits(ceil_kbits)

    def __updateNodeDB(self,node_id,rate_kbits,ceil_kbits):
	db_main.getHandle().transactionQuery(self.__updateNodeQuery(node_id,rate_kbits,ceil_kbits))

    def __updateNodeQuery(self,node_id,rate_kbits,ceil_kbits):
	return ibs_db.createUpdateQuery("bw_node",{"rate_kbits":rate_kbits,
						   "ceil_kbits":ceil_kbits},"node_id=%s"%node_id)
						   