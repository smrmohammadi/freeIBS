class AttributeHandler:
    
    def __init__(self,info_holder_name):
	"""
	    info_holder_name: name string representation of info holder we generate
	"""
	self.info_holder_name=info_holder_name

    def registerInfoHandlerClass(self,info_handler_class,change_attr_list):
	"""
	    register "info_handler_class" 
	    info_handler_class changeInit method will be called with values of "change_attr_list" as arguments
	    if you use this method --DONT-- override method getInfoHolder
	"""
	self.info_handler_class=info_handler_class
	self.info_handler_change_arg_attrs=change_attr_list

    def getInfoHolderName(self):
	return self.info_holder_name

    def getInfoHolder(self,attr_name,attrs,action):
	"""
	    attr_name(string): attribute name we encountered and we want info handler for this attribute
			       and all other relevant attributes
	    attrs(dic or list): dic of attributes for "change" action, and list of attribute for "delete"
	    action(string): should be "change" ro "delete"
	"""
	
	info_holder=self.info_handler_class()
	if action=="change":
	    arg_list=map(lambda x:attrs[x],self.info_handler_change_arg_attrs)
	    apply(info_holder.changeInit,arg_list)
	else:
	    info_holder.deleteInit()
	return info_holder
    
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
