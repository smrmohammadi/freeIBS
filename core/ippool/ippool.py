import threading
from core.ibs_exceptions import *
from core.errors import errorText

class IPpoolFullException(Exception):
    def __init__(self,_str):
	self._str=_str

    def __str__(self):
	return self._str

class IPPool:
    def __init__(self,ippool_id,ippool_name,comment,ip_list):
	"""
	    ippool_id(integer): id of ippool
	    ippool_name(str): name of ippool
	    comment(str):
	    ip_list(list of str): list of ip addresses belongs to this IPPool
	"""
	self.ippool_id=ippool_id
	self.ippool_name=ippool_name
        self.comment=coment
        self.ip_list=ip_list
        self.free=ip_list #list of free ip addresses
        self.used=[] #list of currently used ip addresses
	self.lock=threading.RLock()
    
    def getIPpoolID(self):
	return self.ippool_id

    def getIPpoolName(self):
	return self.ippool_name

    def getInfo(self):
	return {"ippool_id":self.getIPpoolID(),
		"ippool_name":self.getIPpoolName(),
		"comment":self.comment,
		"ip_list":self.ip_list,
		"free":self.free,
		"used":self.used
		}

    def getUsableIP(self):
	"""
	    return a free ip of our pool and add it to used list.
	    raise a IPpoolFullException if all ip's are used and no free ip is available
	"""
	ip=None
	self.lock.acquire()
	try:
	    try:
		ip=self.free.pop()
	    except IndexError:
		raise IPpoolFullException(errorText("IPPOOL","NO_FREE_IP")%self.getIPpoolName())
	    self.used.append(ip)
	finally:
	    self.lock.release()
        return ip
	    
	
    def freeIP(self,ip):
	"""
	    called when an used ip, freed(normally when user that ip was assigned to were logouted)
	"""
	self.lock.acquire()
	try:
	    try:
		self.used.remove(ip)
	    except ValueError:
		toLog("Trying to free ip %s from pool %s while it's not in used list!"%(self.getIPpoolName(),ip),LOG_ERROR)
		raise GeneralException(errorText("IPPOOL","IP_NOT_IN_USED_POOL")%(ip,self.getIPpoolName()))
		
	finally:
	    self.lock.release()
	
    
    def hasIP(self,ip):
	"""
	    return true if ippool has "ip" in its iplist
	"""
	return self.ip_list.has_key(ip)

