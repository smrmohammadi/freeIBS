from core.ibs_exceptions import *
from core.lib.general import *
from core.charge import charge_main
from core.db import ibs_db,db_main
from core.db.ibs_query import IBSQuery
from core.errors import errorText
from core.admin import admin_main
from core.lib import password_lib,iplib,report_lib
from core.group import group_main
from core.user import user_main
from core.ras import ras_main
import re

class UserActions:
#######################################################
    def getLoadedUsersByUserID(self,user_ids):
	"""
	    return a list of LoadedUser instances for users with ids "user_ids"
	"""
	user_ids=map(lambda x:to_int(x,"user id"),user_ids)
	loaded_users=map(user_main.getUserPool().getUserByID,user_ids)
	return loaded_users

    def getUserInfoByUserID(self,user_id,date_type):
	"""
	    return a list of user info dics with user_id in multi string user_id
	    return dic is in format {user_id=>user_info dic}
	"""
	loaded_users=self.getLoadedUsersByUserID(user_id)
	return self.getUserInfosFromLoadedUsers(loaded_users,date_type)
	
#######################################################
    def getLoadedUsersByNormalUsername(self,normal_usernames):
	"""
	    return a list of LoadedUser instances for users with normal_usernames "normal_usernames"
	"""
	loaded_users=map(user_main.getUserPool().getUserByNormalUsername,normal_usernames)
	return loaded_users
    
    def getUserInfoByNormalUsername(self,normal_username,date_type):
	"""
	    return a list of user info dics with normal_username in multi string user_id
	    return dic is in format {user_id=>user_info dic}
	"""
	loaded_users=self.getLoadedUsersByUsername(normal_username)
	return self.getUserInfosFromLoadedUsers(loaded_users,date_type)

########################################################

    def insertUserAttrQuery(self,user_id,attr_name,attr_value):
	"""
	    XXX:change to use stored procedures
	"""
	return ibs_db.createInsertQuery("user_attrs",{"user_id":user_id,
						      "attr_name":dbText(attr_name),
						      "attr_value":dbText(attr_value)}
					)

    def updateUserAttrQuery(self,user_id,attr_name,attr_value):
	"""
	    XXX:change to use stored procedures
	"""
	return ibs_db.createUpdateQuery("user_attrs",{"attr_value":dbText(attr_value)}
						    ,"attr_name=%s and user_id=%s"%
						    (dbText(attr_name),user_id)
					)

    def deleteUserAttrQuery(self,user_id,attr_name):
	"""
	    XXX:change to use stored procedures
	"""
	return ibs_db.createDeleteQuery("user_attrs","user_id=%s and attr_name=%s"%
						      (user_id,dbText(attr_name))
					)


######################################################
    def _checkNormalUsernameChars(self,username):
	if not len(username) or username[0] not in string.letters:
	    return False
        if re.search("[^A-Za-z0-9_\-\.]",username) != None:
	    return False
	return True
	    
    def checkNormalUsernameChars(self,username):
        if not self._checkNormalUsernameChars(username):
	    raise GeneralException(errorText("USER_ACTIONS","BAD_NORMAL_USERNAME"))
