class AttrSearcher:
    def __init__(self,search_helper):
	self.search_helper=search_helper

    def getSearchHelper(self):
	return self.search_helper

    def run(self):
	"""
	    AttrSearchers should override this method and do the real job here
	    by updating search_helper groups and addTable
	"""
	pass

