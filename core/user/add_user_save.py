from core.server import handler
from core.db import ibs_db,db_main
from core.lib.general import *
from core.ibs_exceptions import *
from core.errors import errorText


import itertools

class AddUserSaveActions:
    TYPES={"Normal":1,"VoIP":2}
    def newAddUser(self,ibs_query,user_ids,usernames,passwords,admin_id,_type,comment):
	"""
	    add new user add to keep in db.
	    user_ids(list): list of user ids
	    usernames(list or multistr): list of usernames that will be kept in this user add
	    passwords(list of Password instances): list of passwords
	    admin_id(integer): id of admin doing the add user
	    _type(str): "Normal" or "VoIP"
	    comment(str)
	"""
	add_user_id=self.__getNewUserAddID()
	ibs_query+=self.__insertAddUserQuery(add_user_id,admin_id,self.__getTypeID(_type),comment)
	ibs_query+=map(self.__insertAddUserDetailsQuery,
		       itertools.repeat(add_user_id,len(user_ids)),
		       user_ids,
		       usernames,
		       map(lambda x:x.getPassword(),passwords)
		       )
	return ibs_query

    def __getNewUserAddID(self):
	return db_main.getHandle().seqNextVal("users_user_id_seq")

    def __insertAddUserDetailsQuery(self,add_user_id,user_id,username,password):
	return ibs_db.createInsertQuery("add_user_save_details",{"add_user_save_id":add_user_id,
								 "user_id":user_id,
								 "username":dbText(username),
								 "password":dbText(password)
								})

    def __insertAddUserQuery(self,add_user_id,admin_id,type_id,comment):
	return ibs_db.createInsertQuery("add_user_saves",{"add_user_save_id":add_user_id,
							  "admin_id":admin_id,
							  "type":type_id,
							  "comment":dbText(comment)
							 })

    def __getTypeID(self,_type):
	return self.TYPES[_type]


class AddUserSaveHandler(handler.Handler):
    def __init__(self):    
	handler.Handler.__init__(self,"addUserSave")
	self.registerHandlerMethod("listAddUserSaves")
    
    def __findAdminName(self,request):
	requester=request.getAuthNameObj()
	if request.has_key["admin_name"]: admin_name=request["admin_name"]
	else: admin_name=None
	if not requester.isGod():
	    try:
		admin_perm_obj=requester.getPerms()["SEE SAVED USERNAME PASSWORDS"]
	    except KeyError:
		raise PermissionException(errorText("USER_ACTIONS","ACCESS_TO_SAVED_USER_LIST_DENIED"))
	    if admin_perm_obj.getValue()=="Restricted":
		admin_name=requester.getUsername()
	return admin_name

    def listAddUserSaves(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("type","from","to")
	admin_name=self.__findAdminName(request)
	return getActionsManager().listAddUserSaves(admin_name,request["type"],request["from"],request["to"])

    def getAddUserSaveDetailes(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("add_user_save_id")
	