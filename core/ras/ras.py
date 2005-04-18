from core.event import periodic_events 
from core.ras.msgs import RasMsg
from core.ibs_exceptions import *
from core.ippool import ippool_main
from core.lib.sort import *
from core.ras import ras_main

PORT_TYPES=["Internet","Voice-Origination","Voice-Termination"]

class Ras:
    default_attributes={"online_check":1}

    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes):
    	"""
	    ras_ip(string): ip of ras
	    ras_id(integer): unique id of ras
	    ras_type(string): type of ras, a string that represent ras type. ex. cisco, quintum tenor...
	    port(dic): dic of ports in format    {port_name:{"phone":phone_no,"type":type,"comment":comment}
	    ippools(list): list of IPpool ids that this ras uses
	    attributes(dic): a dictionary of key=>values that show ras specific attributes
			     attributes are diffrent for various rases. for each type, 
			     we have a type_default_attributes that are default values for each type
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
	
	self.handle_reload=False #this flag tells if ras should be reloaded by recreating the ras object
				 #or ras would handle this by it's own _reload method

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
	    return True if this ras, has it's own attribute "attr_name" and else False
	    we won't search type_defaults or ras_defaults for attributes
	"""
	return self.attributes.has_key(attr_name)

    def getAllAttributes(self):
	"""
	    return a sorted list of all attributes, including ras self attributes, type attributes and default attributes
	    format is [(attr_name,attr_value)
	"""
	all_attrs={}
	all_attrs.update(self.default_attributes)
	all_attrs.update(self.type_default_attributes)
	all_attrs.update(self.attributes)
	sorted_dic=SortedDic(all_attrs)
	sorted_dic.sortByKey(False)
	return sorted_dic.getList()
		
    def getAttribute(self,attr_name):
	if self.attributes.has_key(attr_name):
	    return self.attributes[attr_name]
	elif self.type_default_attributes.has_key(attr_name):
	    return self.type_default_attributes[attr_name]
	elif self.default_attributes.has_key(attr_name):
	    return self.default_attributes[attr_name]
	else:
	    return None

    def getInfo(self):
	return {"ras_ip":self.getRasIP(),
		"ras_id":self.getRasID(),
		"radius_secret":self.getRadiusSecret(),
		"ras_type":self.getType(),
		"port":self.getPorts(),
		"attrs":self.getSelfAttributes()}

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
	if len(self.ippools)==0 or ras_msg==None:
	    return

	if reply.has_key("Framed-IP-Address"):
	    return
	
	for ippool_id in self.ippools:
	    try:
		ip=ippool_main.getLoader().getIPpoolByID(ippool_id).setIPInPacket(reply)
	    except IPpoolFullException:
		continue
	    update_msg=ras_msg.createNew(None,None,self)
	    update_msg.setAction("INTERNET_UPDATE")
	    update_msg["update_attrs"]=["ippool_id","ippool_assigned_ip"]
	    update_msg["ippool_id"]=ippool_id
	    update_msg["ippool_assigned_ip"]=ip
	    update_msg.send()
	    break
	else:
	    self.toLog("All IP Pools are full",LOG_ERROR)

    def toLog(self,msg,log_file=LOG_DEBUG):
	toLog("%s Ras %s: %s"%(self.getType(),self.getRasIP(),msg),log_file)

#################
#
# Methods that ras implementions MAY override
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
	
    def applySimpleBwLimit(self,user_msg):
	"""
	    apply or remove bandwidth limit on user
	    should return True on Success and False on Error
	    user_msg has an attribute action, that shows the action ("apply" or "remove") that should be taken
	"""
	return True
    
    def dispatch(self,user_msg):
	"""
	    This method is called when action is not one of known and standard actions.
	    This is useful when user methods know one ras supports a non-standard action that others don't.
	    if ras can't interpret the action, it should call self._raiseUnknownActionException(user_msg)
	"""
	self._raiseUnknownActionException(user_msg)
	
    def _raiseUnknownActionException(self,user_msg):
	raise IBSException("Action not %s supported by ras %s"%(user_msg.getAction(),self.getRasIP()))


    def deActivated(self):
	"""
	    called when ras is deactivated, and after ras deactivated in database.
	"""
	pass
    
    def unloaded(self):
	"""
	    called when ras object is unloaded, it should do the cleanups
	"""
	pass
    
    def _reload(self):
	"""
	    reload ras_obj only if self.handle_reload==True
	    if it has been set to False, reloading is done by unloading/reloading the object
	"""
	(ras_info,ras_attrs,ports,ippools)=ras_main.getLoader().getRasInfo(self.getRasID())

	if self.ras_ip!=ras_info["ras_ip"]:
	    ras_main.getLoader().unKeepObj(self)
	    ras_ip_changed=True
	else:
	    ras_ip_changed=False

	self.ras_ip=ras_info["ras_ip"]
	self.ras_id=ras_info["ras_id"]
	self.ras_type=ras_info["ras_type"]
	self.radius_secret=ras_info["radius_secret"]
	self.ports=ports
	self.ippools=ippools
	self.attributes=ras_attrs
	
	if ras_ip_changed:
	    ras_main.getLoader().keepObj(self)
    
class GeneralUpdateRas(Ras):
    """
	This class has an update method, that will be called for general_update_interval intervals,
	"generalUpdate" is the only method that will be called periodicly
    """
    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes):
	type_default_attributes["general_update_interval"]=10
	Ras.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes)
	self._registerEvent()

    def _registerEvent(self):
	class GeneralUpdateEvent(periodic_events.PeriodicEvent):
	    def __init__(my_self):
		periodic_events.PeriodicEvent.__init__(my_self,"%s general_update"%self.ras_ip,self.getAttribute("general_update_interval"),[],0)

	    def run(my_self):
		self.generalUpdate()
	
	self.__general_update_event=GeneralUpdateEvent()
	periodic_events.getManager().register(self.__general_update_event)
    
    def generalUpdate(self):
	return self.updateInOutBytes()

    def updateInOutBytes(self):
	pass

    def _delEvent(self):
	periodic_events.getManager().unRegister(self.__general_update_event)

    def unloaded(self):
	"""
	    children should call this method if it has been overrided
	"""
	self._delEvent()

    def _reload(self):
	Ras._reload(self)
	self._delEvent()
	self._registerEvent()

class UpdateUsersRas(GeneralUpdateRas):
    """
	This Class is same as GeneralUpdateRas but has an additional updateUsers method, that
	will be called in "update_users" interval
    """
    def __init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes):
	type_default_attributes["update_users_interval"]=60
	GeneralUpdateRas.__init__(self,ras_ip,ras_id,ras_type,radius_secret,ports,ippools,attributes,type_default_attributes)
	self._registerEvent(self)

    def _registerEvent(self):
	class UpdateUserListEvent(periodic_events.PeriodicEvent):
	    def __init__(my_self):
		periodic_events.PeriodicEvent("%s update userlist"%self.getRasIP(),self.getAttribute("update_users_interval"),[],0)

	    def run(my_self):
		self.updateUserList()

	if self.getAttribute("online_check"):
	    self.__update_userlist_event=UpdateUserListEvent()
	    periodic_events.getManager().register(self.__update_userlist_event)

    def updateUserList(self):
	pass
    
    def _delEvent(self):
	GeneralUpdateRas._delEvent(self)
	if self.getAttribute("online_check"):
	    periodic_events.getManager().unRegister(self.__update_userlist_event)
	    