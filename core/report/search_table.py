from core.lib.multi_strs import MultiStr
from core.report.search_group import SearchGroup
from core.lib.general import *
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.date import AbsDateWithUnit

class SearchTable:
    def __init__(self,table_name):
	self._root_group=SearchGroup("and")
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
	if value_parser_method==MultiStr:
	    value=MultiStr(value)
	else:
	    if type(value)==types.StringType:
		value=(value,)
		
	    if callable(value_parser_method):
	        value=map(lambda val:apply(value_parser_method,[val]),value)
	
	return value

    #############################
    def createColGroup(self,col_name,value,op):
	return "%s.%s %s %s"%(self.getTableName(),col_name,op,dbText(value))

    #############################
    def searchOnConds(self,search_helper,cond_key,attr_db_name,value_parser_method,op):
	values=self.getParsedValue(search_helper,cond_key,value_parser_method)
	self.search(attr_db_name,values,op)

    def search(self,db_name,values,op):
	"""
	    add a condition, for "db_name op values"
	    values should be iterable object
	"""
	group=SearchGroup("or")
	map(lambda value:group.addGroup(self.createColGroup(db_name,value,op)),values)
	self.addGroup(group)

    ############################
    def ltgtSearch(self,search_helper,cond_key,cond_op_key,attr_db_name,value_parser_method=None):
	"""
	"""
	if search_helper.hasCondFor(cond_key,cond_op_key):
	    checkltgtOperator(search_helper.getCondValue(cond_op_key))
	    self.searchOnConds(search_helper,
			cond_key,
			attr_db_name,
			value_parser_method,
			search_helper.getCondValue(cond_op_key)
		       )

    ###########################
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

    ##########################
    def likeStrSearch(self,search_helper,cond_key,cond_op_key,db_col_name,value_parser_method=None):
	"""
	    search like Str on db_col_name, if cond_key is available in conditions
	"""

	if search_helper.hasCondFor(cond_key,cond_op_key):
	    op=search_helper.getCondValue(cond_op_key)
	    values=self.getParsedValue(search_helper,cond_key,value_parser_method)
	    (op,values)=self.__applyLikeStrSearch(values,op)
	    self.search(db_col_name,values,op)

    def __applyLikeStrSearch(self,values,op):
	if op in ("like","ilike"):
	    method=lambda x:"%"+str(x)+"%"
	elif op == "starts_with":
	    method=lambda x:"%"+str(x)
	    op="ilike"
	elif op == "ends_with":
	    method=lambda x:str(x)+"%"
	    op="ilike"
	elif op == "equals":
	    method=None
	    op="="
	else:
    	    raise GeneralException(errorText("USER_ACTIONS","INVALID_OPERATOR")%op)
	return (op,map(method,values))
	
    ###########################
    def dateSearch(self,search_helper,cond_key,cond_unit_key,cond_op_key,db_col_name,value_parser_method=None):
	"""
	"""
	if search_helper.hasCondFor(cond_key,cond_unit_key,cond_op_key):
	    date_str=AbsDateWithUnit(search_helper.getCondValue(cond_key),
				     search_helper.getCondValue(cond_unit_key)).getDate("gregorian")
	    search_helper.setCondValue(cond_key,date_str)
	    self.ltgtSearch(search_helper,cond_key,cond_op_key,db_col_name,value_parser_method)    
    
    ###########################
    def createQuery(self):
	"""
	    create a select query to retrieve data from table, with given conditions, may return None when 
	    there's no conditions
	"""
	pass



class SearchAttrsTable(SearchTable):
    def __init__(self,table_name):
	SearchTable.__init__(self,table_name)
	self.attrs=[]

    def hasAttrSearch(self,search_helper,dic_key,attr_db_name,value_parser_method=None):
	"""
	    do search to check if table has attr_db_name
	"""    
	if search_helper.hasCondFor(dic_key):
	    self.addAttr(attr_db_name)
    	    self.addGroup("%s.attr_name = %s"%(self.getTableName(),dbText(attr_db_name)))
    
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
	group=SearchGroup("and")
	group.addGroup("%s.attr_name = %s"%(self.getTableName(),dbText(attr_name)))
	sub_group=SearchGroup("or")
	map(lambda value:sub_group.addGroup("%s.attr_value %s %s"%(self.getTableName(),op,dbText(value))),attr_values)
	group.addGroup(sub_group)
	return group

    def addAttr(self,attr):
	self.attrs.append(attr)

    def getAttrs(self):
	return self.attrs