####################################################
    def addNewUsers(self,_count,credit,owner_name,creator_name,group_name,remote_address,credit_change_comment):
	self.__addNewUsersCheckInput(_count,credit,owner_name,creator_name,group_name,remote_address,credit_change_comment)
	admin_consumed_credit=credit*_count
	ibs_query=IBSQuery()
	ibs_query+=admin_main.getActionManager().consumeDeposit(creator_name,admin_consumed_credit)
	try:
	    user_ids=self.addNewUsersQuery(_count,credit,owner_name,group_name,ibs_query)
	    creator_admin_obj=admin_main.getLoader().getAdminByName(creator_name)
    	    ibs_query+=user_main.getCreditChangeLogActions().logCreditChangeQuery("ADD_USER",creator_admin_obj.getAdminID(),user_ids,credit,\
					admin_consumed_credit,remote_address,credit_change_comment)
	    ibs_query.runQuery()
	    return user_ids
	except:
	    admin_main.getActionManager().consumeDeposit(creator_name,-1*admin_consumed_credit,False) #re-add deposit to admin
	    raise


    def __addNewUsersCheckInput(self,_count,credit,owner_name,creator_name,group_name,remote_address,credit_change_comment):
	if not isInt(_count) or _count<=0:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_USER_COUNT")%_count)
	
	if not isFloat(credit):
	    raise GeneralException(errorText("USER_ACTIONS","CREDIT_NOT_FLOAT"))

	if credit<0:
	    raise GeneralException(errorText("USER_ACTIONS","CREDIT_MUST_BE_POSITIVE"))
	
	admin_main.getLoader().checkAdminName(owner_name)
	admin_main.getLoader().checkAdminName(creator_name)
	group_main.getLoader().checkGroupName(group_name)

    def addNewUsersQuery(self,_count,credit,owner_name,group_name,ibs_query):
	"""
	    _count(integer): count of users
	    owner_name(string): name of owner admin
	    credit(float): amount of credit users will have, 
	    group_name(string): name of group string
	    ibs_query(IBSQuery instance): IBSQuery instance we'll add query to
	    
	    XXX: add this: if credit is an empty string, group initial_credit
		is used, or an exception is raised if there's no initial_credit for user
	    return a list of user ids of newly added users
	"""

	owner_admin_obj=admin_main.getLoader().getAdminByName(owner_name)
	group_obj=group_main.getLoader().getGroupByName(group_name)
	user_ids=self.__generateUserIDs(_count)
	self.__insertBasicUsersQueries(_count,user_ids,credit,owner_admin_obj.getAdminID(),group_obj.getGroupID(),ibs_query)
	return user_ids

    def __insertBasicUsersQueries(self,_count,user_ids,credit,owner_id,group_id,ibs_query):
	"""
	    add query to ibs_query for inserting "_count" of users with user ids in "user_ids" into users table
	"""
	for user_id in user_ids:
	    ibs_query+=self.__insertBasicUserQuery(user_id,credit,owner_id,group_id)

    
    def __insertBasicUserQuery(self,user_id,credit,owner_id,group_id):
	"""
	    XXX : Change this function to use SQL Stored Procedures
	"""
	return ibs_db.createInsertQuery("users",{"user_id":user_id,
						 "credit":credit,
						 "owner_id":owner_id,
						 "group_id":group_id})
	
    def __generateUserIDs(self,_count):
	"""
	    generate "_count" number of user ids and return them in a list
	    _count(integer): count of user ids that will be generated
	"""
	return map(lambda x:self.__getNewUserID(),range(_count))
	
    def __getNewUserID(self):
	"""
	    return a new unique user_id from
	"""
	return db_main.getHandle().seqNextVal("users_user_id_seq")
