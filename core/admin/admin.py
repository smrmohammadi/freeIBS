from core.db import db_main,ibs_db
from core.lib import password_lib
from core.ibs_exceptions import *
from core.lib.general import *
from core.charge import charge_main
import re
import threading
import copy


class Admin:
    def __init__(self,username,password,name,comment,admin_id,deposit,creator_id,due):
	self.username=username
	self.password=password_lib.Password(password.strip())
	self.name=name
	self.comment=comment
	self.admin_id=integer(admin_id)
	self.deposit=integer(deposit)
	self.creator_id=integer(creator_id)
	self.due=due


    def getAdminID(self):
	return self.admin_id

    def getUsername(self):
	return self.username

    def getAdminInfo(self):
	"""
	    return a dictionary of admin properties
	    normally contains username,name,comment,admin_id,deposit,creator_id
	"""
	return {"username":self.username,
		"name":self.name,
		"comment":self.comment,
		"admin_id":self.admin_id,
		"deposit":self.deposit,
		"creator_id":self.creator_id
		}

    def setLocks(self,locks):
	"""
	    locks is a list of admin_lock instances
	"""
	self.locks=locks
	
    def setPerms(self,perms):
	"""
	    calls when loading an admin to set its perms
	    perms is a dic of {perm_name:perm_obj}
	"""
	self.perms=perms

    def getPerms(self):
	return self.perms

    def checkPerm(self,perm_name,*args):
	"""
	    check if this admin has permission with name "perm_name" and it's acceptable with
	    "args", permissions raise a PermissionException on access denied conditions
	"""
	try:
	    return apply(self.perms[perm_name].check,args)
	except KeyError:
	    raise PermissionException(errorText("PERMISSION","DONT_HAVE_PERMISSION"))
	except IndexError:
	    raise PermissionException(errorText("PERMISSION","DONT_HAVE_PERMISSION"))


    def hasPerm(self,perm_name):
	"""
	    check if this admin --JUST HAS-- permission "perm_name" regardless of enviroment and 
	    permission values. To check a permission use checkPerm instead.
	"""
	return self.perms.has_key(perm_name)

    def canDo(self,perm_name,*args):
	"""
	    check if this admin can do "perm_name"
	    "can do" is a positive statement, so "perm_name" can't be a negative (restrictive) 
	    permission such as LIMIT_LOGIN_ADDR.
	    raise a PermissionException if admin can't do it
	"""
	if self.isGod():
	    return 
	apply(self.checkPerm,[perm_name]+list(args))
	

    def isGod(self):
	try:
	    self.checkPerm("GOD")
	except PermissionException:
	    return False
	
	return True

    def checkPass(self,password):
	if password == self.password:
	    return 1
	else:
	    return 0
	
    def isAuthorizedFromAddr(self,remoteaddr):
	if self.hasPerm("LIMIT LOGIN ADDR"):
	    self.checkPerm("LIMIT LOGIN ADDR",remoteaddr)

    def consumeDeposit(self,credit): 
	"""
	    consume admin deposit in loaded instance
	"""
	self.deposit-=credit
	return self.deposit

    def checkPass(self,password):
	"""
	    check if "password" is correct for this admin 
	    password(Password instance): password to check
	"""
	if not self.__checkPass(password):
	    raise GeneralException(errorText("ADMIN_LOGIN","INCORRECT_PASSWORD"))

    def __checkPass(self,password):
	"""
	    check if "password" is correct for this admin 
	    password(Password instance): password to check
	    return 1 if it's correct and 0 if it's not
	"""
	if password == self.password:
	    return 1
	else:
	    return 0


    def canLogin(self,remoteaddr): 
	"""
	    check if this admin can login to server from remote address "remoteaddr"
	"""
	self.isAuthorizedFromAddr(remoteaddr)
	self.__checkIfLocked()
	

    def isLocked(self):
	"""
	    return 0 if admin is not locked
	    return a positive integer if this admin is locked
	"""
	return len(self.locks)
	
    def __checkIfLocked(self):
	"""
	    check if this admin is locked, raise a LoginException if it's locked
	    so admin can't login to IBS
	"""
	if self.isLocked():
	    raise LoginException(errorText("ADMIN_LOGIN","ADMIN_LOCKED"))


    def checkAuth(self,auth_pass,remote_addr):
	"""
	    authenticate admin, raise an exception if access is denied
	"""
	self.checkPass(auth_pass)
	self.canLogin(remote_addr)

    def canUseCharge(self,charge_name):
	"""
	    return True if admin can use charge with name "charge_name"
	"""
	if charge_main.getLoader().getChargeByName(charge_name).isVisibleToAll() or self.isGod() or self.hasPerm("ACCESS ALL CHARGES"):
	    return True

	if self.hasPerm("CHARGE ACCESS"):
	    try:
	        self.checkPerm("CHARGE ACCESS",charge_name)
		return True
	    except PermissionException:
		return False
	return False

    def canUseGroup(self,group_name):
	"""
	    return True if admin can use group with name "group_name"
	"""
	if self.isGod() or self.hasPerm("ACCESS ALL GROUPS"):
	    return True

	if self.hasPerm("GROUP ACCESS"):
	    try:
	        self.checkPerm("GROUP ACCESS",group_name)
		return True
	    except PermissionException:
		return False
	return False

    def canAccessUser(self,loaded_user):
	"""
	    raise an PermissionException if admin can not access and get information of  user loaded in "loaded_user"
	    or return if admin has access to the user. Checking is done with admin permission GET USER INFORMATION
	"""
	self.checkPerm("GET USER INFORMATION",loaded_user)

