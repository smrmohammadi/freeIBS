from core.errors import errorText
from core.lib.general import *

def checkFromTo(_from,to):
	if not isInt(_from) or _from<0:
	    raise GeneralException(errorText("GENERAL","FROM_VALUE_INVALID")%_from)

	if not isInt(to) or to<0 or to>1024*1024*50:
	    raise GeneralException(errorText("GENERAL","TO_VALUE_INVALID")%to)
	
	if _from>to or to-_from>1024:
	    raise GeneralException(errorText("GENERAL","TO_VALUE_INVALID")%to)
	