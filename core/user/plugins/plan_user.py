from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_searcher import AttrSearcher
from core.user.attr_holder import AttrHolder
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *
from core.lib.multi_strs import MultiStr
from core.lib.password_lib import Password,getPasswords
from core.lib import iplib,maclib
from core.ras import ras_main,msgs
from core.db import ibs_db
import itertools,string

attr_handler_name="plan user"
def init():
    user_main.getAttributeManager().registerHandler(PersistentLanUserAttrHandler(),["persistent_lan_mac"],["persistent_lan_mac"],["persistent_lan_ras_id"])

class PersistentLanUserAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,attr_handler_name)
	self.updated_users=[]
	self.inserted_users=[]
	self.deleted_users=[]

    def changeInit(self,mac,ip,ras_ip):
	"""
	    mac(str): mac address of user
	    ip(str): ip/mask address of user
	    ras_ip(str): ip of user, user intends to use
	"""
	self.registerQuery("user","change",self.changeQuery,[])
	self.mac=map(string.upper,MultiStr(mac))
	self.ip=MultiStr(ip)
	self.ras_ip=MultiStr(ras_ip)
	

    def deleteInit(self):
	self.registerQuery("user","delete",self.deleteQuery,[])

    def checkInput(self,src,action,dargs):
	map(dargs["admin_obj"].canChangeNormalAttrs,dargs["users"].itervalues())
    
    def __checkMacExistence(self,macs,users):
	def macNotChanged(_tuple):
	    mac,loaded_user=_tuple
	    return not ( loaded_user.hasAttr("persistent_lan_mac") and mac==loaded_user.getUserAttrs()["persistent_lan_mac"].upper())
	
	macs=filter(macNotChanged,itertools.izip(macs,users.itervalues()))

	exists=user_main.getActionManager().planMacExists([m[0] for m in macs])
	if len(exists):
	    raise GeneralException(errorText("USER_ACTIONS","PERSISTENT_LAN_MAC_EXISTS")%",".join(exists))

    def __checkIP(self):
	for ip in self.ip:
	    if not iplib.checkIPAddr(ip):
		raise GeneralException(errorText("GENERAL","INVALID_IP_ADDRESS")%ip)


    def __checkMac(self):
	for mac in self.mac:
	    if not maclib.checkMacAddress(mac):
		raise GeneralException(errorText("GENERAL","INVALID_MAC_ADDRESS")%mac)
    
    def __checkRasIP(self):
	ras_objs=map(lambda ras_ip:ras_main.getLoader().getRasByIP(ras_ip),self.ras_ip)
	for ras_obj in ras_objs:
	    if ras_obj.getType()!="Persistent Lan":
		raise GeneralException(errorText("USER_ACTIONS","RAS_IS_NOT_PERSISTENT_LAN")%ras_obj.getRasIP())

    def __changeCheckInput(self,users,admin_obj):
	if len(self.mac)!=len(users):
	    raise GeneralException(errorText("USER_ACTIONS","PLAN_MAC_COUNT_NOT_MATCH")%(len(users),len(self.mac)))
	
	self.__checkRasIP()
	self.__checkIP()
	self.__checkMac()
	self.__checkMacExistence(self.mac,users)

    def changeQuery(self,ibs_query,src,action,**args):
	admin_obj=args["admin_obj"]
	users=args["users"]
	
	self.__changeCheckInput(users,admin_obj)
	
	i=0
	for user_id in users:
	    loaded_user=users[user_id]
	    if loaded_user.hasAttr("persistent_lan_mac"):
		ras_id=ras_main.getLoader().getRasByIP(self.ras_ip[i]).getRasID()
		ibs_query+=self.__updatePlanUserAttrsQuery(user_id,
							   self.mac[i],
							   self.ip[i],
							   ras_id
							   )
		self.updated_users.append(( (ras_id,user_id,self.mac[i],self.ip[i]),
					   (user_id,
					    loaded_user.getUserAttrs()["persistent_lan_mac"],
					    loaded_user.getUserAttrs()["persistent_lan_ras_id"]
					    ) ))
	    else:
		ras_id=ras_main.getLoader().getRasByIP(self.ras_ip[i]).getRasID()
		ibs_query+=self.__insertPlanUserAttrsQuery(user_id,
							   self.mac[i],
							   self.ip[i],
							   ras_id
							   )
		self.inserted_users.append((ras_id,user_id,self.mac[i],self.ip[i]))

	    i+=1

	return ibs_query

    def deleteQuery(self,ibs_query,src,action,**args):
	users=args["users"]

	for user_id in users:
	    loaded_user=users[user_id]
	    ibs_query+=self.__deletePlanUserAttrsQuery(user_id)
	    if loaded_user.userHasAttr("persistent_lan_mac"):
	        self.deleted_users.append((user_id,loaded_user.getUserAttrs()["persistent_lan_mac"],loaded_user.getUserAttrs()["persistent_lan_ras_id"]))
	return ibs_query

    def __deletePlanUserAttrsQuery(self,user_id):
	return ibs_db.createDeleteQuery("persistent_lan_users","user_id=%s"%user_id)

    def __updatePlanUserAttrsQuery(self,user_id,mac,ip,ras_id):
	return ibs_db.createUpdateQuery("persistent_lan_users",{"persistent_lan_mac":dbText(mac),
								"persistent_lan_ip":dbText(ip),
								"persistent_lan_ras_id":ras_id},
								"user_id=%s"%user_id)
								
    def __insertPlanUserAttrsQuery(self,user_id,mac,ip,ras_id):
	return ibs_db.createInsertQuery("persistent_lan_users",{"persistent_lan_mac":dbText(mac),
								"persistent_lan_ip":dbText(ip),
								"persistent_lan_ras_id":ras_id,
								"user_id":user_id})

    def postUpdate(self,src,action):
	for user_id,mac,ras_id in self.deleted_users:
	    user_msg=self.__createRemoveUserMsg(user_id,mac,ras_id)
	    user_msg.send()

	for ras_id,user_id,mac,ip in self.inserted_users:
	    user_msg=self.__createLoginUserMsg(user_id,mac,ip,ras_id)
	    user_msg.send()

	for new_info,old_info in self.updated_users:
	    ras_id,user_id,mac,ip=new_info
	    user_id,old_mac,old_ras_id=old_info
	    user_msg=self.__createRemoveUserMsg(user_id,old_mac,old_ras_id)
	    user_msg.send()
	    user_msg=self.__createLoginUserMsg(user_id,mac,ip,ras_id)
	    user_msg.send()
	    

    def __createLoginUserMsg(self,user_id,mac,ip,ras_id):
	user_msg=msgs.UserMsg()
	user_msg.setAction("PLAN_LOGIN_NEW_USER")
	user_msg["mac"]=mac
	user_msg["user_id"]=user_id
	user_msg["ras_id"]=ras_id
	user_msg["ip"]=ip
	return user_msg

    def __createRemoveUserMsg(self,user_id,mac,ras_id):
	user_msg=msgs.UserMsg()
	user_msg.setAction("PLAN_REMOVE_USER")
	user_msg["mac"]=mac
	user_msg["user_id"]=user_id
	user_msg["ras_id"]=ras_id
	return user_msg

