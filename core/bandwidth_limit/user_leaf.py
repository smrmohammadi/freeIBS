class UserLeaf:
    def __init__(self,leaf_obj,ip_addr,direction):
	"""
	    leaf_obj(Leaf instance):
	    ip_addr(str): ip address of user
	    direction(str): can be one of "send" or "receive"
	"""
	self.leaf_obj=leaf_obj
	self.ip_addr=ip_addr
	self.direction=direction

	self.major_tc_id=None
	self.service_marks=None
	self.default_mark=None

	self.last_minor_tc_id=1


    def getLeafObj(self):
	return self.leaf_obj

    ##############################
    def __getNewMinorTC_ID(self):
	self.last_minor_tc_id+=1
	return self.last_minor_tc_id
	
    ###############################
    def addToTC(self):
	self.__setMajorTC_ID()
	self.__addQdisc()
	self.__addClassesAndFilters()

    def __setMajorTC_ID(self):
	self.major_tc_id=self.getLeafObj().Interface().getMajorIDPool().getID(1)

    def __addQdisc(self):
	bw_main.getTCRunner().addQdisc(self.getLeafObj().getInterfaceName(),
				       "parent 0:%s"%self.getLeafObj().getParentNode(),
				       "handle %s:"%self.major_tc_id,
				       "htb")

    
    def __addClassesAndFilters(self):
	all_parent_id=self.__addTotalClass()
	services=self.getLeafObj().getServices()
	self.__setMarks(services)
	map(self.__addService,
	    services,
	    self.service_marks,
	    itertools.repeat(all_parent_id,len(services)))
	self.__addDefaultClassAndFilter(self.default_mark,all_parent_id)
	
    def __setMarks(self,services):
	marks=bw_main.getMarkIDPool().getID(len(services)+1)
	self.default_mark=marks[0]
	self.service_marks=marks[1:]
	
	
    def __addService(self,leaf_service,mark_id,parent_id):
    	"""
	    add service limit in "leaf_service"
	    mark_id(int): mark number to user with iptables
	    parent_id(int): parent minor id of class
	"""
	minor_id=self.__getNewMinorTC_ID()
	bw_main.getTCRunner().addClass(self.getLeafObj().getInterfaceName(),
				       "parent %s:%s"%(self.major_tc_id,parent_id),
				       "classid %s:%s"%(self.major_tc_id,minor_id),
				       "htb",
				       "rate %s"%leaf_service.getBwLimit())
	bw_main.getIptablesRunner().addMark(mark_id,self.ip_addr,self.direction,leaf_service)
	bw_main.getTCRunner().addFilter(self.getLeafObj().getInterfaceName(),
					"protocol ip",
					"prio 1",
					"handle %s fw"%mark_id,
					"flowid %s:%s"%(self.major_tc_id,minor_id))
	

    def __addDefaultClassAndFilter(self,mark_id,parent_id):
	"""
	    add default service limit class
	    mark_id(int): mark number to user with iptables
	    parent_id(int): parent minor id of default class
	"""
	minor_id=self.__getNewMinorTC_ID()
	bw_main.getTCRunner().addClass(self.getLeafObj().getInterfaceName(),
				       "parent %s:%s"%(self.major_tc_id,parent_id),
				       "classid %s:%s"%(self.major_tc_id,minor_id),
				       "htb",
				       "rate %s"%self.getLeafObj().getDefaultBwLimit())
	bw_main.getIptablesRunner().addMark(mark_id,self.ip_addr,self.direction,None)
	bw_main.getTCRunner().addFilter(self.getLeafObj().getInterfaceName(),
					"protocol ip",
					"prio 1",
					"handle %s fw"%mark_id,
					"flowid %s:%s"%(self.major_tc_id,minor_id))
    
    def __addTotalClass(self):
	"""
	    add Total Limit class
	"""
	if self.getLeafObj().getTotalBwLimit()>=0:
	    bw_main.getTCRunner().addClass(self.getLeafObj().getInterfaceName(),
				           "parent %s:0"%self.major_tc_id,
					   "classid %s:1"%self.major_tc_id,
					   "htb",
					   "rate %s"%self.getLeafObj().getTotalBwLimit())
	    all_parent_id=1
	else:
	    all_parent_id=0
	    
	return all_parent_id
    ##############################
    def delFromTC(self):
	"""
	    delete this leaf from tc
	"""	
	self.__delQdisc()
	self.__delMarks()
	
    def __delQdisc(self):
	bw_main.getTCRunner().delQdisc(self.getLeafObj().getInterfaceName(),
				       "parent 0:%s"%self.getLeafObj().getParentNode(),
				       "handle %s:"%self.major_tc_id,
				       "htb")
	self.getLeafObj().Interface().getMajorIDPool().freeID(self.major_tc_id)
	
    def __delMarks(self):
	map(self.__delMark,self.service_marks,self.getLeafObj().getServices())
	self.__delMark(self.default_mark,None)
	bw_main.getMarkIDPool().freeID(self.services_mark+[self.default_mark])

    def __delMark(self,mark_id,leaf_service):
	bw_main.getIptablesRunner().delMark(mark_id,self.ip_addr,self.direction,leaf_service)
