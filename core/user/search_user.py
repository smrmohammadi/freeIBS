from core.lib.general import *

class SearchUserHelper:
    def __init__(self,cond_dic):
	self.__tables=[]
	self.__root_group=SearchUserGroup()
	self.cond_dic=cond_dic

    def addTable(self,table_name):
	if table_name not in self.__tables:
	    self.__tables.append(table_name)

    def getRootGroup(self):
	return self.__root_group

    def getConditionsDic(self):
	return self.cond_dic
    
    def hasConditionFor(self,key):
	return self.cond_dic.has_key(key)

    def getConditionValue(self,key):
	return self.cond_dic[key]

    def getDBConditionValue(self,key):
	return dbText(self.getConditionValue(key))
	
class SearchUserGroup:
    def __init__(self):
	self.__groups=[]
	self.__operator=""

    def setOperator(self,operator):
	"""
	    set operator between each member of this group. Normally it should be "or" or "and"
	"""
	self.__operator=operator
    
    def addGroup(self,group):
	"""
	    add a new group to be member of this group
	    group can be an string or another group object.
	    group objects would be queried to reach a group without another group_obj builtin
	"""
	self.__groups.append(group)

    def getConditionalClause(self):
	"""
	    build an conditional clause based on member groups
	"""
	if len(self.__groups)==0:
	    return ""
	str_groups=map(self.__getConditionStr,self.__groups)
	return " (%s) "%(" %s "%self.__operator).join(str_groups)
    
    def __getConditionStr(self,group_obj):
	if isinstance(group_obj,SearchUserGroup):
	    return group_obj.getConditionalClause()
	else:
	    return group_obj
