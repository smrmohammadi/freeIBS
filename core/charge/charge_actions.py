from core.admin import admin_main
from core.charge import charge_main,charge_types,charge_rule
from core.lib.general import *
from core.lib.time_lib import *
from core.lib.day_of_week import *
from core.ibs_exceptions import *
from core.errors import errorText
from core.db import db_main,ibs_db
from core.ras import ras_main

class ChargeActions:
    CHARGE_TYPES=["Internet","VoIP"]
    def addCharge(self,name,comment,charge_type,admin_id,visible_to_all):
	"""
	    add a charge to database, and command the charge loader to load it
	"""
	self.__addChargeCheckInput(name,comment,charge_type,admin_id,visible_to_all)
	charge_id=self.__getNewChargeID()
	self.__insertNewCharge(charge_id,name,comment,charge_type,admin_id,visible_to_all)
	charge_main.getLoader().loadCharge(charge_id)
	
    
    def __addChargeCheckInput(self,name,comment,charge_type,admin_id,visible_to_all):
	"""
	    check addCharge inputs validity
	    raise exception on bad input
	"""
	admin_main.getLoader().checkAdminID(admin_id)
	checkDBBool(visible_to_all,"Visible to all")
	self.__checkChargeType(charge_type)
	if charge_main.getLoader().chargeNameExists(name):
	    raise GeneralException(errorText("CHARGES","CHARGE_NAME_EXISTS") % name)
	
	if not isValidName(name):
	    raise GeneralException(errorText("CHARGES","INVALID_CHARGE_NAME") % name)

    def __checkChargeType(self,charge_type):
	if charge_type not in self.CHARGE_TYPES:
	    raise GeneralException(errorText("CHARGES","INVALID_CHARGE_TYPE")%charge_type)

    def __getNewChargeID(self):
	"""
	    return a new id for new charge
	"""
	return db_main.getHandle().seqNextVal("charges_id_seq")
	
    def __insertNewCharge(self,charge_id,name,comment,charge_type,admin_id,visible_to_all):
	"""
	    insert the new charge to db
	"""
	db_main.getHandle().insert("charges",{"charge_id":charge_id,
				 "name":dbText(name),
				 "comment":dbText(comment),
				 "charge_type":dbText(charge_type),
				 "admin_id":admin_id,
				 "visible_to_all":dbText(visible_to_all)
				 })

###########################################################
    def updateCharge(self,charge_id,name,comment,visible_to_all):
	"""
	    change charge rule properties
	"""
	self.__updateChargeCheckInput(charge_id,name,comment,visible_to_all)
	self.__updateCharge(charge_id,name,comment,visible_to_all)
	charge_main.getLoader().unloadCharge(charge_id)
	charge_main.getLoader().loadCharge(charge_id)


    def __updateChargeCheckInput(self,charge_id,name,comment,visible_to_all):
	"""
	    check inputs of changeChargeInfo
	    raise an exception on bad input
	"""
	charge_obj=charge_main.getLoader().getChargeByID(charge_id)
	checkDBBool(visible_to_all,"Visible To All")
	if charge_obj.getChargeName() != name and charge_main.getLoader().chargeNameExists(name):
		raise GeneralException(errorText("CHARGES","CHARGE_NAME_EXISTS") % name)

	if not isValidName(name):
	    raise GeneralException(errorText("CHARGES","INVALID_CHARGE_NAME") % name)

    def __updateCharge(self,charge_id,name,comment,visible_to_all):
	"""
	    update a charge rule information in DB
	"""
	db_main.getHandle().update("charges",{"name":dbText(name),
					      "comment":dbText(comment),
					      "visible_to_all":dbText(visible_to_all)
					     },"charge_id=%s"%charge_id)
