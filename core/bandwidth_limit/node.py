from core.bandwidth_limit import bw_main

class Node:
    def __init__(self,node_id,parent_id,interface_id,bw_limit):
	"""
	    parent_id(int): id of parent, None if this is the root node
	    interface_id(int): id of interface, this belongs to
	    bw_limit(int): bandwidth limit in kbits/s
	"""
	self.interface_id=interface_id
	self.node_id=node_id
	self.parent_id=parent_id
	self.bw_limit=bw_limit
	self.children=[]#child nodes
	self.leaves=[]#child leaves
	self.tc_id=None


    def getNodeID(self):
	return self.node_id

    def getBwLimit(self):
	return self.bw_limit

    def getChildren(self):
	return self.children

    def getLeafChildren(self):
	return self.leaves
#################################
    def registerChild(self,child_node_id):
	self.children.append(child_node_id)
    
    def unregisterChild(self,child_node_id):
	self.children.remove(child_node_id)
#################################
    def registerLeaf(self,child_leaf_id):
	self.leaves.append(child_leaf_id)
    
    def unregisterLeaf(self,child_leaf_id):
	self.leaves.remove(child_leaf_id)
#################################
    def registerInParent(self):
	if self.parent_id!=None:
	    bw_main.getLoader().getNodeByID(self.parent_id).registerChild(self.getNodeID())
	else:
	    bw_main.getLoader().getInterfaceByID(self.interface_id).registerRootNode(self.getNodeID())
    
    def unregisterInParent(self):
	if self.parent_id!=None:
	    bw_main.getLoader().getNodeByID(self.parent_id).unregisterChild(self.getNodeID())
	else:
	    bw_main.getLoader().getInterfaceByID(self.interface_id).unregisterRootNode(self.getNodeID())
##################################
    def getParentID(self):
	return self.parent_id

    def getParent(self):
	return bw_main.getLoader().getNodeByID(self.getParentID())
#################################
    def getInterfaceID(self):
	return self.interface_id

    def getInterface(self):
	return bw_main.getLoader().getInterfaceByID(self.getInterfaceID())

    def getInterfaceName(self):
	return self.getInterface().getInterfaceName()
##################################
    def __getParentTC_ID(self):
	if self.getParentID()==None:
	    parent=0
	else:
	    parent=self.getParent().getTC_ID()
	return parent

    def addToTC(self):
	self.__assignTC_ID()
	bw_main.getTCRunner().addClass(self.getInterfaceName(),"parent 0:%s"%self.__getParentTC_ID(),"classid 0:%s"%self.getTC_ID(),"htb","rate %skbit"%self.getBwLimit())
#############################################
    def delFromTC(self):
	#self.__freeTC_ID() buggy tc doesn't delete node, so let's not release the id
	bw_main.getTCRunner().delClass(self.getInterfaceName(),"parent 0:%s"%self.__getParentTC_ID(),"classid 0:%s"%self.getTC_ID())

#############################################
    def getTC_ID(self):
	return self.tc_id    

    def __assignTC_ID(self):
	self.tc_id=self.getInterface().getMinorIDPool().getID(1)[0]

    def __freeTC_ID(self):
	self.getInterface().getMinorIDPool().freeID(self.getTC_ID())

    def createSubTree(self):
	self.addToTC()
	map(lambda node:bw_main.getLoader().getNodeByID(node).createSubTree(),self.getChildren())

###################################
    def getInfo(self):
	parent_id=self.getParentID()
	if parent_id==None: parent_id="root"
	return {"interface_id":self.getInterfaceID(),
		"interface_name":self.getInterfaceName(),
		"node_id":self.getNodeID(),
		"parent_id":parent_id,
		"limit_kbits":self.getBwLimit()}
		