import threading
class LoadingUser:
	"""
	    This class prevent from double parallel load of a same user
	    second loader will sleep until first on finishes
	"""
	def __init__(self):
	    self.lock=threading.Lock()
	    self.__loading={} #currently loading users
	
	def isLoading(self,user):
	    return user in self.__loading

	def loadingStart(self,user):
	    """
		called when we start loading a user
		caller may sleep here until load of previous instance of user finishes
	    """
	    wait=None
	    self.lock.acquire()
	    try:
		if user in self.__loading:
		    if self.__loading[user][0]==None:
			self.__loading[user]=UserEvent(self.__loading[user][1])
		    wait=self.__loading[user].requestWait()
		else:
		    self.__loading[user]=(None,threading.currentThread())
	    finally:
		self.lock.release()

	    if wait!=None:
		self.__loading[user].wait(wait)
	    
	def loadingEnd(self,user):
	    """
		called when we end loading a user
		this method wake waiter of user if any
	    """
	    self.lock.acquire()
	    try:
		user_event,thread=self.__loading[user]
		if user_event!=None and user_event.getWaitingCount():
		    user_event.notify()
		else:
		    del(self.__loading[user])
	    finally:
		self.lock.release()
	
class UserEvent:
    def __init__(self,running_thread):
	"""
	    object of this class would be created when two threads wants to enter critical
	    section of same user
	"""
	self.waiting=[]
	self.running_thread=running_thread
	self.recursive_calls=0
	
    def __setRunningThread(self):
	self.running_thread=threading.currentThread()
    
    def requestWait(self):
	if threading.currentThread()!=self.running_thread:
	    evt=threading.Event()
	    evt.clear()
	    self.waiting.append((evt,threading.currentThread()))
	    return evt
	else:
	    self.recursive_calls+=1
	    return None
    
    def wait(self,evt):
	evt.wait()
	self.__setRunningThread()

    def notify(self):
	if self.recursive_calls>0:
	    self.recursive_calls-=1
	elif len(self.waiting):
	    evt,thread=self.waiting.pop(0)
	    evt.set()

    def getWaitingCount(self):
	return len(self.waiting)+self.recursive_calls
	