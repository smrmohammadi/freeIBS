from core.report.search_helper import SearchHelper
from core.report.search_table import SearchTable,SearchAttrsTable
from core.report.search_group import SearchGroup
from core.lib.multi_strs import MultiStr
from core.lib import report_lib
from core.lib.date import AbsDate
from core.admin import admin_main
from core.user import user_main
from core.ras import ras_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.db import db_main
import types

class ConnectionLogSearchTable(SearchTable):
    def __init__(self):
	SearchTable.__init__(self,"connection_log")
	
    def createQuery(self):
    	if not self.getRootGroup().isEmpty():
	    table_name=self.getTableName()
	    return "select connection_log_id from %s where %s"%(table_name,self.getRootGroup().getConditionalClause())

class ConnectionLogDetailsSearchTable(SearchAttrsTable):
    def __init__(self):
	SearchAttrsTable.__init__(self,"connection_log_details")
	
    def createQuery(self):
    	if not self.getRootGroup().isEmpty():
	    table_name=self.getTableName()
	    return "select connection_log_id from %s where %s"%(table_name,self.getRootGroup().getConditionalClause())
	

class ConnectionSearchHelper(SearchHelper):
    def __init__(self,conds,admin_obj):
	SearchHelper.__init__(self,conds,admin_obj,{"connection_log":ConnectionLogSearchTable(),
						    "connection_log_details":ConnectionLogDetailsSearchTable()})
    def getConnectionLogs(self,_from,to,order_by,desc,date_type):
	db_handle=db_main.getHandle(True)
	self.__createTempTable(db_handle)
	total_rows=self.__getTotalResultsCount(db_handle)
	if total_rows==0:
	    return (0,0,"00:00:00",[])
	total_credit_used=self.__getTotalCreditUsed(db_handle)
	total_duration=self.__getTotalDuration(db_handle)
	connections=self.__getConnections(db_handle,_from,to,order_by,desc)
	connection_details=self.__getConnectionDetails(db_handle,connections)
	self.dropTempTable(db_handle,"connection_log_report")
	db_handle.releaseHandle()
	return (total_rows,total_credit_used,total_duration,self.__createReportResult(connections,connection_details,date_type))

    def __createReportResult(self,connections,connection_details,date_type):
	details_dic=self.__convertConnectionDetailsToDic(connection_details)
	self.__repairConnectionsDic(connections,details_dic,date_type)
	return connections
	
    def __repairConnectionsDic(self,connections,details_dic,date_type):
	for connection in connections:
	    try:
		connection["login_time_formatted"]=AbsDate(connection["login_time"],"gregorian").getDate(date_type)
		connection["logout_time_formatted"]=AbsDate(connection["logout_time"],"gregorian").getDate(date_type)
		connection["ras_ip"]=ras_main.getLoader().getRasByID(connection["ras_id"]).getRasIP()
		connection["service_type"]=user_main.getConnectionLogManager().getIDType(connection["service"])
		connection["details"]=details_dic[connection["connection_log_id"]]
	    except KeyError:
		pass
    
	return connections
	
    def __convertConnectionDetailsToDic(self,connection_details):
	details_dic={}
	last_id=None
	for detail in connection_details:
	    if last_id!=detail["connection_log_id"]:
		if last_id!=None:
		    details_dic[last_id]=per_detail_list
		last_id=detail["connection_log_id"]
		per_detail_list=[]
	    per_detail_list.append((detail["name"],detail["value"]))

	if last_id!=None:
	    details_dic[last_id]=per_detail_list

	return details_dic
		
    def __getConnectionDetails(self,db_handle,connections):
	connection_log_id_conds=map(lambda x:"connection_log_id=%s"%x["connection_log_id"],connections)
	return db_handle.get("connection_log_details",
			     " or ".join(connection_log_id_conds),
			     0,-1,"connection_log_id,name desc")

    def __getConnections(self,db_handle,_from,to,order_by,desc):
	return db_handle.get("connection_log_report,connection_log",
		             "connection_log.connection_log_id=connection_log_report.connection_log_id",
			     _from,
			     to,
			     (order_by,desc),
			     ["*",
			      "cast(logout_time-login_time as time) as duration",
			      "extract(seconds from logout_time-login_time) as duration_seconds"
			     ]
			    )
		      
    def __createTempTable(self,db_handle):
	select_query=self.__createConnectionLogIDsQuery()
	self.createTempTableAsQuery(db_handle,"connection_log_report",select_query)

    def __getTotalResultsCount(self,db_handle):
	return db_handle.getCount("connection_log_report","true")

    def __getTotalCreditUsed(self,db_handle):
	if self.hasCondFor("show_total_credit_used"):
	    return db_handle.selectQuery("select sum(credit_used) as sum from connection_log,connection_log_report where \
					   connection_log.connection_log_id=connection_log_report.connection_log_id")[0]["sum"]
	return -1

    def __getTotalDuration(self,db_handle):
	if self.hasCondFor("show_total_duration"):
	    return db_handle.selectQuery("select cast(sum(logout_time-login_time) as time) as sum from connection_log,connection_log_report where \
					   connection_log.connection_log_id=connection_log_report.connection_log_id")[0]["sum"]
	return -1
    
    def __createConnectionLogIDsQuery(self):
	queries=self.getTableQueries()
	queries=apply(self.filterNoneQueries,queries.values())
	if len(queries)==0:
	    query="select connection_log_id from connection_log"
	else:
	    query=self.intersectQueries(queries)
	return query

