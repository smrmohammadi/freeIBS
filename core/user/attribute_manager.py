from core.ibs_exceptions import *
from core.errors import errorText
from core.user.info_holder import InfoHolderContainer

class AttributeManager:
    def __init__(self):
	self.attr_handlers={}

    def registerHandler(self,handler_obj,attr_list):
	"""
	    handler_obj(AttributeHandler instance): Attribute Handler that generate an info holder
	    attr_list(list of strs): list of attributes
	    register a attr_handler, that will be called when we encounter an attribute in attr_list
	"""
	for attr in attr_list:
	    if self.attr_handlers.has_key(attr):
		raise IBSException(errorText("USER","DUPLICATE_ATTR_REGISTRATION")%attr)
	    self.attr_handlers[attr]=handler_obj

    def __getAttrHandler(self,attr_name):
	try:
	    return self.attr_handlers[attr_name]
	except KeyError:
	    raise GeneralException(errorText("USER","UNREGISTERED_ATTRIBUTE")%attr_name)
	
    def getInfoHolders(self,attrs_dic):
	"""
	    attrs_list(dic): dic of all attributes in format name:value
	    return a list of info handlers or raise an exception on error
	"""
	info_holders=InfoHolderContainer()
        for attr_name in attrs_dic:
	    handler=self.__getAttrHandler(attr_name)
	    if not info_holders.hasName(handler.getInfoHolderName()):
	        info_holders.addNew(handler.getInfoHolder(attr_name,attrs_dic))

	return info_holders
    
