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

class RelExpDate(user_plugin.UserPlugin):
    def __init__(self,user_obj):
	user_plugin.UserPlugin.__init__(self,user_obj)
	self.__initFirstLogin()
	self.__initValues()

    def hasAttr(self):
	return self.user_obj.getUserAttrs().hasAttr("rel_exp_date")

    def __initFirstLogin(self):
	self.commit_first_login=False
	if self.__isFirstLogin():
	    self.commit_first_login=True
	    self.first_login=long(time.time())
	else:
	    self.first_login=long(self.user_obj.getUserAttrs()["first_login"])

    def __initValues(self):
	if self.hasAttr():
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

    def login(self,ras_msg):
	if self.hasAttr() and self.__isRelExpired():
	    raise LoginException(errorText("USER_LOGIN","REL_EXP_DATE_REACHED"))

    def canStayOnline(self):
	if self.hasAttr():	
	    result=self.createCanStayOnlineResult()
	    if self.__isRelExpired():
		result.setKillForAllInstances(errorText("USER_LOGIN","REL_EXP_DATE_REACHED",False),self.user_obj.instances)
	    else:
		result.newRemainingTime(self.rel_exp_date_time-time.time())
    	    return result

    def commit(self):
	query=""
	if self.commit_first_login:
	    query+=user_main.getActionManager().insertUserAttrQuery(self.user_obj.getUserID(),
								    "first_login",
								    self.first_login
								    )
	    self.commit_first_login=False
	return query
	
    def _reload(self):
	self.__initValues()
    
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

	self.useGenerateQuery(self.__createUpdateAttrsDic())
		
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
		table.search("rel_exp_date",(rel_date_obj.getDBDate(),),search_helper.getCondValue("rel_exp_date_op"),"integer")

class RelExpAttrHolder(AttrHolder):
    def __init__(self,rel_exp):
	self.rel_exp=rel_exp
	self.rel_date_obj=RelativeDate(rel_exp,"Seconds")

    def getParsedDic(self):
	(rel_exp_date,unit)=self.rel_date_obj.getFormattedDate()
	return {"rel_exp_date":rel_exp_date,"rel_exp_date_unit":unit}


class FirstLoginAttrHolder(AttrHolder):
    def __init__(self,first_login):
	self.first_login=AbsDateFromEpoch(long(first_login))

    def getParsedDic(self):
	return ({"first_login":self.first_login.getDate(self.date_type)})

class RelExpDateAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(RelExpAttrUpdater,["rel_exp_date","rel_exp_date_unit"])
	self.registerAttrHolderClass(RelExpAttrHolder,["rel_exp_date"])
	self.registerAttrHolderClass(FirstLoginAttrHolder,["first_login"])
	self.registerAttrSearcherClass(RelExpAttrSearcher)