######################################################
    def changeCredit(self,user_ids,credit,changer_admin_name,remote_address,credit_change_comment,loaded_users):
	"""
	    change credit of user(s) with user_id in "user_ids"
	    user_ids(iterable object, list or multi_str): user_ids that credit will be changed
	    credit(float): amount of credit change, can be negative
	    changer_admin_name(string): username of admin that initiate the change. He should have enough deposit
	    remote_address(string): changer client ip address 
	    credit_change_comment(string): comment that will be stored in credit change log
	    loaded_users(LoadedUser instance): list of loaded users of "user_ids"
	"""
	self.__changeCreditCheckInput(user_ids,credit,changer_admin_name,remote_address,credit_change_comment,loaded_users)
	admin_consumed_credit=credit*len(user_ids)
	ibs_query=IBSQuery()
    	ibs_query+=admin_main.getActionManager().consumeDeposit(changer_admin_name,admin_consumed_credit)
	try:
	    changer_admin_obj=admin_main.getLoader().getAdminByName(changer_admin_name)
	    ibs_query+=self.__changeCreditQuery(user_ids,credit)
    	    ibs_query+=user_main.getCreditChangeLogActions().logCreditChangeQuery("CHANGE_CREDIT",changer_admin_obj.getAdminID(),user_ids,credit,\
					admin_consumed_credit,remote_address,credit_change_comment)
	    ibs_query.runQuery()
	except:
	    admin_main.getActionManager().consumeDeposit(changer_admin_name,-1*admin_consumed_credit,False) #re-add deposit to admin
	    raise
	self.__broadcastChange(user_ids)

    def __changeCreditCheckInput(self,user_ids,credit,changer_admin_name,remote_address,credit_change_comment,loaded_users):
	if not isFloat(credit):
	    raise GeneralException(errorText("USER_ACTIONS","CREDIT_NOT_FLOAT"))

	admin_main.getLoader().checkAdminName(changer_admin_name)

	if not iplib.checkIPAddr(remote_address):
	    raise GeneralException(errorText("GENERAL","INVALID_IP_ADDRESS")%ip_addr)

	if len(user_ids)==0:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_USER_COUNT")%0)

	for loaded_user in loaded_users:
	    if credit<0 and loaded_user.getBasicUser().getCredit()+credit<0:
		raise GeneralException(errorText("USER_ACTIONS","CAN_NOT_NEGATE_CREDIT")%(loaded_user.getUserID(),loaded_user.getBasicUser().getCredit()))
	    
    def __changeCreditQuery(self,user_ids,credit):
	where_clause=" or ".join(map(lambda user_id:"user_id = %s"%user_id,user_ids))
	return ibs_db.createUpdateQuery("users",{"credit":"credit+%s"%credit},where_clause)

######################################################
    def updateUserAttrs(self,loaded_users,admin_obj,attrs,to_del_attrs):
	"""
	    loaded_users(list of LoadedUser instances):
	    
	"""
	self.__updateUserAttrsCheckInput(loaded_users,admin_obj,attrs,to_del_attrs)
	changed_attr_updaters=user_main.getAttributeManager().getAttrUpdaters(attrs,"change")
	deleted_attr_updaters=user_main.getAttributeManager().getAttrUpdaters(to_del_attrs,"delete")
	users=self.__createUsersDic(loaded_users)
	ibs_query=IBSQuery()
	ibs_query=self.__getChangedQuery(ibs_query,users,admin_obj,changed_attr_updaters)
	ibs_query=self.__getDeletedQuery(ibs_query,users,admin_obj,deleted_attr_updaters)
	ibs_query.runQuery()
	self.__broadcastChange(users.keys())
	self.__callPostUpdates(changed_attr_updaters,deleted_attr_updaters)

    def __updateUserAttrsCheckInput(self,loaded_users,admin_obj,attrs,to_del_attrs):
	pass #nothing to check here for now, everything is checked or will be checked
    
    def __createUsersDic(self,loaded_users):
	"""
	    create a dic of {user_id:loaded_user,user_id:loaded_user,...} from loaded_users
	"""
	users={}
	for loaded_user in loaded_users:
	    users[loaded_user.getUserID()]=loaded_user
	return users

    def __getChangedQuery(self,ibs_query,users,admin_obj,changed_attr_updaters):
	return changed_attr_updaters.getQuery(ibs_query,"user","change",{"users":users,
							                 "admin_obj":admin_obj})
	
    def __getDeletedQuery(self,ibs_query,users,admin_obj,deleted_attr_updaters):
	return deleted_attr_updaters.getQuery(ibs_query,"user","delete",{"users":users,
							                 "admin_obj":admin_obj})

    def __callPostUpdates(self,changed_attr_updaters,deleted_attr_updaters):
	changed_attr_updaters.postUpdate("user","change")
	deleted_attr_updaters.postUpdate("user","delete")

    def __broadcastChange(self,user_ids):
	"""
	    broadcast that users with id in "users" has been change
	    normally user_pool should be told to refresh the user
	"""
	userChanged=user_main.getUserPool().userChanged
	map(userChanged,user_ids)
