from core.lib.general import *

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
	    if value_parser_method==None:
		value=self.getSearchHelper().getDBConditionValue(dic_key)
	    else:
		value=dbText(apply(value_parser_method,self.getSearchHelper().getConditionValue(dic_key)))
		
	    group=SearchUserGroup()
	    group.addGroup("attr_name=%s"%dbtext(attr_db_name))
	    group.addGroup("attr_value=%s"%value)
	    group.setOperator("and")
	    self.getSearchHelper().getRootGroup().addGroup(group)
