import time
import threading

from core import defs
from core.ibs_exceptions import *
from core.event import event
from core import main
from core.lib.general import *

#TODO: more exception checkings


class DBPool:
    __pool=[]
    __in_use={}
    tlock=None
    
    def __init__(self):
        self.tlock=threading.RLock()
	self.__createHandles()

    def __createHandles(self):
        for i in range(defs.DB_POOL_DEFAULT_CONNECTIONS):
            while not main.isShuttingDown(): #this make ibs don't quit on startup when database doesn't still started. (it takes some time to start esp. after a server crash)
		try:                          #ibs will wait until it can create the connection
		    db_obj=defs.getDBHandle() #this raises some risks, for ex. when DB_POOL_DEFAULT_CONNECTIONS is too high
		except:			      #and database can't create this amount of connection, ibs won't start/quit
		    logException(LOG_ERROR,"Can't connect to database")
		    time.sleep(5)
		    continue
		self.__addToPool(db_obj)
		break

    def getHandle(self):
	handle=self.__getHandleFromPool()
        self.__addToInUse(handle)
        return handle

    def release(self,handle):
        self.__delFromInUse(handle)
        self.__addToPool(handle)   

    def check(self):
        now=time.time()
        self.tlock.acquire()
        try:
            to_del=[]
            for handle in self.__in_use:
                if now-self.__in_use[i]>defs.DB_POOL_MAX_RELEASE_TIME:
		    toLog("Found stale db connection %s"%str(self.__in_use[handle]),LOG_ERROR)
                    handle.reset()
                    to_del.append(handle)

            for handle in to_del:
                del(self.__delFromInUse[handle])
                self.__addToPool(handle)

            for handle in self.__pool:
                try:
                    handle.check() #ping and reset connection
                except DBException,e:
                    self.__delFromPool(handle)

	    if len(self.__pool)==0 and len(self.__in_use)==0:
		raise DBException("No Available db connection")

        finally:
            self.tlock.release()

    def close(self): #it will be called after killing all threads, so it's OK
        for handle in self.__pool:
	    try:
        	handle.close()
	    except:
		logException(LOG_ERROR,"dbpool.close")
        for handle in self.__in_use:
	    try:
		toLog("In Use Database Handle while shutting down!!!",LOG_ERROR)
        	handle.close()
	    except:
		logException(LOG_ERROR,"dbpool.close")
        
    def __addToPool(self,handle):
        self.tlock.acquire()
        try:
            self.__pool.append(handle)
        finally:
            self.tlock.release()

    def __delFromPool(self,handle):
        self.tlock.acquire()
        try:
            self.__pool.remove(handle)
        finally:
            self.tlock.release()

    def __getHandleFromPool(self):
        self.tlock.acquire()
        try:
            pool_len=len(self.__pool)
            if pool_len>0:
                handle=self.__pool.pop()
            else:
                if len(self.__in_use) > defs.DB_POOL_MAX_CONNECTIONS:
                    raise DBException("reached maximum number of connections")
        	else:
            	    handle=defs.getDBObject()
        finally:
            self.tlock.release()

        return handle
	
    def __addToInUse(self,handle):
        self.tlock.acquire()
        try:
            self.__in_use[handle]=time.time()         
        finally:
            self.tlock.release()

    def __delFromInUse(self,handle):
        self.tlock.acquire()
        try:
            del(self.__in_use[handle])
        finally:
            self.tlock.release()



def initPool():
    global main_pool
    main_pool=DBPool()
    from core.db import db_check
    db_check.init()

def getPool():
    return main_pool

