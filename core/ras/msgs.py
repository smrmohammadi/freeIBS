import time
class Msg:
    def __init__(self):
	self.action=None
	self.attrs={}
	self.time=time.time()
	
    def __getitem__(self,key):
	return self.attrs[key]

    def __setitem__(self,key,value):
	self.attrs[key]=value    

    def hasAttr(self,attr_name):
	return self.attrs.has_key(attr_name)
	
    def getAttrs(self):
	return self.attrs

    def setAction(self,action):
	self.action=action

    def getAction(self):
	return self.action

    def getTime(self):
	return self.time()

    def send(self):
	assert(self.action!=None)

class RasMsg(Msg):
    def __init__(self,request_pkt,reply_pkt,ras_obj):
	Msg.__init__(self)
	self.request_pkt=request_pkt
	self.reply_pkt=reply_pkt
	self.ras_obj=ras_obj
    
    def getRequestPacket(self):
	return self.request_pkt

    def getReplyPacket(self):
	return self.reply_pkt


    def getRequestAttr(self,attr_name):
	return self.request_pkt[attr_name]

    def getRasID(self):
	return self.ras_obj.getRasID()

    def getUniqueIDValue(self):
	return self[self["unique_id"]]
    
    def setRequestToAttr(self,request_key,attr_name):
	"""
	    request_key(string): Request Attribute Name
	    attr_name(string): Attribute Name that value will be assigned
	    
	    set Request packet attribute value to packet attribute with key "attr_name"
	    if request attribute has multiple values, you shouldn't use this
	"""
	try:
	    self[attr_name]=self.getRequestAttr(request_key)[0]
	except:
	    raise IBSException("Attribute %s not found in request packet"%request

    def setRequestToAttrIfExists(self,request_key,attr_name):
	"""
	    request_key(string): Request Attribute Name
	    attr_name(string): Attribute Name that value will be assigned
	    
	    set Request packet attribute value to packet attribute with key "attr_name" if it exists
	    if request attribute has multiple values, you shouldn't use this
	    
	    return True if request_key exists in request or False if it doesn't exists
	"""
	if self.request_pkt.has_key(request_key):
	    self[attr_name]=self.getRequestAttr(request_key)[0]
	    return True
	else:
	    return False

    def setInAttrs(self,key_dics):
	"""
	    key_dic(dic): dictionary in format {request_key:attr_key}
	    set request keys into attributes, this is done, by calling self.setRequestToAttr multiple times
	"""
	return map(self.setRequestToAttr,key_dics.keys(),key_dics.values())

    def setInAttrsIfExists(self,key_dics):
	"""
	    key_dic(dic): dictionary in format {request_key:attr_key}
	    set request keys into attributes, this is done, by calling self.setRequestToAttrIfExists multiple times
	"""
	return map(self.setRequestToAttrIfExists,key_dics.keys(),key_dics.values())

    def send(self):
	"""
	    Send this Message to Ras Message Dispatcher
	"""
	Msg.send(self)
	user_main.getRasMsgDispatcher().dispatch(self)

class UserMsg(Msg):
    def __init__(self):
	Msg.__init__(self)

    def send(self):
	"""
	    send this message to User Message Dispatcher
	"""
	Msg.send(self)
