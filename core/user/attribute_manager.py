from core.ibs_exceptions import *
from core.errors import errorText
from core.user.info_holder import InfoHolderContainer

class AttributeManager:
    def __init__(self):
	self.change_attr_handlers={}
	self.delete_attr_handlers={}

    def registerHandler(self,handler_obj,change_attr_list,delete_attr_list):
	"""
	    handler_obj(AttributeHandler instance): Attribute Handler that generate an info holder
	    change_attr_list(list of strs): list of attributes for change action
	    delete_attr_list(list of strs): list of attributes for delete action
	    register a attr_handler, that will be called when we encounter an attribute in attr_list
	"""
	for attr in change_attr_list:
	    if self.change_attr_handlers.has_key(attr):
		raise IBSException(errorText("USER","DUPLICATE_ATTR_REGISTRATION")%attr)
	    self.change_attr_handlers[attr]=handler_obj

	for attr in delete_attr_list:
	    if self.delete_attr_handlers.has_key(attr):
		raise IBSException(errorText("USER","DUPLICATE_ATTR_REGISTRATION")%attr)
	    self.delete_attr_handlers[attr]=handler_obj

    def __getAttrHandler(self,attr_name,action):
	try:
	    if action=="change":
		return self.change_attr_handlers[attr_name]
	    elif action=="delete":
		return self.delete_attr_handlers[attr_name]
	except KeyError:
	    raise GeneralException(errorText("USER","UNREGISTERED_ATTRIBUTE")%attr_name)
	
    def getInfoHolders(self,attrs,action):
	"""
	    attrs(dic or list): dic of all attributes in format name:value
	    action(string): should be "change" ro "delete"
	    return a list of info handlers or raise an exception on error
	"""
	info_holders=InfoHolderContainer()
        for attr_name in attrs:
	    handler=self.__getAttrHandler(attr_name,action)
	    if not info_holders.hasName(handler.getInfoHolderName()):
	        info_holders.addNew(handler.getInfoHolder(attr_name,attrs,action))

	return info_holders
    
