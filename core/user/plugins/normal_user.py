from core.user import user_plugin,user_main,attribute
from core.user.info_holder import InfoHolder
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *
from core.lib.multi_strs import MultiStr
from core.lib.password_lib import Password,getPasswords

info_holder_name="normal user"
def init():
    user_main.getAttributeManager().registerHandler(NormalUserAttrHandler(),["normal_username","normal_password","normal_generate_password","normal_generate_password_len","normal_save_usernames"])

class NormalUserInfoHolder(InfoHolder):
    def __init__(self,normal_username,normal_password,generate_password,password_len,normal_save):
	"""
	    generate_passwd is an integer, 0 means don't generate password and use normal_passwords instead
	    positive values are same as password_lib.getPasswords _type, see function comments
	    
	    normal_save(bool): tells if we should save this username passwords in database so
				username/passwords can be seen later
				
				
	    NOTE: For delete action none of arguments are necessary, 
		  so just pass some empty values and it will be trashed when deleting
	"""
	InfoHolder.__init__(self,info_holder_name)
	self.normal_username=normal_username
	self.normal_password=normal_password
	self.generate_password=generate_password
	self.password_len=password_len
	self.normal_save=normal_save

    def __parseNormalAttrs(self):
	self.usernames=MultiStr(self.normal_username)
	if self.generate_password==0:
	    pass_multi=MultiStr(self.normal_password)
	    self.passwords=map(lambda x:Password(pass_multi[x]),range(len(self.usernames)))
	else:
	    self.passwords=getPasswords(len(self.usernames),self.generate_password,self.password_len)
	
    def checkInput(self,src,action,dargs):
	dargs["admin_obj"].canDo("CHANGE NORMAL USER ATTRIBUTES")

    def __changeCheckInput(self,users,admin_obj):
	
	if len(self.usernames)!=len(users):
	    raise GeneralException(errorText("USER_ACTIONS","NORMAL_COUNT_NOT_MATCH")%(len(users),len(self.usernames)))
	
	map(lambda passowrd:password.checkPasswordChars(),self.passwords)
	map(lambda username:user_main.getActionManager().checkNormalUsernameChars,self.usernames)

    def changeQuery(self,ibs_query,src,action,**args):
	admin_obj=args["admin_obj"]
	users=args["users"]
	
	self.__parseNormalAttrs()
	self.__changeCheckInput(users,admin_obj)
	
	
	i=0
	for user_id in users:
	    loaded_user=users[user_id]
	    if loaded_user.hasAttr("normal_username"):
		ibs_query+=user_main.getActionManager().updateNormalUserAttrsQuery(loaded_user.getUserID(),
										   self.usernames[i],
										   self.passwords[i])
	    else:
		ibs_query+=user_main.getActionManager().insertNormalUserAttrsQuery(loaded_user.getUserID(),
										   self.usernames[i],
										   self.passwords[i])
	    i+=1
	return ibs_query

    def deleteQuery(self,ibs_query,src,action,**args):
	users=args["users"]

	for user_id in users:
	    ibs_query+=user_main.getActionManager().deleteNormalUserAttrsQuery(user_id)
	return ibs_query
	

class NormalUserAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,info_holder_name)
	self.registerInfoHandlerClass(NormalUserInfoHolder,["normal_username","normal_password","normal_generate_password","normal_generate_password_len","normal_save_usernames"])

