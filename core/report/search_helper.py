class SearchHelper:
    def __init__(self,conds,admin_obj,tables):
	"""
	    conds(dic like object): dictionary of conditions
	    admin_obj(Admin instance): Admin that requested the search
    	    tables(dic): dictionary of database tables involving search in format "table_name":search_table_instance
	"""
        self.conds=conds
	self.admin_obj=admin_obj
        self.tables=tables

    def getAdminObj(self):
	return self.admin_obj
	
    def getConds(self):
	return self.conds
    
    def hasCondFor(self,*keys):
	for key in keys:
	    if not self.conds.has_key(key):
		return False
	return True

    def getCondValue(self,key):
	return self.conds[key]

    def setCondValue(self,key,value):
	self.conds[key]=value

    def getTable(self,table):
	return self.tables[table]

    def createGetIDQuery(self,if_empty_query):
	"""
	    create a select query, by intersecting all table queries.
	    If none of tables has a query, it will return "if_empty_query"
	"""
	queries=self.getTableQueries()
	queries=apply(self.filterNoneQueries,queries.values())
	if len(queries)==0:
	    query=if_empty_query
	else:
	    query=self.intersectQueries(queries)
	return query
	

    def getTableQueries(self):
	table_query={}
	for table_name in self.tables:
	    table_query[table_name]=self.tables[table_name].createQuery()
	return table_query

    def filterNoneQueries(self,*args):
	return filter(lambda x:x!=None,args)

    def intersectQueries(self,queries):
	return " intersect ".join(queries)

    def createTempTableAsQuery(self,db_handle,table_name,query):
    	db_handle.query("create temp table %s as (%s)"%(table_name,query))

    def dropTempTable(self,db_handle,table_name):
	db_handle.query("drop table %s"%table_name)
	
