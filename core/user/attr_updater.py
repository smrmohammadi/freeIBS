from core.db import ibs_db,ibs_query
from core.lib.general import *
from core.group import group_main

class AttrUpdaterContainer:
    def __init__(self):
	self.attr_updaters={}

    def __iter__(self):
	return self.attr_updaters.itervalues()

    def addNew(self,attr_updater_obj):
	"""
	    add new attr updater to container
	"""
	self.attr_updaters[attr_updater_obj.getName()]=attr_updater_obj

    def hasName(self,attr_updater_name):
	return self.attr_updaters.has_key(attr_updater_name)
    
    def mustHave(self,*attr_updater_names):
	for name in attr_updater_names:
	    if not self.hasName(name):
		raise GeneralException(errorText("USERS","INCOMPLETE_attr_updater_SET"%name))

    def getQuery(self,ibs_query,src,action,dic_args):
	"""
	    return an ibs_query instance for doing "action" on "src" with args "dic_args"
	    ibs_query(IBSQuery instance): ibs query instance that we add query to
	    src(str): "group" or "user"
	    action(str): "change" or "delete"
	    
	"""
	self.callOnAll("getQuery",[ibs_query,src,action],dic_args)
	return ibs_query

    def callOnAll(self,method_name,args,dargs):
	"""
	    call "method_name" of all attr_updaters, with argument "args" and "dargs"
	    args are list arguments and dargs are dic arguments
	"""
	ret=[]
	for attr_updater_name in self.attr_updaters:
	    attr_updater_obj=self.attr_updaters[attr_updater_name]
	    ret.append(apply(getattr(attr_updater_obj,method_name),args,dargs))
	return ret
		
class AttrUpdater:
    def __init__(self,name):
	"""
	    name(str): attribute handler name, this should be unique between attribute handlers, and should be same
	    as the name relevant attribute handler return
	"""
	self.name=name
	self.query_funcs={}
	self.query_attrs={}


    def changeInit(self,*args):
	"""
	    should be overide by child classes
	    called with attributes as arguments changeInit(self,attr1,attr2,...).. when we want to change
	    arguments
	"""
	pass

    def deleteInit(self):
	"""
	    should be overide by child classes
	    called when we want to delete attributes
	"""
	pass

    def getName(self):
	return self.name

    def checkInput(self,src,action,arg_dic):
	"""
	    this method must check attr updater properties, and check their validity
	    "action" is one of self.actions that show what action is getting done
	    arg_dic are extra arguments, that maybe necessary for checkings.
	    arg_dic contents differs on diffrent actions
	    IMPORTANT WARNING: early checkings should be done in class initializer
			       this method will be called after we reserved our user IDs
			       so raising an exception here means that reserved IDs would be lost
	"""
	pass


    def getQuery(self,ibs_query,src,action,**args):
	"""
	    return query for insert/update/delete our attributes
	    preferrably this method should return an IBSQuery instance
	    this is important when query can be large
	    this method maybe overidded to customize the behaviour
    
	    src(string): "group" or "user"
	    action(string):"change" or "delete"
	    args(dic): extra arguments, for group src, group_obj and for user src "users" objs are passed with requester admin_obj s
	    users list and admin_obj would be there always
	"""
	self.checkInput(src,action,args)
	if self.query_funcs.has_key(src+"_"+action):
	    return self.__callQueryFunc(ibs_query,src,action,args)
	else:
	    return ""


    def __callQueryFunc(self,ibs_query,src,action,args):
	args["attr_updater_attrs"]=self.query_attrs[src+"_"+action]
        return apply(self.query_funcs[src+"_"+action],[ibs_query,src,action],args)

    def registerQuery(self,src,action,query_function,attrs): 
	"""
	    register query_function for action

	    query_function must accept **args and use this dictionary for it's arguments
	    string query_function(IBSQuery ibs_query,string src,string action,dic **args)

	    attrs(dic or list): update actions: this dictionary is passed to query_function as "attr_updater_attrs" in dict arguments (**args)
				delete actions: the list is a list of attrs that should be deleted
		
	"""
	self.query_funcs[src+"_"+action]=query_function
	self.query_attrs[src+"_"+action]=attrs

    def useGenerateQuery(self,attrs):
	"""
	    set all query_functions to self.generateQuery
	"""
	self.registerQuery("user","change",self.generateQuery,attrs)
	self.registerQuery("user","delete",self.generateQuery,attrs)
	self.registerQuery("group","change",self.generateQuery,attrs)
	self.registerQuery("group","delete",self.generateQuery,attrs)


    def generateQuery(self,ibs_query,src,action,**args):
	"""
	    this method is a generic query generator for common attribute handlings
	    this can be registered via registerQuery or useGenerateQuery, and do the delete/update/insert automatically
	    or call by another proxy function
	"""
	if action=="delete":
	    if src=="user":
		return self.__deleteUserAttr(ibs_query,args["attr_updater_attrs"],args["users"])
	    elif src=="group":
		return self.__deleteGroupAttr(ibs_query,args["attr_updater_attrs"],args["group_obj"])
	elif action=="change":
	    if src=="user":
		return self.__changeUserAttr(ibs_query,args["attr_updater_attrs"],args["users"])
	    elif src=="group":
		return self.__changeGroupAttr(ibs_query,args["attr_updater_attrs"],args["group_obj"])

    def __changeGroupAttr(self,ibs_query,attrs,group_obj):
	for attr_name in attrs:
	    if group_obj.hasAttr(attr_name):
		ibs_query+=group_main.getActionManager().updateGroupAttrQuery(group_obj.getGroupID(),attr_name,attrs[attr_name])
	    else:
		ibs_query+=group_main.getActionManager().insertGroupAttrQuery(group_obj.getGroupID(),attr_name,attrs[attr_name])
	return ibs_query

    def __deleteGroupAttr(self,ibs_query,attrs,group_obj):
	for attr_name in attrs:
		ibs_query+=group_main.getActionManager().deleteGroupAttrQuery(group_obj.getGroupID(),attr_name)
    	return ibs_query

    def __changeUserAttr(self,ibs_query,attrs,users):
	for user in users:
	    for attr_name in attrs:
		if user.hasAttr(attr_name):
		    ibs_query+=user_main.getActionManager().updateUserAttrQuery(user.getUserID(),attr_name,attr_value)
		else:
		    ibs_query+=user_main.getActionManager().insertUserAttrQuery(user.getUserID(),attr_name,attr_value)
	return ibs_query

    def __deleteUserAttr(self,ibs_query,attrs,users):
	for user in users:
	    for attr_name in attrs:
		    ibs_query+=user_main.getActionManager().deleteUserAttrQuery(user.getUserID(),attr_name)
	return ibs_query
	

	