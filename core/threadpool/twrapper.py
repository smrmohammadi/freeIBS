import threading
from core.threadpool import threadpool


class ThreadPoolWrapper:
    """
	Wrapper for threadpool
	it use a queue, to enqueue jobs that currently can't run due to our maximum 
	number of allocated threads limit.
	if we didn't get to the limit, we'll ask the mainThreadPool to get us a thread
    """
    def __init__(self,usage_limit,name):
	"""
	    usage_limit(integer): maximum number of allocated threads for this object
	    name(String): Object name, used for debugging
	"""
	self.tlock=threading.RLock()
	self.usage=0
	self.usage_limit=usage_limit
	self.name=name
	self.queue=[]

    def __runInThreadPool(self,method,args):
	threadpool.getThreadPool().runThread(self,method,args)

    def runThread(self,method,args):
	"""
	    run a new thread whithin this wrapper
	"""
	self.tlock.acquire()
	try:
	    if self.usage>self.usage_limit:
		self.queue.append([method,args])
	    else:
		self.__runInThreadPool(method,args)	
		self.usage+=1
	finally:
	    self.tlock.release()
	    
    
    def threadReleased(self):
	"""
	    called when main thread pool wants to signal us that one of our threads released
	"""
	self.tlock.acquire()
	try:
	    if len(self.queue)>0:
		(method,args,priority)=self.queue.pop(0)
		self.__runInThreadPool(self,method,args)
	    else:
		self.usage-=1
	finally:
	    self.tlock.release()
