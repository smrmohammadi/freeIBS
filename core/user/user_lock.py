class UserLock:
    def __init__(self,locker_admin_id,user_id,reason):
	"""
	    locker_admin_id (integer) : id of admin that created the lock
	    user_id (integer) : id of locked user
	    reason (str) : reason of lock
	"""
	self.locker_admin_id=locker_admin_id
	self.user_id=user_id
	self.reason=reason

    def getLockerID(self):
	"""
	    return locker admin id
	"""
	return self.locker_admin_id
	
    def getReason(self):
	return self.reason

    def getUserID(self):
	return self.user_id