class ConnectionSearcher:
    def __init__(self,conds,admin_obj):
	self.search_helper=ConnectionSearchHelper(conds,admin_obj)
	
    ##############################################
    def applyConditions(self):
	"""
	    Apply conditions on tables, should check conditions here
	"""
	con_table=self.search_helper.getTable("connection_log")
	con_details_table=self.search_helper.getTable("connection_log_details")

	self.__addUserIDCondition(con_table)

	con_table.ltgtSearch(self.search_helper,"credit_used","credit_used_op","credit_used")
    
	con_table.dateSearch(self.search_helper,"login_time","login_time_unit","login_time_op","login_time")

	con_table.dateSearch(self.search_helper,"logout_time","login_time_unit","logout_time_op","logout_time")
	
	con_table.exactSearch(self.search_helper,"successful","successful",lambda bool:dbText(("t","f")[bool]))

	con_table.exactSearch(self.search_helper,"service","service",lambda _type:user_main.getConnectionLogManager().getTypeValue(_type))

	con_table.exactSearch(self.search_helper,"ras_ip","ras_id",lambda ras_ip:ras_main.getLoader().getRasByIP(ras_ip).getRasID())
	
    def __addUserIDCondition(self,con_table):
	admin_restricted=not self.search_helper.getAdminObj().isGod() and self.search_helper.getAdminObj().getPerms()["SEE CONNECTION LOGS"].isRestricted()
	if admin_restricted or self.search_helper.hasCondFor("owner"):
	    if admin_restricted:
		owner_ids=(self.search_helper.getAdminObj().getAdminID(),)
	    else:
		owner_name=self.search_helper.getCondValue("owner")
		if type(owner_name)==types.StringType:
		    owner_name=(owner_name,)
		owner_ids=map(lambda owner_name:admin_main.getLoader().getAdminByName(owner_name).getAdminID(),owner_name)
	    
	    sub_query=self.__userOwnersConditionQuery(owner_ids)
	    self.search_helper.getTable("connection_log").getRootGroup().addGroup(sub_query)	    
	
    	con_table.exactSearch(self.search_helper,"user_ids","user_id",MultiStr)	

    def __userOwnersConditionQuery(self,owner_ids):
	"""
	    Change to exists subquery, if performance is low. also possible to filter user_ids in case of user_id
	    conditions to boost speed
	"""
	cond_group=SearchGroup("or")
	map(lambda owner_id:cond_group.addGroup("users.owner_id=%s"%owner_id),owner_ids)
	return "connection_log.user_id in (select user_id from users where %s)"%cond_group.getConditionalClause()
	
    #################################################
    def getConnectionLog(self,_from,to,order_by,desc,date_type):
	"""
	    if total_credit or total_duration is smaller thatn 0, then it was not requested by caller, so we didn't
		calculate em
	"""
	
	self.__getConnectionLogCheckInput(_from,to,order_by,desc)
	self.applyConditions()
	(total_rows,total_credit,total_duration,report)=self.search_helper.getConnectionLogs(_from,to,order_by,desc,date_type)
	return {"total_rows":total_rows,
		"total_credit":total_credit,
		"total_duration":total_duration,
		"report":report
	       }

    def __getConnectionLogCheckInput(self,_from,to,order_by,desc):
	report_lib.checkFromTo(_from,to)
	self.__checkOrderBy(order_by)
	
    def __checkOrderBy(self,order_by):
	if order_by not in ["user_id","credit_used","login_time","logout_time","successful","service","ras_id"]:
	    raise GeneralException(errorText("GENERAL","INVALID_ORDER_BY")%order_by)
	    

_comment="""
IBSng=# EXPLAIN ANALYZE select * from connection_log where user_id in (select user_id from users where owner_id=0 or owner_id=1) order by login_time;
                                                     QUERY PLAN
---------------------------------------------------------------------------------------------------------------------
 Sort  (cost=2.23..2.23 rows=1 width=44) (actual time=0.173..0.189 rows=9 loops=1)
   Sort Key: connection_log.login_time
   ->  Nested Loop  (cost=1.02..2.22 rows=1 width=44) (actual time=0.053..0.139 rows=9 loops=1)
         Join Filter: ("inner".user_id = "outer".user_id)
         ->  HashAggregate  (cost=1.02..1.02 rows=1 width=8) (actual time=0.033..0.035 rows=1 loops=1)
               ->  Seq Scan on users  (cost=0.00..1.01 rows=1 width=8) (actual time=0.015..0.018 rows=1 loops=1)
                     Filter: ((owner_id = 0) OR (owner_id = 1))
         ->  Seq Scan on connection_log  (cost=0.00..1.09 rows=9 width=44) (actual time=0.005..0.030 rows=9 loops=1)
 Total runtime: 0.298 ms
(9 rows)

IBSng=# EXPLAIN ANALYZE select * from connection_log where exists (select users.user_id from users where users.user_id=connection_log.user_id and (users.owner_id=0 or owner_id=1)) order by login_time;
                                                   QUERY PLAN
----------------------------------------------------------------------------------------------------------------
 Sort  (cost=10.31..10.32 rows=5 width=44) (actual time=0.200..0.216 rows=9 loops=1)
   Sort Key: login_time
   ->  Seq Scan on connection_log  (cost=0.00..10.25 rows=5 width=44) (actual time=0.053..0.159 rows=9 loops=1)
         Filter: (subplan)
         SubPlan
           ->  Seq Scan on users  (cost=0.00..1.02 rows=1 width=8) (actual time=0.006..0.006 rows=1 loops=9)
                 Filter: ((user_id = $0) AND ((owner_id = 0) OR (owner_id = 1)))
 Total runtime: 0.296 ms
(8 rows)

"""