class AttrHolder:
    """
	This class used to hold attributes. Normally for parsing them into interface
	meaningful values
    """
    def __init__(self,*args):
	"""
	    initalizer will be called by attributes as arguments. 
	    The Arg list names should passed to registerAttrHolderClass in AttributeHandler 
	"""
	pass

    def getParsedDic(self):
	"""
	    return parsed dic of attributes
	"""
	return {}