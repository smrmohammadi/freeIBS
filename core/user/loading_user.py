import threading
class LoadingUser:
	"""
	    This class prevent from double parallel load of a same user
	    second loader will sleep until first on finishes
	"""
	def __init__(self):
	    self.lock=threading.Lock()
	    self.__loading=[] #currently loading users, to prevent from 
	    self.__locks={}
	
	def isLoading(self,user):
	    return user in self.__loading

	def loadingStart(self,user):
	    """
		called when we start loading a user
		caller may sleep here until load of previous instance of user finishes
	    """
	    evt=None
	    self.lock.acquire()
	    try:
		if user in self.__loading:
    		    evt=threading.Event()
		    evt.clear()

		    if not self.__locks.has_key(user):
			self.__locks[user]=[evt]
		    else:
			self.__locks[user].append(evt)
	    finally:
		self.lock.release()

	    if evt!=None:
		evt.wait()
	    
	def loadingEnd(self,user):
	    """
		called when we end loading a user
		this method wake waiter of user if any
	    """
	    evt=None
	    self.lock.acquire()
	    try:
		if self.__locks.has_key(user):
		    evt=self.__locks[user].pop(0)
		    if len(self.__locks[user])==0:
			del(self.__locks[user])
		    
	    finally:
		self.lock.release()
	
	    if evt!=None:
		evt.set()
