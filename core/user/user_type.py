class UserType:
    def __init__(self,user_obj):
	self.user_obj=user_obj

    def killInstance(self,instance):
	pass
	
    def logout(self,instance,ras_msg):
	"""
	    logout the user
	    return an ibs_query instance
	    this function is responsible for commiting user credit if necessary
	"""
	pass

    def getOnlineReportDic(self,instance):
	return {}

    


    