class PersistentLanUserAttrSearcher(AttrSearcher):
    def run(self):
	plan_table=self.getSearchHelper().getTable("persistent_lan_users")
	plan_table.exactSearch(self.getSearchHelper(),
			           "persistent_lan_mac",
				   "persistent_lan_mac",
				   MultiStr)

	plan_table.exactSearch(self.getSearchHelper(),
			           "persistent_lan_ip",
				   "persistent_lan_ip",
				   MultiStr)

	plan_table.exactSearch(self.getSearchHelper(),
			           "persistent_lan_ras_ip",
				   "persistent_lan_ras_id",
				   lambda ras_ip:ras_main.getLoader().getRasByIP(ras_ip).getRasID())


class PersistentLanUserAttrHolder(AttrHolder):
    def __init__(self,ras_id):
	self.ras_id=int(ras_id)

    def getParsedDic(self):
	return {"persistent_lan_ras_ip":ras_main.getLoader().getRasByID(self.ras_id).getRasIP()}

class PersistentLanUserAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,attr_handler_name)
	self.registerAttrUpdaterClass(PersistentLanUserAttrUpdater,
				      ["persistent_lan_mac",
				       "persistent_lan_ip",
				       "persistent_lan_ras_ip"
				      ])
	self.registerAttrSearcherClass(PersistentLanUserAttrSearcher)
	self.registerAttrHolderClass(PersistentLanUserAttrHolder,["persistent_lan_ras_id"])
	