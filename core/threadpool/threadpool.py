import threading
import time
import copy
import sys
import traceback
from core import defs
from core.ibs_exceptions import *
from core.lib.general import *
from core import main
from core.debug import thread_debug

#single bytecode operations are thread safe

class IBSThread(threading.Thread):
    def run(self):
	thread_debug.debug_me()
        while 1:
            self.event_obj.wait()
            self.event_obj.clear() #clear it, to suspend the thread after completing the job
	    (method,args_list)=self.job
	    if method == "exit":
		return
            try:
	        apply(method,args_list)
            except:
    		logException(LOG_ERROR,"Exception on thread %s while running %s"%(self,self.job))

            getThreadPool().releaseThread(self)

    def setEvent(self,event_obj):
	self.event_obj=event_obj

    def setJob(self,method,args_list):
	self.job=[method,args_list]
    
class ThreadPool:

    def __init__(self):
	self.__pool={}
	self.__in_use={}
        self.tlock=threading.RLock() 
	self.__initThreads()

    def __initThreads(self):
        for i in range(defs.THREAD_POOL_DEFAULT_SIZE):
            self.__createThread("thread_%s"%i)
        
    def __createThread(self,t_name):
	    (new_thread,new_event)=self.__getNewThread(t_name)
            self.__addToPoolWithLocking(new_thread,new_event)

    def __getNewThread(self,t_name):
	"""
	    create a new thread with name t_name
	    each thread has an event object to sleep on. 
	    event object is used to wake the thread
	"""
        new_thread=IBSThread(name=t_name) 
	new_event=self.__getNewEvent()
	new_thread.setEvent(new_event)
        new_thread.start()
        return (new_thread,new_event)

    def __getNewEvent(self):
	new_event=threading.Event() 
        new_event.clear()
	return new_event
	    
    def __addToPoolWithLocking(self,new_thread,new_event):
	"""
	    add new_threan and new_event to pool, with locking
	"""
	self.tlock.acquire()
	try:
	    self.__addToPool(new_thread,new_event)
	finally:
	    self.tlock.release()

    def __addToPool(self,new_thread,new_event):
        self.__pool[new_thread]=new_event

    def runThread(self,wrapper,method,args_list=[]):
	"""
	    run a thread, that is called from wrapper "wrapper" to run method "method"
	    with arguments "args_list"
	    wrapper(ThreadPoolWrapper instance): wrapper that want to allocate new thread
	    method(function): function to run
	    arg_list(list): list of arguments
	"""
        if not main.isShuttingDown():
            self.__runThread(wrapper,method,args_list)
        else:
            raise ThreadException("We're shutting down")

    def __runThread(self,wrapper,method,arg_list):
        self.tlock.acquire()
        try:
            (thread,event)=self.__getThreadFromPool()
            self.__addToInUse(thread,event,method,arg_list,wrapper)
	    thread.setJob(method,arg_list)
            event.set() 
        finally:
            self.tlock.release()
	
    def __getThreadFromPool(self):
	"""
	    return a free thread from pool, or allocate if we are out of threads and we didn't hit
	    the maximum number of threads
	"""
        pool_size=len(self.__pool)
        if pool_size==0:
            in_use_size=len(self.__in_use)
            if in_use_size<defs.THREAD_POOL_MAX_SIZE:
                (thread,event)=self.__getNewThread("thread_%s"%in_use_size)
            else:
                raise ThreadException("No Available thread")
        else:
    	    (thread,event)=self.__pool.popitem()
        return (thread,event)

    def __addToInUse(self,thread,event,method,args_list,wrapper):
        self.__in_use[thread]=[event,method,args_list,wrapper,time.time()]

    def releaseThread(self,thread): 
	"""
	    each thread will call this to tell his job has finished
	"""
	self.tlock.acquire()
	try:
	    if thread in self.__in_use:
        	event=self.__in_use[thread][0]
		wrapper=self.__in_use[thread][3]
	    else:
        	raise ThreadException("no such thread to release")
	    self.__delFromInUse(thread)
    	    self.__addToPool(thread,event)
	finally:
	    self.tlock.release()

	if wrapper!=None:
	    wrapper.threadReleased()
	
    def __delFromInUse(self,thread):
        del(self.__in_use[thread])

    def shutdown(self,sec=10): 
	"""XXX
	    shutdown the threadpool, by calling exit function on all threads
	    it will wait until all threads exits for maximum "sec" seconds
	"""
        while len(self.__pool) != 0 or len(self.__in_use) != 0:
            bak=copy.copy(self.__in_use)
            for thread in bak:
                if not thread.isAlive():
                    self.__delFromInUse(thread)
	            thread.join()
    
            for thread in range(len(self.__pool)):
                self.__runThread(None,"exit",[],-1)
	
	    time.sleep(1)
	    sec-=1
	    if sec==0:
		break

	    toLog("threadpool.shutdown: pool \"%s\" inUse \"%s\""%(self.__pool,self.__in_use),LOG_DEBUG,defs.DEBUG_ALL)
	
    def printMe(self):
        print "Free: %s"%self.__pool
	print "\n"
        for thread in self.__in_use:
	    print "Thread %s doing %s args %s"%(thread,thread.job[0],thread.job[1])


        
def initThreadPool():
    global main_thread_pool
    main_thread_pool=ThreadPool()

def getThreadPool():
    return main_thread_pool
