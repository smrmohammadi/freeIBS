class AttributeHandler:
    def __init__(self,attr_updater_name):
	"""
	    attr_handler_name: name string representation of info holder we generate
	"""
	self.attr_handler_name=attr_updater_name

    def getName(self):
	return self.attr_handler_name

    ###############################################
    def registerAttrUpdaterClass(self,attr_updater_class,change_attr_list):
	"""
	    register "attr_updater_class" 
	    attr_updater_class changeInit method will be called with values of "change_attr_list" as arguments
	    if you use this method --DONT-- override method getattrUpdater
	"""
	self.attr_updater_class=attr_updater_class
	self.attr_updater_change_arg_attrs=change_attr_list

    def getAttrUpdater(self,attr_name,attrs,action):
	"""
	    attr_name(string): attribute name we encountered and we want attr updater for this attribute
			       and all other relevant attributes
	    attrs(dic or list): dic of attributes for "change" action, and list of attribute for "delete"
	    action(string): should be "change" or "delete". 
	"""
	
	attr_updater=self.attr_updater_class()
	if action=="change":
	    arg_list=map(lambda x:attrs[x],self.attr_updater_change_arg_attrs)
	    apply(attr_updater.changeInit,arg_list)
	else:
	    attr_updater.deleteInit()
	return attr_updater

    #########################################################
    def registerAttrHolderClass(self,attr_holder_class,holder_attrs):
	"""
	    register a attr holder for this handler
	    attr_holder_class(Class): the class to be registered
	    holder_attrs(list): list of attributes that will be passed to initializer of attr_holder
	"""
	self.attr_holder_class=attr_holder_class
	self.attr_holder_attrs=holder_attrs

    def getAttrHolder(self,attr_name,attrs):
	"""
	    attr_name(string): attribute name we encountered and we want attr holder for this attribute
			       and all other relevant attributes
	    attrs(dic or list): dic of attributes 
	"""
	arg_list=map(lambda x:attrs[x],self.attr_holder_attrs)
	return apply(self.attr_holder_class,arg_list)

class UserAttributes:
    def __init__(self,attributes,group_id):
	"""
	    attributes(dic): set of user attributes in format {attr_name:attr_value}
	    group_id(int): Group ID, that will be asked, if we don't have an attribute
	"""
	self.attributes=attributes
	self.group_id=group_id
    
    def __getGroupObj(self):
	"""
	    maybe group attributes changed during 
	"""
	return group_main.getLoader().getGroupByID(self.group_id)
    
    def getAttribute(self,attr_name):
	if self.hasAttribute(attr_name):
	    return self.attributes[attr_name]
	
	return self.__getGroupObj().getAttribute(attr_name) 

    def hasAttribute(self,attr_name):
	return self.attributes.has_key(attr_name)
	
    def getAllAttributes(self):
	return self.attributes
