from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_holder import AttrHolder
from core.user.attr_searcher import AttrSearcher
from core.ibs_exceptions import *
from core.lib.date import *
from core.errors import errorText
import time

attr_handler_name="rel exp date"

def init():
    user_main.getUserPluginManager().register("rel_exp_date",RelExpDate)
    user_main.getAttributeManager().registerHandler(RelExpDateAttrHandler(),["rel_exp_date"],["rel_exp_date"],["rel_exp_date","first_login"])

class RelExpDate(user_plugin.AttrCheckUserPlugin):
    def __init__(self,user_obj):
	user_plugin.AttrCheckUserPlugin.__init__(self,user_obj,"rel_exp_date")
	self.__initValues(True)

    def __initValues(self,init):
	if self.hasAttr():
	    self.commit_first_login=False
	    if self.__isFirstLogin():
		self.commit_first_login=True
		if init:
		    self.first_login=time.time()
		else:
		    self.first_login=self.user_obj.getInstanceInfo(1)["auth_ras_msg"].getTime()
	    else:
		self.first_login=long(self.user_obj.getUserAttrs()["first_login"])

	self.rel_exp_date_time=self.__calcRelExpDateTime(self.first_login,long(self.user_obj.getUserAttrs()["rel_exp_date"]))

    def __isFirstLogin(self):
	return not self.user_obj.getUserAttrs().hasAttr("first_login")
	    
    def __calcRelExpDateTime(self,first_login,rel_exp_date_val):
	return first_login+rel_exp_date_val

    def __isRelExpired(self):
	"""
	    check if user has relative expiration date has reached
	"""
	return self.rel_exp_date_time<=time.time()


    def s_login(self,ras_msg):
	if self.__isRelExpired():
	    raise LoginException(errorText("NORMAL_USER_LOGIN","REL_EXP_DATE_REACHED"))

    def s_canStayOnline(self):
	result=self.createCanStayOnlineResult()
	if self.__isRelExpired():
	    result.setKillForAllInstances(errorText("NORMAL_USER_LOGIN","REL_EXP_DATE_REACHED",False),user_obj.instances)
	else:
	    result.newRemainingTime(time.time()-self.rel_exp_date_time)
	return result

    def s_commit(self):
	query=""
	if self.commit_first_login:
	    query+=user_main.getActionsManager().insertUserAttrQuery(user_obj.getUserID(),
								    "first_login",
								    self.first_login
								    )
	    self.commit_first_login=False
	return query
	
    def _reload(self):
	user_plugin.AttrCheckUserPlugin.__init__(self)
	self.__initValues(False)
    
class RelExpAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)
	
    def changeInit(self,rel_exp_date,rel_exp_date_unit):
	self.rel_exp_date=rel_exp_date
	self.rel_exp_date_unit=rel_exp_date_unit
	self.rel_date_obj=RelativeDate(rel_exp_date,rel_exp_date_unit)

	try:
	    self.rel_date_obj.check()
	except GeneralException:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_REL_EXP_DATE"))

	self.useGenerateQuery(self.__CreateUpdateAttrsDic())
		
    def __createUpdateAttrsDic(self):
	return {"rel_exp_date":self.rel_date_obj.getDBDate()}

    def userChangeQuery(self,ibs_query,src,action,**args):
	"""
	    unused
	"""
	new_args=args.copy()
	for user_id in args["users"]:
	    loaded_user=args["users"][user_id]
	    new_args["attr_updater_attrs"]=self.__createUpdateAttrsDic()
	    new_args["users"]={user_id:loaded_user}
	    if loaded_user.hasAttr("first_login"):
	        new_args["attr_updater_attrs"]["rel_exp_date_time"]=loaded_user.getUserAttrs()["first_login"]+self.rel_date_obj.getDateHours()*3600
	    self.generateQuery(ibs_query,src,action,**new_args)


    def deleteInit(self):
	self.useGenerateQuery(["rel_exp_date"])

class RelExpAttrSearcher(AttrSearcher):
    def run(self):
	search_helper=self.getSearchHelper()
	if search_helper.hasCondFor("rel_exp_date","rel_exp_date_unit","rel_exp_date_op"):
	    checkltgtOperator(search_helper.getCondValue("rel_exp_date_op"))
	    rel_date_obj=RelativeDate(search_helper.getCondValue("rel_exp_date"),
				      search_helper.getCondValue("rel_exp_date_unit"))
	    for table in self.getUserAndGroupAttrsTable():
		table.search("rel_exp_date",(rel_date_obj.getDBDate(),),search_helper.getCondValue("rel_exp_date_op"))

class RelExpAttrHolder(AttrHolder):
    def __init__(self,rel_exp_hours):
	self.rel_exp_hours=rel_exp_hours
	self.rel_date_obj=RelativeDate(rel_exp_hours,"Hours")

    def getParsedDic(self):
	(rel_exp_date,unit)=self.rel_date_obj.getFormattedDate()
	return {"rel_exp_date":rel_exp_date,"rel_exp_date_unit":unit}


class FirstLoginAttrHolder(AttrHolder):
    def __init__(self,first_login,rel_exp_date_time):
	self.first_login=AbsDateFromEpoch(first_login)
	self.rel_exp_date_time=AbsDateFromEpoch(rel_exp_date_time)

    def getParsedDic(self):
	return ({"first_login":self.first_login.getDate(self.date_type),
		 "rel_exp_date_time":self.rel_exp_date_time.getDate(self.date_type)})

class RelExpDateAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(RelExpAttrUpdater,["rel_exp_date","rel_exp_date_unit"])
	self.registerAttrHolderClass(RelExpAttrHolder,["rel_exp_date"])
	self.registerAttrHolderClass(FirstLoginAttrHolder,["first_login","rel_exp_date_time"])
	self.registerAttrSearcherClass(RelExpAttrSearcher)