#########################################################
    def getUserInfosFromLoadedUsers(self,loaded_users,date_type):
	"""
	    return a list of user info dics, from loaded_users list
	    return dic is in format {user_id=>user_info dic}
	    loaded_users(list of LoadedUser instances): users that we want info for
	"""
	user_infos={}
	def addToUserInfo(loaded_user):
	    user_infos[str(loaded_user.getUserID())]=loaded_user.getUserInfo(date_type) #python xmlrpc required keys not to be integers
	    
    	map(addToUserInfo,loaded_users)
	return user_infos

##########################################################
    def normalUsernameExists(self,normal_username):
	"""
	    check if normal_username currently exists
	    normal_username(iterable object can be multistr or list): username that will be checked
	    return a list of exists usernames
	    NOTE: This is not thread safe 
	    XXX: test & check where_clause length
	"""
	if len(normal_username)==0:
	    return []
	where_clause=" or ".join(map(lambda username:"normal_username=%s"%dbText(username),normal_username))
	users_db=db_main.getHandle().get("normal_users",where_clause,0,-1,"",["normal_username"])
	return [m["normal_username"] for m in users_db]

##########################################################
    def searchUsers(self,conds,_from,to,order_by,desc,admin_obj):
	"""
	    search in users based on conditions in "conds" and return user_ids result from "_from" to "to"
	    admin_obj(Admin Instance): requester admin object
	"""
	self.__searchUsersCheckInput(conds,_from,to,order_by,desc,admin_obj)
	search_helper=user_main.getAttributeManager().runAttrSearchers(conds,admin_obj)
	return search_helper.getUserIDs(_from,to,order_by,desc)

    def __searchUsersCheckInput(self,conds,_from,to,order_by,desc,admin_obj):
	report_lib.checkFromTo(_from,to)
###########################################################
    def delUser(self,user_ids,comment,del_connections,admin_name,remote_address):
	"""
	    delete users with ids in user_ids
	    comment: comment when deleting users
	    del_connection tells if we should delete user(s) connection logs too
	"""
	self.__delUserCheckInput(user_ids,comment,del_connections,admin_name,remote_address)
	admin_obj=admin_main.getLoader().getAdminByName(admin_name)
	map(lambda user_id:user_main.getUserPool().addToBlackList,user_ids)
	try:
	    loaded_users=self.getLoadedUsersByUserID(user_ids)
	    total_credit=self.__delUserCheckUsers(loaded_users)
	    admin_deposit=total_credit*-1
	    ibs_query=IBSQuery()
	    ibs_query+=user_main.getCreditChangeLogActions().logCreditChangeQuery("DEL_USER",
									      admin_obj.getAdminID(),
									      user_ids,
									      0,
									      admin_deposit,
									      remote_address,
									      comment)
	    ibs_query+=admin_main.getActionManager().consumeDepositQuery(admin_obj.getAdminID(),admin_deposit)
	    self.__delUserQuery(ibs_query,user_ids,del_connections)
	    ibs_query.runQuery()
	    admin_obj.consumeDeposit(admin_deposit)
	    map(user_main.getUserPool().userChanged,user_ids)
	finally:
	    map(lambda user_id:user_main.getUserPool().removeFromBlackList,user_ids)

    def __delUserCheckInput(self,user_ids,comment,del_connections,admin_name,remote_address):
	admin_main.getLoader().checkAdminName(admin_name)
	if not iplib.checkIPAddr(remote_address):
	    raise GeneralException(errorText("GENERAL","INVALID_IP_ADDRESS")%remote_addr)
	if len(user_ids)==0:
	    raise GeneralException(errorText("USER_ACTIONS","INVALID_USER_COUNT")%0)


    def __delUserCheckUsers(self,loaded_users):
	"""
	    check users and return their total credit
	    WARNING: XXX this is not safe, checking online, and unloading there! to be fixed
	"""
	total_credit=0
	for loaded_user in loaded_users:
	    if loaded_user.isOnline():
	        raise GeneralException(errorText("USER_ACTIONS","DELETE_USER_IS_ONLINE"%loaded_user.getUserID()))
	    total_credit+=max(0,loaded_user.getBasicUser().getCredit())
	return total_credit

    def __delUserQuery(self,ibs_query,user_ids,del_connections):
	user_id_conds=" or ".join(map(lambda user_id:"user_id=%s"%user_id,user_ids))
	ibs_query+=self.__delUserAttrsQuery(user_id_conds)
	ibs_query+=self.__delUserNormalAttrsQuery(user_id_conds)
	ibs_query+=self.__delUserVoIPAttrsQuery(user_id_conds)
	ibs_query+=self.__delUserFromUsersTableQuery(user_id_conds)
	if del_connections:
	    ibs_query+=user_main.getConnectionLogManager().deleteConnectionLogsForUsersQuery(user_ids)

    def __delUserAttrsQuery(self,user_id_conds):
	"""
	    user_ids_conds: condition of user_ids
	"""
	return ibs_db.createDeleteQuery("user_attrs",user_id_conds)

    def __delUserNormalAttrsQuery(self,user_id_conds):
	return ibs_db.createDeleteQuery("normal_users",user_id_conds)

    def __delUserVoIPAttrsQuery(self,user_id_conds):
	return ibs_db.createDeleteQuery("voip_users",user_id_conds)

    def __delUserFromUsersTableQuery(self,user_id_conds):
	return ibs_db.createDeleteQuery("users",user_id_conds)

