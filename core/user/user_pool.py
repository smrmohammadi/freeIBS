"""
XXX TODO: Make getUserByNormalUsername and similars efficent without two query of same table

"""

from core.user import user_main
from core.user.loading_user import LoadingUser
from core.ibs_exceptions import *
import threading

class ReleaseCandidates:
    """
	this class keep loaded users and can be queried to release a user and tells the user id of user
	    that should be released
	users will be kept in a sorted list that will be act as a lifo queue
	
	NOTE: we're keeping LoadedUser instance of online users in the same list as others
	      if we see one of them, we add them to the end of list. This makes life easy(TM) but
	      maybe inefficient if USER_POOL_SIZE is small.
	      so please keep USER_POOL_SIZE 10x factor of your online users
    """
    def __init__(self):
	"""
	    initialize the internal list	    
	"""
	self.__release_candidates=[] #sorted list of release candidate users sorted 
	self.lock=threading.RLock()

    def addUser(self,loaded_user):
	"""
	    add a new user to queue
	    loaded_user(LoadedUser instance)
	"""
	self.lock.acquire()
	try:
	    self.__release_candidates.append(loaded_user)
	finally:
	    self.lock.release()
	
    def getCandidate(self):
	"""
	    get a candidate to release.
	    return LoadedUser instance(deleted from our queue already) or 
	    None value if no user can be released at this time (Shows that USER_POOL_SIZE is small!)
	"""
	self.lock.acquire()
	try:
	    loaded_user=None
	    try:
	        loaded_user=self.__release_candidates.pop(0)
	    except IndexError: #empty list BadThingHappened(TM)
		toLog("User Pool is full and we can't release anyone!!! Please increase USER_POOL_SIZE in defs ASAP!",LOG_ERROR&LOG_DEBUG)
		return None
	
	    return loaded_user
	finally:
	    self.lock.release()


class UserPool:
    """
	XXX MISSING: Normal And VoIP mapping to user_ids in memory!
    """
    def __init__(self):
	self.__pool_by_id={} #this is reference pool. All users should be here
	self.__pool_len=0
	self.loading_users=LoadingUser()
	self.rel_candidate=ReleaseCandidates()
	self.lock=threading.RLock()
	self.misses=0
	self.hits=0

    def __fixUserID(self,user_id):
	return long(user_id)
	
    def __isInPoolByID(self,user_id):
	"""
	    check if user with id "user_id" is in pool return LoadedUser instance if 
	    it's in pool or None if it isn't
	"""
	self.lock.acquire()
	try:
	    if self.__pool_by_id.has_key(user_id):
		self.hits+=1
		return self.__pool_by_id[user_id]
	    self.misses+=1
	    return None
	finally:
	    self.lock.release()

    def __saveInPool(self,loaded_user):
	"""
	    Save LoadedUser instance into pool
	"""
	self.__checkPoolSize()
	self.rel_candidate.addUser(loaded_user)
	self.__addToPool(loaded_user)

    def __addToPool(self,loaded_user):
    	self.lock.acquire()
        try:
	    self.__pool_by_id[loaded_user.getUserID()]=loaded_user
	finally:
	    self.lock.release()

    def __checkPoolSize(self):
	"""
	    check pool size and release a user if we are more then defs.MAX_USER_POOL_SIZE
	"""
    	self.lock.acquire()
        try:
	    self.__pool_len+=1
	finally:
	    self.lock.release()
	if self.__pool_len>defs.MAX_USER_POOL_SIZE: 
	    self.__releaseOneUser()

    def __releaseOneUser(self):
	"""
	    release a user from pool, if possible
	"""
	loaded_user_obj=self.rel_candidate.getCandidate()
        if loaded_user_obj!=None:
	    self.lock.acquire()
	    try:
	        if loaded_user_obj.isOnline() or self.loading_users.isLoading(loaded_user_obj.getUserID()):
		    self.__releaseOneUser()
		    self.rel_candidates.addUser(loaded_user)
		else:
		    try:
		        self.__delFromPool(loaded_user_obj.getUserID())
		    except KeyError: #user has been deleted previously by userChanged method
		        self.__releaseOneUser()
	    finally:
	        self.lock.release()

    def __delFromPool(self,user_id):
	"""
	    delete user with id "user_id" from pool
	"""
	self.lock.acquire()
	try:
	    self.__pool_len-=1
	    del(self.__pool_by_id[user_id])
	finally:
	    self.lock.release()


    def __loadUserByID(self,user_id):
	"""
	    load user into memory using user id and return a LoadedUser instance
	    also put user in pool
	"""	
	loaded_user=user_main.getUserLoader().getLoadedUserByUserID(user_id)
	self.__saveInPool(loaded_user)
	return loaded_user


################################
    def getUserByID(self,user_id,online_flag=False):
	"""
	    return a LoadedUser instance of user with id "user_id"
	"""
	user_id=self.__fixUserID(user_id)
	self.loading_users.loadingStart(user_id)
	try:
	    loaded_user=self.__isInPoolByID(user_id)
	    if loaded_user==None:
		loaded_user=self.__loadUserByID(user_id)
	    
	    if online_flag: #it should be done here, because we don't want to release this user while he's trying to log in
		loaded_user.setOnlineFlag(True)
	finally:
	    self.loading_users.loadingEnd(user_id)
	return loaded_user
	
#################################
    def getUserByNormalUsername(self,normal_username,online_flag=False):
	"""
	    XXX: current implemention can be optimized by not querying normal_users table twice
	    return a LoadedUser instance of user with normal username "normal_username"
	"""
	user_id=user_main.getUserLoader().normalUsername2UserID(normal_username)
	return self.getUserByID(user_id)

#################################
    def userChanged(self,user_id):
	"""
	    called when attributes or information of user with id "user_id" changed
	"""
	user_id=self.__fixUserID(user_id)
	self.loading_users.loadingStart(user_id)
	try:
	    loaded_user=self.__isInPoolByID(user_id)
	    if loaded_user!=None:
	        if loaded_user.isOnline():
		    loaded_user.reload()
	        else:
	    	    self.__delFromPool(user_id)
	finally:
	    self.loading_users.loadingEnd(user_id)

