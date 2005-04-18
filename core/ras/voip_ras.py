from core.lib import time_lib

class VoIPRas:
    attr_index={"H323-conf-id":13,
		"H323-remote-address":20,
		"H323-setup-time":16,
		"H323-connect-time":18,
		"H323-disconnect-time":21,
		"H323-disconnect-cause":22
	       }
    
    def getH323AttrIndex(self,attr_name):
	"""
	    return cut index of attr_name
	"""
	return self.attr_index[attr_name]

    def getH323AttrValue(self,attr_name,pkt):
	"""
	    return correct value of voip attr "attr_name"
	    Cisco Style H323 attribute values has format "name=value", so for
	    correct value we must cut the head of value
	"""
	return pkt[attr_name][0][self.getH323AttrIndex(attr_name):]
	
    def getH323EpochTimeFromAttr(self,attr_name,pkt):
	"""
	    convert "attr_name" value from pkt to epoch and return it
	"""
	return time_lib.getEpochFromRadiusTime(self.getH323AttrValue(attr_name,pkt))
	
    def setH323TimeInAttrs(self,ras_msg,attr_dic):
	"""
	    set H323 converted time in ras_msg. All Times are converted to epoch.
	    attr_dic(dic): dic in format radius_attr_name=>ras_msg_attr_name
	"""
	for rad_attr_name in attr_dic:
	    ras_msg[attr_dic[rad_attr_name]]=self.getH323EpochTimeFromAttr(rad_attr_name,ras_msg.getRequestPacket())