import copy

from core.ibs_exceptions import *
from core.errors import errorText
from core.user.attr_updater import AttrUpdaterContainer

class AttributeManager:
    def __init__(self):
	self.change_attr_handlers={}
	self.delete_attr_handlers={}
	self.parse_attr_handlers={}

    def registerHandler(self,handler_obj,change_attr_list,delete_attr_list,parse_attr_list):
	"""
	    handler_obj(AttributeHandler instance): Attribute Handler that generate an attr_updater and attr_holder
	    change_attr_list(list of strs): list of attributes for change action
	    delete_attr_list(list of strs): list of attributes for delete action
	    parse_attr_list(list of strs): list of attributes that this attr handle can parse
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

	for attr in parse_attr_list:
	    if self.parse_attr_handlers.has_key(attr):
		raise IBSException(errorText("USER","DUPLICATE_ATTR_REGISTRATION")%attr)
	    self.parse_attr_handlers[attr]=handler_obj

#########################################
    def __getAttrHandlerForUpdater(self,attr_name,action):
	try:
	    if action=="change":
		return self.change_attr_handlers[attr_name]
	    elif action=="delete":
		return self.delete_attr_handlers[attr_name]
	except KeyError:
	    raise GeneralException(errorText("USER","UNREGISTERED_ATTRIBUTE")%attr_name)
	
    def getAttrUpdaters(self,attrs,action):
	"""
	    attrs(dic or list): dic of all attributes in format name:value
	    action(string): should be "change" ro "delete"
	    return an AttrUpdaterContainer instance containing attrs attrUpdaters
	"""
	attr_updaters=AttrUpdaterContainer()
        for attr_name in attrs:
	    handler=self.__getAttrHandlerForUpdater(attr_name,action)
	    if not attr_updaters.hasName(handler.getName()):
	        attr_updaters.addNew(handler.getAttrUpdater(attr_name,attrs,action))
	return attr_updaters

##########################################
    def __getAttrHandlerForHolder(self,attr_name):
	try:
	    return self.parse_attr_handlers[attr_name]
	except KeyError:
	    return None

    def getAttrHolders(self,attrs):
	"""
	    attrs(dic or list): dic of all attributes in format name:value
	    return a dic of attr holders for attrs in format {attr handler name:AttrHandler instance}
	"""
	attr_holders={}
	for attr_name in attrs:
	    handler=self.__getAttrHandlerForHolder(attr_name)
	    if handler!=None:
		attr_holders[handler.getName()]=handler.getAttrHolder(attr_name,attrs)
	return attr_holders

    def parseAttrs(self,attrs,date_type):
	"""
	    return a dic of attrs containing the parsed attributes of attrs
	"""
	attrs=copy.copy(attrs) #make sure we don't change user/group attributes
    	attr_holders=self.getAttrHolders(attrs).values()
	map(lambda x:x.setDateType(date_type),attr_holders)
	map(lambda x:attrs.update(x.getParsedDic()),attr_holders)
	return attrs
