from core.lib.general import *
from core.db.ibs_query import IBSQuery
from core.db import ibs_db,db_main

class ConnectionLogActions:
    TYPES={"internet":1,"voip":2}
    def logConnectionQuery(self,user_id,credit_used,login_time,logout_time,successful,_type,ras_id,details):
	"""
	    user_id(int): id of user, this connection is related to
	    credit_used(float): amount of credit used by user
	    login_time(str): string representaion of user login time
	    logout_time(str): string representaion of user logout time
	    successful(boolean): was user connection successful, or it failed and user connection didn't established normally in authentication or authorization phase
	    _type(str): type of connection, can be "internet" or "voip"
	    ras_id(integer): id of ras, connection made to
	    details(dictionary): dic of connection details, varying for diffrent types/rases/connections
	"""
	connection_log_id=self.__getNewConnectionLogID()
	ibs_query=IBSQuery()
	ibs_query+=self.__insertConnectionQuery(connection_log_id,credit_used,login_time,logout_time,successful,self.getTypeValue(_type),ras_id)
	self.__insertConnectionDetailsQuery(ibs_query,details)
	return ibs_query

    def __getNewConnectionLogID(self):
    	return db_main.getHandle().seqNextVal("connection_log_id")


    def __insertConnectionQuery(self,connection_log_id,credit_used,login_time,logout_time,successful,_type,ras_id):
	return ibs_db.createInsertQuery("connection_log",{"connection_log_id":connection_log_id,
							  "credit_used":credit_used,
							  "login_time":dbText(login_time),
							  "logout_time":dbText(logout_time),
							  "successful":successful,
							  "service":_type,
							  "ras_id":ras_id})
    
    def __insertConnectionDetailsQuery(self,ibs_query,details):
	for name in details:
	    ibs_query+=self.__insertConnectionDetailQuery(name,details[name])
	return ibs_query

    def __insertConnectionDetailQuery(self,name,value):
	return ibs_db.createInsertQuery("connection_log_details",{"name":dbText(name),"value":dbText(value)})

    def getTypeValue(self,_type):
	return self.TYPES[_type]
	