###########################################################

    def addInternetChargeRule(self,charge_name,start_time,end_time,day_of_weeks,cpm,cpk,\
		    		   assumed_kps,bandwidth_limit_kbytes,ras_id,ports):
	"""
	    add a charge rule to charge with id "charge_id" and reload the charge
	    it will add charge_rule and it's ports to db too
	"""
	start_time,end_time,day_of_weeks=self.__chargeRuleTimesCheck(start_time,end_time,day_of_weeks)
	self.__internetChargeRuleCheckInput(charge_name,cpm,cpk,assumed_kps,bandwidth_limit_kbytes,ras_id,ports)
	charge_obj=charge_main.getLoader().getChargeByName(charge_name)
	day_of_weeks_container=self.__createDayOfWeekContainer(day_of_weeks)
	rule_obj=self.__createInternetChargeRuleObject(charge_obj,start_time,end_time,day_of_weeks_container,\
				cpm,cpk,assumed_kps,bandwidth_limit_kbytes,ras_id,ports)
        self.__checkRuleConflict(charge_obj,rule_obj)
        self.__addInternetChargeRuleToDB(rule_obj)
        charge_main.getLoader().loadCharge(charge_obj.getChargeID())


    def __internetChargeRuleCheckInput(self,charge_name,cpm,cpk,assumed_kps,bandwidth_limit_kbytes,ras_id,ports):
	self.__chargeRuleCheckInput(charge_name,"Internet",ras_id,ports)
	try:
	    assumed_kps=int(assumed_kps)
	except:
	    raise GeneralException(errorText("CHARGES","ASSUMED_KPS_NOT_INTEGER"))

	try:
	    bandwidth_limit_kbytes=int(bandwidth_limit_kbytes)
	except:
	    raise GeneralException(errorText("CHARGES","BANDWIDTH_LIMIT_NOT_INTEGER"))

	try:
	    cpm=float(cpm)
	except:
	    raise GeneralException(errorText("CHARGES","CPM_NOT_NUMERIC"))

	try:
	    cpk=float(cpk)
	except:
	    raise GeneralException(errorText("CHARGES","CPK_NOT_NUMERIC"))
	    
	if assumed_kps<=0:
	    raise GeneralException(errorText("CHARGES","ASSUMED_KPS_NOT_POSITIVE"))

	if bandwidth_limit_kbytes<=0:
	    raise GeneralException(errorText("CHARGES","BANDWIDTH_LIMIT_NOT_POSITIVE"))
	    
	if cpm<0:
	    raise GeneralException(errorText("CHARGES","CPM_NOT_POSITIVE"))
	    
	if cpk<0:
	    raise GeneralException(errorText("CHARGES","CPK_NOT_POSITIVE"))

    def __addInternetChargeRuleToDB(self,rule_obj):
	"""
	    add rule_obj properties to DB
	"""
	charge_rule_id=self.__getNewChargeRuleID()
	rule_obj.setRuleID(charge_rule_id)
	query=self.__addChargeRuleAndPortsQuery(rule_obj)
	db_main.getHandle().transactionQuery(query)

    def __getNewChargeRuleID(self):
	"""
	    return an id for new charge_rule
	"""
	return db_main.getHandle().seqNextVal("charge_rules_id_seq")


    def __addChargeRuleAndPortsQuery(self,rule_obj):
	"""
	    return query for inserting "rule_obj" with id "charge_rule_id"
	"""
	return self.__addInternetChargeRuleQuery(rule_obj) + \
	       self.__addChargeRulePortsQuery(rule_obj.getPorts(),rule_obj.getRuleID()) + \
	       self.__addChargeRuleDowsQuery(rule_obj.getDows(),rule_obj.getRuleID())
	
    def __addInternetChargeRuleQuery(self,rule_obj):
	"""
	    return query for inserting rule_obj properties into charge_rules table
	"""
	if rule_obj.getRasID() == charge_rule.ChargeRule.ALL:
	    ras_id="NULL"
	else:
	    ras_id=rule_obj.getRasID()
	return ibs_db.createInsertQuery("internet_charge_rules",{"charge_id":rule_obj.charge_obj.getChargeID(),
							"charge_rule_id":rule_obj.getRuleID(),
							"start_time":dbText(rule_obj.start_time),
							"end_time":dbText(rule_obj.end_time),
							"cpm":float(rule_obj.cpm),
							"cpk":float(rule_obj.cpk),
							"assumed_kps":integer(rule_obj.assumed_kps),
							"bandwidth_limit_kbytes":integer(rule_obj.bandwidth_limit),
							"ras_id":ras_id
							})

    def __addChargeRulePortsQuery(self,ports_list,charge_rule_id):
	"""
	    return query for inserting "ports" to charge_rule "charge_rule_id"
	"""
	if None in ports_list:
	    ports_list=[dbNull(None)]
	query=""
	for port in ports_list:
	    query+=ibs_db.createInsertQuery("charge_rule_ports",{"charge_rule_id":charge_rule_id,
								 "ras_port":dbText(port)
								})
	return query

    def __addChargeRuleDowsQuery(self,dows_container,charge_rule_id):
	"""
	    return query for inserting "dows_container" to charge_rule "charge_rule_id"
	"""
	query=""
	for dow in dows_container:
	    query+=ibs_db.createInsertQuery("charge_rule_day_of_weeks",{"charge_rule_id":charge_rule_id,
								 "day_of_week":dow.getIntValue()
								})
	return query