################################################################
    def getUserIDsWithBasicAttr(self,attr_name,attr_value):
	"""
	    return user_ids whom attr_name value in basic attrs is attr_value
	"""
	user_ids=db_main.getHandle().get("users","%s=%s"%(attr_name,attr_value),
					 0,-1,("user_id",True),["user_id"])
	return map(lambda dic:dic["user_id"],user_ids)
################################################################
    def getUserIDsWithAttr(self,attr_name,attr_value):
	"""
	    return user_ids whom attr_name value is attr_value, of course user should have attr_name!
	"""
	user_ids=db_main.getHandle().get("user_attrs","attr_name=%s and attr_value=%s"%(dbText(attr_name),dbText(attr_value)),
					 0,-1,("user_id",True),["user_id"])
		
	return map(lambda dic:dic["user_id"],user_ids)
#################################################################
    def getPersistentLanUsers(self,ras_id):
	"""
	    return a list of dics, containin
	"""
	return db_main.getHandle().get("persistent_lan_users","persistent_lan_ras_id=%s"%ras_id)

##########################################################
    def planMacExists(self,mac):
	"""
	    check if mac currently exists in plan_macs
	    mac(iterable object can be multistr or list): mac that will be checked
	    return a list of exists macs
	    NOTE: This is not thread safe 
	    XXX: test & check where_clause length
	"""
	if len(mac)==0:
	    return []
	where_clause=" or ".join(map(lambda m:"persistent_lan_mac=%s"%dbText(m),mac))
	users_db=db_main.getHandle().get("persistent_lan_users",where_clause,0,-1,"",["persistent_lan_mac"])
	return [m["persistent_lan_mac"] for m in users_db]

##################################################################
    def killUser(self,user_id,ras_ip,unique_id_val):
	"""
	    kill user on "ras_ip" and "unique_id_val" and check that user is "user_id"
	"""
	ras_id=ras_main.getLoader().getRasByIP(ras_ip).getRasID()
	user_obj=user_main.getOnline().getUserObjByUniqueID(ras_id,unique_id_val)
	if user_obj==None or user_obj.getUserID()!=user_id:
	    raise GeneralException(errorText("GENERAL","NOT_ONLINE")%(user_id,ras_ip,unique_id_val))
	instance=user_obj.getInstanceFromUniqueID(ras_id,unique_id_val)
	user_obj.getTypeObj().killInstance(instance)
####################################################################