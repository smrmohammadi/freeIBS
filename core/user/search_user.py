from core.lib.general import *

class Condition:
    def __init__(self,cond_dic):
	self.cond_dic=self.__fix(cond_dic)

    def __getitem__(self,key):
	return self.cond_dic[key]

    def has_key(self,key):
	return self.cond_dic.has_key(key)

class SearchTable:
    def __init__(self):
	self.__root_group=SearchUserGroup("and")
    
    def addGroup(self,group):
	return self.__root_group.addGroup(group)
    
    def addGroups(self,groups):
	return map(self.addGroup,groups)


############################# some helpers
    def getParsedValue(self,search_helper,dic_key,value_parser_method):
	value=search_helper.getCondValue(dic_key)
	if type(value)==types.StringType:
	    value=(value,)
	if value_parser_method!=None:
	    value=map(lambda val:apply(value_parser_method,val),value)


class SearchUsersTable(SearchTable):
    def __init__(self):
	SerachTable.__init__(self)

    def exactSearch(self,search_helper,cond_key,db_col_name,value_parser_method=None):
	"""
	    do the exact search for one attribute.
	    cond_key(str): key of attribute in conditions that passed us from interface
	    db_col_name(str): name of attribute in database 
	    value_parser_method(callable): call this method on value and use the returned value in query
					   not that the returned value will go through dbText
	"""
	if search_helper.hasCondFor(dic_key):
	    values=self.getParsedValue(search_helper,dic_key,value_parser_method)
	    group=SearchUserGroup("or")
	    groups=map(lambda value:group.addGroup("%s = %s"%(db_col_name,dbtext(value))),values)
	    self.addGroups(groups)

class SearchNormalUsersTable(SearchTable):
    def __init__(self):
	SerachTable.__init__(self)

class SearchVoIPUsersTable(SearchTable):
    def __init__(self):
	SerachTable.__init__(self)



class SearchAttrsTable(SearchTable):
    def __init__(self):
	SerachTable.__init__(self)
    
    def exactSearch(self,search_helper,dic_key,attr_db_name,value_parser_method=None):
	"""
	    do the exact search for one attribute.
	    dic_key(str): key of attribute in conditions that passed us from interface
	    attr_db_name(str): name of attribute in database attr_name field
	    value_parser_method(callable): call this method on value and use the returned value in query
					   not that the returned value will go through dbText
	"""
	if search_helper.hasCondFor(dic_key):
	    self.searchOnConds(search_helper,dic_key,attr_db_name,value_parser_method,"=")

    def ltgtSearch(self,cond_key,cond_op_key.attr_db_name,value_parser_method=None):
	"""
	"""
	if search_helper.hasCondFor(cond_key,cond_op_key):
	    checkltgtOperator(search_helper.getCondValue(cond_op_key))
	    self.searchOnConds(serach_helper,
			cond_key,
			attr_db_name,
			value_parser_method,
			search_helper.getCondValue(cond_op_key)
		       )
	    

    def searchOnConds(self,search_helper,dic_key,attr_db_name,value_parser_method,op):
	values=self.getParsedValue(search_helper,dic_key,value_parser_method)
	self.serach(attr_db_name,values,op)


    def createAttrGroup(self,attr_name,attr_value,op):
	"""
	"""
	group=SearchUserGroup("and")
	group.addGroup("attr_name = %s"%dbtext(attr_name))
	group.addGroup("attr_value %s %s"%(op,dbText(value)))
	return group

class SearchUserAttrsTable(SearchAttrsTable):
    def __init__(self):
	SerachAttrsTable.__init__(self)

    def search(self,attr_db_name,values,op):
	"""
	"""
	group=SearchUserGroup("or")
	groups=map(lambda value:group.addGroup(self.attrEqualsGroup(attr_db_name,value,op)),values)
	self.addGroups(groups)

class SearchGroupAttrsTable(SearchAttrsTable):
    def __init__(self):
	SerachAttrsTable.__init__(self)
	self.attrs=[]

    def addAttr(self,attr):
	self.attrs.append(attr)

    def search(self,attr_db_name,values,op):
	"""
	"""
	self.addAttr(attr_db_name)
	group=SearchUserGroup("or")
	groups=map(lambda value:group.addGroup(self.attrEqualsGroup(attr_db_name,value,op)),values)
	self.addGroups(groups)


class SearchUserHelper:
    def __init__(self,conds):
	self.conds=conds
	self.tables={"users":SearchUsersTable(),
		     "user_attrs":SearchUserAttrsTable(),
		     "normal_users":SearchNormalUsersTable(),
		     "voip_users":SearchVoIPUsersTable(),
		     "group_attrs":SearchGroupAttrsTable()
		    }

    def getConds(self):
	return self.cond_dic
    
    def hasCondFor(self,*keys):
	for key in keys:
	    if not self.conds.has_key(key):
		return False
	return True

    def getCondValue(self,key):
	return self.conds[key]

    def getTable(self,table):
	return self.tables[table]
    
    
    
class SearchUserGroup:
    def __init__(self,op=""):
	self.__groups=[]
	self.setOperator(op)

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