################################################################3
    def __checkChargeRuleInCharge(self,charge_rule_id,charge_name):
	"""
	    check if charge rule with id "charge_rule_id" is in charge with name "charge_name"
	    raise a GeneralException if it isn't
	"""
	if charge_rule_id not in charge_main.getLoader().getChargeByName(charge_name).getRules():
	    raise GeneralException(errorText("CHARGES","CHARGE_RULE_NOT_IN_CHARGE")%(charge_rule_id,charge_name))
    

    def __createDayOfWeekContainer(self,day_of_weeks):
	"""
	    day_of_weeks: list of day of weeks strings
	"""
	dows_container=DayOfWeekIntContainer()
	for dow in day_of_weeks:
	    dows_container.append(dow.getDowInt())
	return dows_container

    def __createInternetChargeRuleObject(self,charge_obj,start_time,end_time,day_of_week_container,cpm,cpk,\
		    			 assumed_kps,bandwidth_limit_kbytes,ras_id,ports,charge_rule_id=None):
	"""
	    create an half complete rule object from arguments and return it
	    this object is useful for checking conflict
	"""
	rule_info={}
	rule_info["charge_rule_id"]=charge_rule_id
	rule_info["cpm"]=cpm
	rule_info["cpk"]=cpk
	rule_info["start_time"]=start_time.getFormattedTime()
	rule_info["end_time"]=end_time.getFormattedTime()
	rule_info["bandwidth_limit_kbytes"]=bandwidth_limit_kbytes
	rule_info["assumed_kps"]=assumed_kps
	rule_info["ras_id"]=ras_id
	return charge_types.getChargeRuleObjForType("Internet",rule_info,charge_obj,day_of_week_container,ports)


    def __checkRuleConflict(self,charge_obj,rule_obj,ignore_rule_ids=[]):
	"""
	    check if rule_obj conflicts with any other rule in charge charge_obj
	    raise a generalException if there's a conflict
	"""
	charge_obj.checkConflict(rule_obj,ignore_rule_ids)


    def __chargeRuleTimesCheck(self,start_time,end_time,day_of_weeks):
	"""
	    Check rule times and convert them the way ibs needed them to insert to IBS
	    day_of_weeks(list): list of day of week strings
	"""
	try:
	    start_time=Time(start_time)
	except GeneralException,e:
	    raise GeneralException(errorText("CHARGES","INVALID_RULE_START_TIME")%e)

	try:
	    end_time=Time(end_time)
	except GeneralException,e:
	    raise GeneralException(errorText("CHARGES","INVALID_RULE_END_TIME")%e)

	if start_time >= end_time:
	    raise GeneralException(errorText("CHARGES","RULE_END_LESS_THAN_START"))
    
	try:
	    dows=map(DayOfWeekString,day_of_weeks)
	except GeneralException,e:
	    raise GeneralException(errorText("CHARGES","INVALID_DAY_OF_WEEK")%e)

	return (start_time,end_time,dows)

	
    def __chargeRuleCheckInput(self,charge_name,charge_type,ras_id,ports):
	"""
	    check ChargeRule inputs and raise an exception on bad input
	"""
	charge_obj=charge_main.getLoader().getChargeByName(charge_name)
	if charge_obj.getType()!=charge_type:
	    raise GeneralException(errorText("CHARGES","ANOTHER_CHARGE_TYPE_REQUIRED")%charge_type)
	if ras_id!=charge_rule.ChargeRule.ALL:
	    ras_main.getLoader().checkRasID(ras_id)
	    if len(ports)==0:
		raise GeneralException(errorText("CHARGES","NO_PORT_SELECTED"))

    

