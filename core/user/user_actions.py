from core.ibs_exceptions import *
from core.lib.general import *
from core.charge import charge_main
from core.db import ibs_db,db_main
from core.db.ibs_query import IBSQuery
from core.errors import errorText
from core.admin import admin_main
from core.lib import password_lib,iplib
from core.group import group_main
from core.user import user_main
import re

class UserActions:
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
	return ibs_db.createInsertQuery("user_attrs",{"attr_value":dbText(attr_value)}
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

    def insertNormalUserAttrsQuery(self,user_id,normal_username,normal_password):
	"""
	    insert user normal attributes in "normal_users" table
	"""
	return ibs_db.createInsertQuery("normal_users",{"normal_username":dbText(normal_username),
							"normal_password":dbText(normal_password),
							"user_id":user_id}
					)

    def updateNormalUserAttrsQuery(self,user_id,normal_username,normal_password):
	"""
	    update user normal attributes in "normal_users" table
	"""
	return ibs_db.createUpdateQuery("normal_users",{"normal_username":dbText(normal_username),
							"normal_password":dbText(normal_password),
							},"user_id=%s"%user_id
					)

    def deleteNormalUserAttrsQuery(self,user_id):
	"""
	    delete user normal attributes from "normal_users" table
	"""
	return ibs_db.createDeleteQuery("normal_users","user_id=%s"%user_id)

######################################################
    def checkNormalUsernameChars(self,username):
	if not len(username) or username[0] not in string.letters:
	    raise GeneralException(errorText("BAD_USERNAME","USER_ACTIONS"))

        if re.search("[^A-Za-z0-9_\-\.]",username) != None:
	    raise GeneralException(errorText("BAD_USERNAME","USER_ACTIONS"))
	

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

	self.__creditChangeCheckInput(remote_address,credit_change_comment)

    def addNewUsersQuery(self,_count,credit,owner_name,group_name,ibs_query):
	"""
	    _count(integer): count of users
	    owner_name(string): name of owner admin
	    credit(integer or empty string): amount of credit users will have, if credit is an empty string, group initial_credit
		is used, or an exception is raised if there's no initial_credit for user
	    group_name(string): name of group string
	    ibs_query(IBSQuery instance): IBSQuery instance we'll add query to
	    
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
	self.__broadcastChange(users)

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

    def __broadcastChange(self,users):
	"""
	    broadcast that users with id in "users" has been change
	    normally user_pool should be told to refresh the user
	"""
	userChanged=user_main.getUserPool().userChanged
	map(userChanged,users.keys())


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
    def getLoadedUsersByUsername(self,normal_usernames):
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
	where_clause=" or ".join(map(lambda username:"normal_username=%s"%dbText(username),normal_username))
	users_db=db_main.getHandle().get("normal_users",where_clause)
	return [m["normal_username"] for m in users_db]
