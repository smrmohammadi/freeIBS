from core.lib.general import *
import itertools

class AttrSearcher:
    def __init__(self,search_helper):
	self.search_helper=search_helper

    def getSearchHelper(self):
	return self.search_helper

    def run(self):
	"""
	    AttrSearchers should override this method and do the real job here
	    by updating search_helper groups and addTable
	"""
	pass

    def exactSearchForAttr(self,dic_key,attr_db_name,value_parser_method=None):
	"""
	    do the exact search for one attribute.
	    dic_key(str): key of attribute in conditions that passed us from interface
	    attr_db_name(str): name of attribute in database attr_name field
	    value_parser_method(callable): call this method on value and use the returned value in query
					   not that the returned value will go through dbText
	"""
	if self.getSearchHelper().hasConditionFor(dic_key):
	    self.getSearchHelper().addTable("user_attrs")
	    value=self.__getParsedValue(dic_key,value_parser_method)
	    groups=map(self.attrEqualsGroup(attr_db_name,value),)
	    self.getSearchHelper().getRootGroup().addGroup(group)

    def attrEqualsGroup(self,attr_name,attr_value):
	group=SearchUserGroup()
	group.addGroup("attr_name=%s"%dbtext(attr_name))
	group.addGroup("attr_value=%s"%dbText(value))
	group.setOperator("and")
	return group

    def exactSearchForBasicInfo(self,dic_key,db_col_name,value_parser_method=None):
	"""
	    do the exact search for one attribute.
	    dic_key(str): key of attribute in conditions that passed us from interface
	    db_col_name(str): name of attribute in database 
	    value_parser_method(callable): call this method on value and use the returned value in query
					   not that the returned value will go through dbText
	"""
	if self.getSearchHelper().hasConditionFor(dic_key):
	    self.getSearchHelper().addTable("users")
	    value=self.__getParsedValue(dic_key,value_parser_method)
	    self.getSearchHelper().getRootGroup().addGroup("%s = %s"%(db_col_name,dbtext(value)))

    def __getParsedValue(self,dic_key,value_parser_method):
	if value_parser_method==None:
	    value=self.getSearchHelper().getConditionValue(dic_key)
	else:
	    value=map(lambda val:apply(value_parser_method,val),self.getSearchHelper().getConditionValue(dic_key))

	