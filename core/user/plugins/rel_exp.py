from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_holder import AttrHolder
from core.ibs_exceptions import *
from core.lib.date import *
from core.errors import errorText
import time

attr_handler_name="rel exp date"

def init():
    user_main.getUserPluginManager().register("rel_exp_date",RelExpDate)
    user_main.getAttributeManager().registerHandler(RelExpDateAttrHandler(),["rel_exp_date","rel_exp_date_unit"],["rel_exp_date"],["rel_exp_date"])

class RelExpDate(user_plugin.UserPlugin):#XXX TO CHECK
    def __init__(self,user_obj):
	user_plugin.UserPlugin(self,user_obj)
	if self.getAttr("rel_exp_date"):
	    self.has_rel_exp=True
	    self.__checkFirstLogin()
	    self.rel_exp_date=int(self.user_obj.getAttr("rel_exp_date"))*3600
	else:
	    self.has_rel_exp=False

    def __isRelExpired(self):
	"""
	    check if user has relative expiration date has reached
	"""
	return self.__getRelExpireTime()<time.time()

    def __getRelExpireTime(self):
	"""
	    return absolout epoch time of relative expiration date
	"""
	return self.first_login_epoch+self.rel_exp_date

    def __checkFirstLogin(self):
	"""
	    check if it's first time the users log in
	    if it's first time, then update dirst_login in db
	"""
	if self.user_obj.getAttr("first_login")==None:
	    user_manager.getUserManager().updateAttr("first_login",int(time.time()))
	    self.first_login_epoch=time.time()
	else:
	    self.first_login_epoch=int(self.user_obj.getAttr("first_login"))

    def login(self,*args):
	if self.has_rel_exp and self.__isRelExpired():
	    raise loginException(errorText("NORMAL_USER_LOGIN","REL_EXP_DATE_REACHED"))

    def canStayOnline(self):
	if not self.has_rel_exp:
	    return defs.MAXLONG

	next_event=self.__getRelExpireTime()-time.time()
	if next_event<=0:
	    return (0,self.user_obj.__createKillAllInstancesDic())
	else:
	    return (next_event,{})

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

	self.useGenerateQuery({"rel_exp_date":self.rel_date_obj.getDBDate()})

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
		

class RelExpAttrHolder(AttrHolder):
    def __init__(self,rel_exp_hours):
	self.rel_exp_hours=rel_exp_hours
	self.rel_date_obj=RelativeDate(rel_exp_hours,"Hours")

    def getParsedDic(self):
	(rel_exp_date,unit)=self.rel_date_obj.getFormattedDate()
	return {"rel_exp_date":rel_exp_date,"rel_exp_date_unit":unit}

class RelExpDateAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(RelExpAttrUpdater,["rel_exp_date","rel_exp_date_unit"])
	self.registerAttrHolderClass(RelExpAttrHolder,["rel_exp_date"])
