from core import ibs_exceptions
from core.db.ibs_db import *
import pg

class db_pg (ibs_db):
    
    def connect(self,dbname,host,port,user,password):
        try:
            self.connHandle=pg.connect(dbname,host,port,None,None,user,password)
        except Exception,e:
            raise ibs_exceptions.DBException(str(e))
        except pg.error,e:
            raise ibs_exceptions.DBException(str(e))

    def _runQuery(self,query):
	"""
	    run the query , no exception handling done here
	    return result set of query
	"""
	ibs_db._runQuery(self,query)
	connection=self.getConnection()
        return connection.query(query)

    def transactionQuery(self,query):
	ibs_db.transactionQuery(self,query)
	if len(query)>8000:
            raise ibs_exceptions.DBException("Can't execute large transaction: %s"%query)

	return self.__transactionQuery("BEGIN; %s COMMIT;"%query)
    
    def __transactionQuery(self,command):
        try:
	    return self._runQuery(command)
        except pg.error,e:
	    try:
		connection.query("ABORT;")
	    except:
		pass
	
	    raise ibs_exceptions.DBException("%s query: %s" %(e,command))

        except Exception,e:
	    try:
		connection.query("ABORT;")
	    except:
		pass

            raise ibs_exceptions.DBException("%s query: %s" %(e,command))


    
    def query(self,command):
	ibs_db.query(self,command)
        try:
	    return self._runQuery(command)
        except pg.error,e:
	    raise ibs_exceptions.DBException("%s query: %s" %(e,command))

        except Exception,e:
            raise ibs_exceptions.DBException("%s query: %s" %(e,command))

    def runIBSQuery(self,ibs_query):
	for query in ibs_query:
	    self.__transactionQuery(query)
    
    def check(self):
        try:
            self.query("BEGIN;ROLLBACK;")
        except Exception,e:
            try:
                self.reset()
            except Exception,e:
                raise ibs_exceptions.DBException("check function on reseting connection %s"%e)
            except pg.error,e:
                raise ibs_exceptions.DBException("check function on reseting connection %s"%e)