"""
select user_id from users where group_id=4 or group_id=5 
intersect 
select user_id from normal_users where username like 'a%' 
intersect 

    (select user_id,count(user_id) from users_attrs where (attr_name='charge_id' and (attr_value='2' or attr_value='3')) or (attr_name='rel_exp_date' and attr_value='2') group by user_id
    union 
    select users_attrs.user_id,count(users_attrs.user_id) from users,users_attrs,group_attrs,groups where users.group_id=groups.group_id and not exists
    (select attr_name from users_attrs where users_attrs.user_id=users.user_id and users_attrs.attr_name='charge_id' or attr_name='rel_exp_date') 
    and group_attrs.attr_name='charge_id' and group_attrs.attr_value='2' );
"""
from core.lib.general import *

class Condition:
    def __init__(self,cond_dic):
	self.cond_dic=self.__fix(cond_dic)

    def __getitem__(self,key):
	return self.cond_dic[key]

    def has_key(self,key):
	return self.cond_dic.has_key(key)

class SearchTable:
    def __init__(self,table_name):
	self._root_group=SearchUserGroup("and")
	self.table_name=table_name
    
    def addGroup(self,group):
	return self._root_group.addGroup(group)
    
    def addGroups(self,groups):
	return map(self.addGroup,groups)

    def getRootGroup(self):
	return self._root_group

    def getTableName(self):
	return self.table_name
    ############################# some helpers
    def getParsedValue(self,search_helper,dic_key,value_parser_method):
	value=search_helper.getCondValue(dic_key)
	if type(value)==types.StringType:
	    value=(value,)
	if value_parser_method!=None:
	    value=map(lambda val:apply(value_parser_method,[val]),value)
	
	return value

    def createColGroup(self,col_name,value,op):
	return "%s.%s %s %s"%(self.getTableName(),col_name,dbText(value),op)

    def searchOnConds(self,search_helper,cond_key,attr_db_name,value_parser_method,op):
	values=self.getParsedValue(search_helper,cond_key,value_parser_method)
	self.search(attr_db_name,values,op)

    def search(self,db_name,values,op):
	group=SearchUserGroup("or")
	groups=map(lambda value:group.addGroup(self.createColGroup(db_col_name,dbText(value),op)),values)
	self.addGroups(groups)

    def ltgtSearch(self,cond_key,cond_op_key,attr_db_name,value_parser_method=None):
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

    def exactSearch(self,search_helper,cond_key,db_col_name,value_parser_method=None):
	"""
	    do the exact search for one attribute.
	    cond_key(str): key of attribute in conditions that passed us from interface
	    db_col_name(str): name of attribute in database 
	    value_parser_method(callable): call this method on value and use the returned value in query
					   not that the returned value will go through dbText
	"""
	if search_helper.hasCondFor(cond_key):
	    self.searchOnConds(search_helper,cond_key,db_col_name,value_parser_method,"=")

    def likeStrSearch(self,search_helper,cond_key,cond_op_key,value_parser_method=None):
	"""
	"""
	if search_helper.hasCondFor(cond_key):
	    op=search_helper.getCondValue(cond_op_key)
	    values=self.getParsedValue(search_helper,cond_key,value_parser_method)
	    (op,values)=self.__applyLikeStrSearch(values,op)
	    self.search(db_col_name,values,op)

    def __applyLikeStrSearch(self,values,op):
	if op in ("like","ilike"):
	    method=lambda x:"%"+`x`+"%"
	elif op == "starts_with":
	    method=lambda x:"%"+`x`
	    op="ilike"
	elif op == "equals":
	    method=None
	    op="="
	else:
    	    raise GeneralException(errorText("USER_ACTIONS","INVALID_OPERATOR")%op)
	return (op,map(method,values))
	
    def createQuery(self):
	if not self.getRootGroup().isEmpty():
	    table_name=self.getTableName()
	    query="select %s.user_id from %s where %s"% \
		(table_name,table_name,self.getRootGroup().getConditionalClause())
	    return query

class SearchUsersTable(SearchTable):
    def __init__(self):
	SearchTable.__init__(self,"users")

class SearchNormalUsersTable(SearchTable):
    def __init__(self):
	SearchTable.__init__(self,"normal_users")

