from core.ibs_exceptions import *
from core import defs

class ibs_db: #abstract parent class for all db implementions. Children must implement esp. query and connect 
    connHandle=None
    
    def __init__(self,dbname,host,port,user,password):
        self.connHandle=None
        self.connect(dbname,host,port,user,password)

    def connect(self,dbname,host,port,user,password):
        pass
    
    def _runQuery(self,query):
	"""
	    run the query, without any exception handleing
	    users normally should use query or transactionQuery ot IBSQuery class, and should not
	    use this method directly
	"""
	self.__logQuery(query)


    def query(self,query):
	"""
	    run the query
	"""
	pass

    def transactionQuery(self,query):
	pass

    def runIBSQuery(self,ibs_query):
	"""
	    run IBS query class queries
	"""
	pass

    def __logQuery(self,query):
        if defs.LOG_DATABASE_QUERIES:
	    toLog(query,LOG_QUERY)
	
    def getConnection(self):
        if self.connHandle==None:
            raise dbException("None connection")
        return self.connHandle

    def reset(self):
        self.getConnection().reset()

    
    def close(self):
        self.getConnection().close()
        self.pgConn=None

    
    def get(self,table,condition,from_=0,to=-1,orderBy="",rows=[]):
        query="select "
        if rows==[]:
            query+="*"
        else:         
            for m in rows:
                query+=m+","
            query=query[:-1]

        query += " from " + table + " where " + condition + " "
        
        if orderBy != "":
            query += "order by " + orderBy
        if from_ >0:
            query +=" offset " + str(from_)

        if to > from_:
            query +=" limit " + str(to-from_)

        result=self.query(query)
        return self.getDictResult(result)

    def selectQuery(self,query):
	result=self.query(query)
	return self.getDictResult(result)
    
    def getDictResult(self,result):
        return result.dictresult()
    

    def insert(self,table,dict_values):    
	query=createInsertQuery(table,dict_values)
        self.transactionQuery(query)
        
    def update(self,table,dict_values,condition):
	query=createUpdateQuery(table,dict_values,condition)
        self.transactionQuery(query)

    def delete(self,table,condition):
	query=createDeleteQuery(table,condition)
        self.query(query)

    def release(self):
	from core.db import dbpool
        dbpool.release(self)

    def check(self):
        pass

    def seqNextVal(self,seq_name):
	"""
	    return next value of sequenece "seq_name",
	    this supposed to be thread safe
	"""
	return self.selectQuery("select nextval('%s')"%seq_name)[0]["nextval"]

    def getCount(self,table,condition):
	"""
	    return result row count for query with condition "condition" from "table"
	"""
	return self.get(table,condition,0,-1,"",["count(*) as count"])[0]["count"]


def createInsertQuery(table,dict_values):
    """
	create and return an insert query to insert "dict_values" into "table"
	"dict_values" is in form {column_name=>value}
    """
    if len(dict_values)<1:
        raise dbException("Empty values for insert")
    
    names="("
    values="("
    for name in dict_values:
        names += str(name)+","
        values += str(dict_values[name])+","
    names=names[:-1]
    values=values[:-1]
    names+=") "
    values+=") "
    return "insert into %s %s VALUES %s ;"%(table,names,values)


def createUpdateQuery(table,dict_values,condition):
    """
	create query to update "dict_values" with condition "condition" on "table" 
	dict_value is in form {column_name=>value}
    """
    if len(dict_values)<1:
        raise dbException("Empty values for update")
    query="update %s set " % table
    for name in dict_values:
        query+=" %s = %s ,"%(name,dict_values[name])
    query=query[:-1]
    query+=" where %s ;"%condition
    return query 

def createDeleteQuery(table,condition):
    return "delete from " + table + " where " + condition + ";"
