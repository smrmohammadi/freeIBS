class AdminLock:
    def __init__(self,locker_admin_id,admin_id,reason):
	self.locker_admin_id=locker_admin_id
	self.admin_id=admin_id
	self.reason=reason

    def getLockerID(self):
	return self.locker_admin_id
	
    def getReason(self):
	return self.reason