class SearchVoIPUsersTable(SearchTable):
    def __init__(self):
	SearchTable.__init__(self,"voip_users")

class SearchAttrsTable(SearchTable):
    def __init__(self,table_name):
	SearchTable.__init__(self,table_name)
	self.attrs=[]
    
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

    def search(self,attr_db_name,values,op):
	"""
	"""
	self.addAttr(attr_db_name)
	group=self.createAttrGroup(attr_db_name,values,op)
	self.addGroup(group)

    def createAttrGroup(self,attr_name,attr_values,op):
	"""
	    attr_values(list or iterable object): list of values
	"""
	group=SearchUserGroup("and")
	group.addGroup("%s.attr_name = %s"%(self.getTableName(),dbText(attr_name)))
	sub_group=SearchUserGroup("or")
	map(lambda value:sub_group.addGroup("%s.attr_value %s %s"%(self.getTableName(),op,dbText(value))),attr_values)
	group.addGroup(sub_group)
	return group

    def addAttr(self,attr):
	self.attrs.append(attr)

    def getAttrs(self):
	return self.attrs

class SearchUserAttrsTable(SearchAttrsTable):
    def __init__(self):
	SearchAttrsTable.__init__(self,"user_attrs")

    def createQuery(self):
	if not self.getRootGroup().isEmpty():
	    return "select user_attrs.user_id,count(user_attrs.user_id) from user_attrs where %s group by user_id"%\
		    (self.getRootGroup().getConditionalClause())

class SearchGroupAttrsTable(SearchAttrsTable):
    def __init__(self):
	SearchAttrsTable.__init__(self,"group_attrs")

    def createQuery(self):
	if not self.getRootGroup().isEmpty():
	    attr_not_in_user=self.__createNotInUserAttrsClause()
	    return "select users.user_id,count(users.user_id) from users,groups,group_attrs \
		    where users.group_id = groups.group_id and \
		    groups.group_id = group_attrs.group_id and \
	    	    not exists (select attr_name from user_attrs where user_attrs.user_id = users.user_id and %s) \
		    and %s group by users.user_id "% \
		    (attr_not_in_user,self.getRootGroup().getConditionalClause())

    def __createNotInUserAttrsClause(self):
	group=SearchUserGroup("or")
	map(lambda attr_name:group.addGroup("attr_name = %s"%dbText(attr_name)),self.getAttrs())
	return group.getConditionalClause()
    
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

    def createQuery(self):
	table_query=self.__getTableQueries()
	attrs_query=self.__createAttrsQuery(table_query["user_attrs"],table_query["group_attrs"])
	queries=self.__filterNoneQueries(attrs_query,table_query["users"],table_query["normal_users"],table_query["voip_users"])
	return self.__intersectQueries(queries)


    def __filterNoneQueries(self,*args):
	return filter(lambda x:x!=None,args)

    def __intersectQueries(self,queries):
	return " intersect ".join(queries)

    def __getTableQueries(self):
	table_query={}
	for table_name in self.tables:
	    table_query[table_name]=self.tables[table_name].createQuery()
	return table_query
    
    def __createAttrsQuery(self,user_attrs,group_attrs):
	if user_attrs!= None and group_attrs!=None:
	    sub_query="select count(user_id) as count,user_id from (%s union %s) as all_attrs group by user_id"%(user_attrs,group_attrs)
	elif user_attrs!=None:
	    sub_query="select count(user_id) as count,user_id from (%s) as all_attrs group by user_id"%(user_attrs)
	elif group_attrs!=None:
	    sub_query="select count(user_id) as count,user_id from (%s) as all_attrs group by user_id"%(group_attrs)
	else:
	    return None

	return "select user_id from (%s) as filtered_attrs where count=%s"%(sub_query,len(self.getTable("user_attrs").getAttrs()))
    
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
    
    def isEmpty(self):
	return len(self.__groups)==0

    def __getConditionStr(self,group_obj):
	if isinstance(group_obj,SearchUserGroup):
	    return group_obj.getConditionalClause()
	else:
	    return group_obj


def checkltgtOperator(op):
    if op not in ("=",">","<",">=","<="):
        raise GeneralException(errorText("USER_ACTIONS","INVALID_OPERATOR")%op)
