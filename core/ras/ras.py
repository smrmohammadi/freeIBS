from core.event import periodic_events 
from core.ras.msgs import RasMsg
from core.ibs_exceptions import *
from core.ippool import ippool_main

PORT_TYPES=["Internet","Voice-Origination","Voice-Termination"]

class Ras:
    default_attributes={"online_check":1,"update_inout_bytes_interval":10,"update_users_interval":60,"online_check_reliable":0,
			"online_check_valid_ports":0}

    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes):
    	"""
	    ras_ip(string): ip of ras
	    ras_id(integer): unique id of ras
	    ras_type(string): type of ras, a string that represent ras type. ex. cisco, quintum tenor...
	    port(dic): dic of ports in format    {port_name:{"phone":phone_no,"type":type,"comment":comment}
	    ippools(list): list of IPpool ids that this ras uses
	    attributes(dic): a dictionary of key=>values that show ras specific attributes
			     attributes are diffrent for various rases. for each type, 
			     we have a type_default_attributes that are default values for each type,
			     and default_attributes that are 
	    type_default_attributes(dic): default attributes for ras type
	"""
	self.ras_ip=ras_ip
	self.ras_id=ras_id
	self.ras_type=ras_type
	self.radius_secret=radius_secret
	self.ports=ports
	self.ippools=ippools
	self.attributes=attributes
	self.type_default_attributes=type_default_attributes

    def getRasID(self):
	return self.ras_id

    def getRasIP(self):
	return self.ras_ip
	
    def getPorts(self):
	return self.ports
	
    def hasPort(self,port_name):
	return self.ports.has_key(port_name)
	
    def hasIPpool(self,ippool_id):
	return ippool_id in self.ippools

    def getIPpools(self):
	return self.ippools

    def getSelfAttributes(self):
	return self.attributes

    def getRadiusSecret(self):
	return self.radius_secret

    def getType(self):
	return self.ras_type
    
    def hasAttribute(self,attr_name):
	"""
	    return 1 if this ras, has it's own attribute "attr_name" and else 0
	    we won't search type_defaults or ras_defaults for attributes
	"""
	return self.attributes.has_key(attr_name)

    def getAllAttributes(self):
	"""
	    return a dic of all attributes, including ras self attributes, type attributes and default attributes
	"""
	all_attrs={}
	for attrs in [self.attributes,self.type_default_attributes,self.default_attributes]:
	    for attr_name in attrs:
		if not all_attrs.has_key(attr_name):
		    all_attrs[attr_name]=attrs[attr_name]
	
	return all_attrs
		
    def getAttribute(self,attr_name):
	if self.attributes.has_key(attr_name):
	    return self.attributes[attr_name]
	elif self.type_default_attributes.has_key(attr_name):
	    return self.type_default_attributes[attr_name]
	elif self.default_attributes.has_key(attr_name):
	    return self.default_attributes[attr_name]
	else:
	    return None

    def _isOnline(self,user_msg):
	"""
	    check if user is online on ras, with condition in "user_msg"
	    must return True , if user is onlines, and False if he is not
	    contents of user_msg attributes may differ on diffrent rases
	"""
	if not self.getAttribute("online_check"):
	    return True
	
	return self.isOnline(user_msg)


    def _handleRadAuthPacket(self,request,reply):
	"""
	    request(Radius Packet Instance): Authenticate Request Packet
	    reply(Radius Packet Instance): Authenticate Reply Packet

	    Handle Radius Authenticate Packet
	    We will call self.handleRadAuthPacket that should be overrided by ras implemention
	"""
	(ras_msg,auth_success)=self._callWithRasMsg(self.handleRadAuthPacket,request,reply)
	if auth_success:
	    self._applyIPpool(ras_msg)
	return auth_success

    def _handleRadAcctPacket(self,request,reply):
	"""
	    request(Radius Packet Instance): Accounting Request Packet
	    reply(Radius Packet Instance): Accounting Reply Packet
	"""
	self._callWithRasMsg(self.handleRadAcctPacket,request,reply)

    def _callWithRasMsg(self,method,request,reply):
	"""
	    call "method" with ras_msg as argument
	    ras_msg is created by "request" , "reply"
	"""
	ras_msg=RasMsg(request,reply,self)
	apply(method,[ras_msg])
        return (ras_msg,ras_msg.send())

    def _applyIPpool(self,ras_msg):
	reply=ras_msg.getReplyPacket()
	if reply.has_key("Framed-IP-Address"):
	    return
	
	if len(self.ippools)==0:
	    return
	
	for ippool_id in self.ippools:
	    try:
		ip=ippool_main.getLoader().getIPpoolByID(ippool_id).getUsableIP()
		reply["Framed-IP-Address"]=ip
		ras_msg["ippool_id"]=ippool_id
		ras_msg["ippool_assigned_ip"]=ip
		break
	    except IPpoolFullException:
		pass
	else:
	    return

	toLog("All IP Pools are full for ras %s"%self.getRasIP(),LOG_ERROR)

#################
#
# Methods that ras implementions should override
#
#################
    def handleRadAuthPacket(self,ras_msg):
	"""
	    this method should be overrided by ras implementions
	    Ras Implemention must set their own attributes in "ras_msg" and set action of ras_msg
	"""
	pass

    def handleRadAcctPacket(self,ras_msg):
	"""
	    this method should be overrided by ras implementions
	    Ras Implemention must set their own attributes in "ras_msg" and set ras_msg action
	"""
	pass

    def isOnline(self,user_msg):
	"""
	    must return a bool (True or False) that shows wether user is online or not
	    
	    this function should be overrided by ras implementions
	"""
	return False
    
    def killUser(self,user_msg):
	"""
	    force disconnect a user, user_msg is message from user
	"""
	pass

    def getInOutBytes(self,user_msg):
	"""
	    user_msg(UserMsg instance): User Message to get inout bytes
	    return a tuple of (in_bytes,out_bytes), in and out bytes are from user view, 
		and not ras
	"""
	return (0,0)
	
class GeneralUpdateRas(Ras):
    """
	This class has an update method, that will be called for update_inout_bytes intervals,
	"UpdateInOutBytes" is the only method that will be called periodicly
    """
    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes):
	Ras.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes)
	self.__registerEvents()

    def __registerEvents(self):
	class UpdateInOutEvent(periodic_events.PeriodicEvent):
	    def __init__(my_self):
		periodic_events.PeriodicEvent.__init__(my_self,"%s updateinout"%self.ras_ip,self.getAttribute("update_inout_bytes_interval"),[],0)

	    def run(my_self):
		self.updateInOutBytes()
	

	periodic_events.getManager().register(UpdateInOutEvent())
    
    def updateInOutBytes(self):
	pass

class UpdateUsersRas(GeneralUpdateRas):
    """
	This Class is same as GeneralUpdateRas but has an additional updateUsers method, that
	will be called in "update_users" interval
    """
    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes):
	GeneralUpdateRas.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes)
	self.__registerEvents(self)

    def __registerEvents(self):
	class UpdateUserListEvent(periodic_events.PeriodicEvent):
	    def __init__(my_self):
		periodic_events.PeriodicEvent("%s update userlist"%self.ras_ip,self.getAttribute("update_users_interval"),[],0)

	    def run(my_self):
		self.updateUserList()

	if self.getAttribute("online_check"):
	    periodic_events.getManager().register(UpdateUserListEvent())

    def updateUserList(self):
	pass
    