#######################################################3
    def updateInternetChargeRule(self,charge_name,charge_rule_id,start_time,end_time,day_of_weeks,cpm,cpk,\
		    		   assumed_kps,bandwidth_limit_kbytes,ras_id,ports):
	"""
	    add a charge rule to charge with id "charge_id" and reload the charge
	    it will add charge_rule and it's ports to db too
	"""
	start_time,end_time,day_of_weeks=self.__chargeRuleTimesCheck(start_time,end_time,day_of_weeks)
	charge_rule_id=self.__updateInternetChargeRuleCheckInput(charge_name,charge_rule_id,start_time,end_time,day_of_weeks,cpm,cpk,\
		    		   assumed_kps,bandwidth_limit_kbytes,ras_id,ports)
	
	charge_obj=charge_main.getLoader().getChargeByName(charge_name)
	day_of_weeks_container=self.__createDayOfWeekContainer(day_of_weeks)
	rule_obj=self.__createInternetChargeRuleObject(charge_obj,start_time,end_time,day_of_weeks_container,\
				cpm,cpk,assumed_kps,bandwidth_limit_kbytes,ras_id,ports,charge_rule_id)
        self.__checkRuleConflict(charge_obj,rule_obj,[charge_rule_id])
        self.__updateInternetChargeRuleDB(rule_obj)
        charge_main.getLoader().loadCharge(charge_obj.getChargeID())


    def __updateInternetChargeRuleCheckInput(self,charge_name,charge_rule_id,start_time,end_time,day_of_weeks,cpm,cpk,\
		    		   assumed_kps,bandwidth_limit_kbytes,ras_id,ports):
	self.__internetChargeRuleCheckInput(charge_name,cpm,cpk,assumed_kps,bandwidth_limit_kbytes,ras_id,ports)
	try:
	    charge_rule_id=int(charge_rule_id)
	except:
	    raise GeneralException(errorText("CHARGES","INVALID_CHARGE_RULE_ID")%charge_rule_id)

	self.__checkChargeRuleInCharge(charge_rule_id,charge_name)
	
	return charge_rule_id

    def __updateInternetChargeRuleDB(self,rule_obj):
	"""
	    add rule_obj properties to DB
	"""
	query=self.__updateInternetChargeRuleAndPortsQuery(rule_obj)
	db_main.getHandle().transactionQuery(query)

    def __updateInternetChargeRuleAndPortsQuery(self,rule_obj):
	"""
	    return query for inserting "rule_obj" with id "charge_rule_id"
	"""
	return self.__updateInternetChargeRuleQuery(rule_obj) + \
	       self.__updateChargeRulePortsAndDowsQuery(rule_obj)
	
    def __updateChargeRulePortsAndDowsQuery(self,rule_obj):
	return self.__delChargeRulePortsQuery(rule_obj.getRuleID()) + \
	       self.__delChargeRuleDowsQuery(rule_obj.getRuleID()) + \
	       self.__addChargeRulePortsQuery(rule_obj.getPorts(),rule_obj.getRuleID()) + \
	       self.__addChargeRuleDowsQuery(rule_obj.getDows(),rule_obj.getRuleID())
	       

    def __updateInternetChargeRuleQuery(self,rule_obj):
	"""
	    return query for inserting rule_obj properties into charge_rules table
	"""
	if rule_obj.getRasID() == charge_rule.ChargeRule.ALL:
	    ras_id="NULL"
	else:
	    ras_id=rule_obj.getRasID()
	    
	return ibs_db.createUpdateQuery("internet_charge_rules",{"start_time":dbText(rule_obj.start_time),
							"end_time":dbText(rule_obj.end_time),
							"cpm":float(rule_obj.cpm),
							"cpk":float(rule_obj.cpk),
							"assumed_kps":integer(rule_obj.assumed_kps),
							"bandwidth_limit_kbytes":integer(rule_obj.bandwidth_limit),
							"ras_id":ras_id
							},"charge_rule_id=%s"%rule_obj.getRuleID())



    def __delChargeRulePortsQuery(self,rule_id):
	return ibs_db.createDeleteQuery("charge_rule_ports","charge_rule_id=%s"%rule_id)
	
	
    def __delChargeRuleDowsQuery(self,rule_id):
	return ibs_db.createDeleteQuery("charge_rule_day_of_weeks","charge_rule_id=%s"%rule_id)
	
