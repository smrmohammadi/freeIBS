import types
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

    
    def get(self,table,condition="true",from_=0,to=-1,orderBy="",rows=[]):
	"""
	    orderBy (str or tuple): if it's an string, it will be placed after the order by clause
				    if it's a tuple, it'll interpreted as (col_name,desc_flag) where desc_flag
					is a boolean telling if it should be ordered desc.
	
	"""
        query="select "
        if len(rows)==0:
            query+="*"
        else:         
            query+=",".join(rows)

        query += " from " + table 
	if condition!="":
	    query+= " where " + condition + " "
        
        if orderBy != "":
	    order_by_clause=self.__createOrderBy(orderBy)

            query += " order by %s"%order_by_clause

        if from_ >0:
            query +=" offset " + str(from_)
        if to > from_:
            query +=" limit " + str(to-from_)

        result=self.query(query)
        return self.getDictResult(result)

    def __createOrderBy(self,order_by):
	if type(order_by)==types.StringType:
	    return order_by
	elif type(order_by)==types.TupleType:
	    if order_by[1]:	
	        desc="desc"
	    else:
	        desc="asc"
	    return "%s %s"%(order_by[0],desc)

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
    if len(dict_values)==0:
        raise DBException("Empty values for insert")
    
    names="("+",".join(dict_values.keys())+")"
    values="("+",".join(map(str,dict_values.values()))+")"
    return "insert into %s %s VALUES %s ;"%(table,names,values)


def createUpdateQuery(table,dict_values,condition):
    """
	create query to update "dict_values" with condition "condition" on "table" 
	dict_value is in form {column_name=>value}
    """
    if len(dict_values)==0:
        raise DBException("Empty values for update")
    set_list=map(lambda name:"%s = %s"%(name,dict_values[name]),dict_values)
    query="update %s set %s where %s ;" % (table,",".join(set_list),condition)
    return query 

def createDeleteQuery(table,condition):
    return "delete from " + table + " where " + condition + ";"
