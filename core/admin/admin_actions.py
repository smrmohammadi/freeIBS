import string
import re

from core.ibs_exceptions import *
from core.errors import errorText
from core.db import db_main,ibs_db
from core.lib.general import *
from core.admin import admin_main

class AdminActions:
    def addNewAdmin(self,username,password,name,comment,creator_id):


	self.__addNewAdminCheckInput(username,password,name,comment,creator_id)
	admin_id=self.__getNewAdminID()
	self.__addNewAdminDB(admin_id,username,password.getMd5Crypt(),name,comment,creator_id)
	self.__getAdminLoader().loadAdmin(admin_id)
	return admin_id
    
    
    def __getNewAdminID(self):
	"""
	    return a new unique admin id
	"""
	return db_main.getHandle().seqNextVal("admins_id_seq")


    def __addNewAdminDB(self,admin_id,username,password,name,comment,creator_id):
	"""
	    insert the new admin information into admins table
	"""
	db_main.getHandle().transactionQuery(self.__addNewAdminQuery(admin_id,username,password,name,comment,creator_id))
	
    def __addNewAdminQuery(self,admin_id,username,password,name,comment,creator_id):
	"""
	    return query to insert new admin
	"""
	return ibs_db.createInsertQuery("admins",{"admin_id":admin_id,
						  "username":dbText(username),
						  "password":dbText(password),
						  "name":dbText(name.strip()),
						  "comment":dbText(comment.strip()),
						  "creator_id":dbText(creator_id),
						  "deposit":0,
						  "due":0
						  })

    def __addNewAdminCheckInput(self,username,password,name,comment,creator_id):
	if not self.__getAdminLoader().adminNameAvailable(username):
	    raise GeneralException(errorText("ADMIN","ADMIN_USERNAME_TAKEN")%username)
	    
	if self.__checkAdminUserChars(username) != 1:
	    raise GeneralException(errorText("ADMIN","BAD_USERNAME")%username)

	if password.checkPasswordChars() != 1:
	    raise GeneralException(errorText("ADMIN","BAD_PASSWORD"))
	
	self.__getAdminLoader().checkAdminID(creator_id)

    def __checkAdminUserChars(self,username):
	if not len(username) or username[0] not in string.letters:                 
	    return 0
	if re.search("[^A-Za-z0-9_]",username) != None:                 
	    return 0
	return 1



    ######################
    def changePassword(self,username,password):
	"""
	    change admin password
	    username(string): admin username
	    password(password instance): New Password instance
	"""
	self.__changePasswordCheckInput(username,password)	
	self.__changePasswordDB(username,password.getMd5Crypt())
	self.__getAdminLoader().loadAdminByName(username)
    
    def __changePasswordCheckInput(self,username,password):
	self.__getAdminLoader().checkAdminName(username)

	if password.checkPasswordChars() != 1:
	    raise GeneralException(errorText("ADMIN","BAD_PASSWORD"))

    def __changePasswordDB(self,username,password):
	db_main.getHandle().update("admins",
		      {"password":dbText(password)},
		      "username=%s"%dbText(username)
		     )
    
    
    #####################

    def __getAdminLoader(self):
	return admin_main.getLoader()

    ####################
    
    def updateInfo(self,admin_username,name,comment):
	self.__updateInfoCheckInput(admin_username,name,comment)
	admin_obj=self.__getAdminLoader().getAdminByName(admin_username)
	self.__updateInfoDB(admin_obj,name,comment)
	self.__getAdminLoader().loadAdmin(admin_obj.getAdminID())
    
    def __updateInfoDB(self,admin_obj,name,comment):
	query=self.__updateInfoQuery(admin_obj.getAdminID(),name,comment)
	db_main.getHandle().transactionQuery(query)

    def __updateInfoQuery(self,admin_id,name,comment):
	return ibs_db.createUpdateQuery("admins",{"name":dbText(name),
						  "comment":dbText(comment)},"admin_id=%s"%admin_id)

#    def __updateDepositRatioQuery(self,admin_id,deposit_ratio):
#	return ibs_db.createUpdateQuery("admins",{"deposit_ratio":integer(deposit_ratio)},"admin_id=%s"%admin_id)

    def __updateInfoCheckInput(self,admin_username,name,comment):
	self.__getAdminLoader().checkAdminName(admin_username)

    ######################
    
    def consumeDeposit(self,admin_username,deposit,need_query=True):
	"""
	    consume "deposit" amount of deposit from admin with username "admin_username" and return 
	    the query to commit it into database. 
	    The caller must take care of readding deposit, if commit of query into database failed.
	    This method may raise exception in case of admin doesn't have enough deposit. In such cases caller
	    doesn't need to readd deposit!
	    need_query(boolean): tell if we need query to be returned, useful when query failed and we want to readd
				 deposit to in memory object
	"""
	admin_obj=self.__getAdminLoader().getAdminByName(admin_username)
	new_deposit=admin_obj.consumeDeposit(deposit)
	try:
	    if new_deposit<0:
		admin_obj.canDo("NO DEPOSIT LIMIT")
	except PermissionException: #negative deposit not allowed!
	    admin_obj.consumeDeposit(-1*deposit) 
	    raise GeneralException(errorText("ADMIN","NEGATIVE_DEPOSIT_NOT_ALLOWED")%(-1*deposit))
	
	if need_query:
	    return self.consumeDepositQuery(admin_obj.getAdminID(),deposit)
	
    def consumeDepositQuery(self,admin_id,deposit):
	return ibs_db.createUpdateQuery("admins",
					{"deposit":"deposit - %s"%deposit},
					"admin_id=%s"%admin_id)

	
	    