class AttributeHandler:
    
    def __init__(self,info_holder_name):
	"""
	    info_holder_name: name string representation of info holder we generate
	"""
	self.info_holder_name=info_holder_name

    def registerInfoHandlerClass(self,info_handler_class,attr_list):
	"""
	    register "info_handler_class" 
	    info_handler_class initializer will be called with values of "attr_list" as arguments
	    if you use this method --DONT-- override method getInfoHolder
	"""
	self.info_handler_class=info_handler_class
	self.info_handler_arg_attrs=attr_list

    def getInfoHolderName(self):
	return self.info_holder_name

    def getInfoHolder(self,attr_name,attrs):
	"""
	    attr_name(string): attribute name we encountered and we want info handler for this attribute
			       and all other relevant attributes
	    attrs(dic): dic of attributes
	"""
        arg_list=map(lambda x:attrs[x],self.info_handler_arg_attrs)
	return apply(self.info_handler_class,arg_list)
	
    
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
	
