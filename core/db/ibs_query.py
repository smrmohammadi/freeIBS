from core.db import db_main

class IBSQuery:
    """
	IBSQuery is used for large transactions that are more than 8kb. The Query is passed to 
	database backend as many little queries.
    """
    def __init__(self):
	self.__queries=[]

    def __iter__(self):
	return iter(self.__queries)
	
    def __getitem__(self,_index):
	return self.__queries[_index]
    
    def __add__(self,query):
	if isinstance(query,IBSQuery):
	    map(self.addQuery,query.getQueries())
	else:
	    self.addQuery(query)
	return self
	
    def addQuery(self,query):
	"""
	    add a new query to the transaction
	"""
	self.__queries.append(query)

    
    def runQuery(self):
	"""
	    run the transaction query
	"""
	return db_main.getHandle().runIBSQuery(self)

    def getQueries(self):
	"""
	    return list of queries
	"""
	return self.__queries