######################
    def delChargeRule(self,charge_rule_id,charge_name):
	"""
	    delete charge_rule with id "charge_rule_id" from charge with name "charge_name"
	    it will delete all of charge_rule ports too
	"""
	self.__delChargeRuleCheckInput(charge_rule_id,charge_name)
	charge_obj=charge_main.getLoader().getChargeByName(charge_name)
	self.__delChargeRuleFromDB(charge_rule_id,charge_obj)
	charge_main.getLoader().loadCharge(charge_obj.getChargeID())


    def __delChargeRuleCheckInput(self,charge_rule_id,charge_name):
	"""
	    check delChargeRule Inputs
	    raise a generalExcetpion on bad input
	"""
	self.__checkChargeRuleInCharge(charge_rule_id,charge_name)

    def __delChargeRuleFromDB(self,charge_rule_id,charge_obj):
	"""
	    delete charge_rule with id "charge_rule_id" from db
	"""
	query=self.__delChargeRulePortsQuery(charge_rule_id)+ \
	     self.__delChargeRuleDowsQuery(charge_rule_id) 

	if charge_obj.getType()=="Internet":
	    query+=self.__delInternetChargeRuleQuery(charge_rule_id)
	
	db_main.getHandle().transactionQuery(query)

    def __delInternetChargeRuleQuery(self,charge_rule_id):
	"""
	    return query needed to delete rule only from charge_rules table
	    it won't delete ports
	"""
	return ibs_db.createDeleteQuery("internet_charge_rules","charge_rule_id=%s"%charge_rule_id)

######################UNCHECKED
    def delCharge(self,charge_id):
	"""
	    delete a charge from both db and list of active charges
	"""
	self.__delChargeCheckInput(charge_id)
	self.__delChargeFromDB(charge_id)
	charge_main.getLoader().unloadCharge(charge_id)
    
    def __delChargeCheckInput(self,charge_id):
	"""
	    check del Charge inputs
	    raise exception on bad input
	"""
	charge_main.getLoader().checkChargeID(charge_id)    

    def __delChargeFromDB(self,charge_id):
	"""
	    --completely-- delete charge with id "charge_id" from db, also delete
	    it's rules and ports
	"""
	charge_obj=charge_main.getLoader()[charge_id]
	query=""
	for charge_rule_id in charge_obj.getRules():
	    query+=self.rule_loader.delRuleAndPortsQuery(charge_rule_id)
	
	query+=self.__delChargeQuery(charge_id)
	db_main.getHandle().transactionQuery(query)
	
	
    def __delChargeQuery(self,charge_id):
	"""
	    return query to delete the charge itself from charges table
	    it won't return query for deleting rules
	"""
	return ibs_db.createDeleteQuery("internet_charge_rules","charge_id=%s"%charge_id)



	