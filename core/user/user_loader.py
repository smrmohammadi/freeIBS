from core.errors import errorText
from core.ibs_exceptions import *
from core.lib.general import *
from core.db import db_main
from core.user.loaded_user import LoadedUser
from core.user.basic_user import BasicUser
from core.user.attribute import UserAttributes

def init():
    global user_loader
    user_loader=UserLoader()
    
def getLoader():
    return user_loader

class UserLoader:
    def __init__(self):
	pass

    def normalUsername2UserID(self,normal_username):
	"""
	    return user_id of user with normal username "normal_username"
	"""
	normal_attrs=self.__fetchNormalUserAttrsByNormalUsername(normal_username)
	if normal_attrs==None:
	    raise GeneralException(errorText("USER","NORMAL_USERNAME_DOESNT_EXISTS")%normal_username)
	else:
	    return normal_attrs["user_id"]
	
	
    def getLoadedUserByUserID(self,user_id):
	"""
	    return LoadedUser instance of user with id "user_id"
	"""
	basic_user=self.getBasicUser(user_id) #should be first
	user_attrs_dic=self.getUserAttrsByUserID(user_id)
	user_attrs=self.__createUserAttrs(user_attrs_dic,basic_user)
	return self.__createLoadedUser(basic_user,user_attrs)

    def getUserAttrsByUserID(self,user_id):
	"""
	    return complete user attributes containing voip and normal user attributes
	"""
	attrs=self.__fetchUserAttrs(user_id)
	attrs.update(self.__fetchNormalUserAttrsByUserID(user_id))
	attrs.update(self.__fetchVoipUserAttrsByUserID(user_id))
	attrs.update(self.__fetchPersistentLanAttrs(user_id))
	return attrs

    def getBasicUser(self,user_id):
	"""
	    return BasicUser instance of user_id
	    raise a GeneralException if user with user_id doesn't exists
	"""
	basic_user_info=self.__fetchBasicUserInfo(user_id)
	if basic_user_info==None:
	    raise GeneralException(errorText("USER","USERID_DOESNT_EXISTS")%user_id)
	return self.__createBasicUser(basic_user_info)

    def __createUserAttrs(self,user_attrs_dic,basic_user):
	"""
	    create UserAttributes Instance from user_attrs_dic and basic_user
	    user_attrs_dic(dic): dic of {attr_name:attr_value}
	    basic_user(BasicUser instance): basic user informations
	"""
	return UserAttributes(user_attrs_dic,basic_user.getGroupID())

    def __createLoadedUser(self,basic_user,user_attrs):
	"""
	    create and return an instance of LoadedUser
	"""
	return LoadedUser(basic_user,user_attrs)

    def __createBasicUser(self,basic_user_info):
	"""
	    create BasicUser instance from basic_user_info
	    basic_user_info(dic): dic of user infos, normally returned by __fetchBasicUserInfo
	"""
	return BasicUser(basic_user_info["user_id"],
			 basic_user_info["owner_id"],
			 basic_user_info["credit"],
			 basic_user_info["group_id"],
			 basic_user_info["creation_date"])
			 
			 
    def __fetchBasicUserInfo(self,user_id):
	"""
	    fetch basic user info by user id and return a dic of user informations or None if 
	    there's no such id
	"""
	basic_user_info=db_main.getHandle().get("users","user_id=%s"%user_id)
	if len(basic_user_info)==0:
	    return None
	return basic_user_info[0]
	

    def __fetchNormalUserAttrsByUserID(self,user_id):
	"""
	    fetch normal user info from "normal_users" table, using user_id of user
	    return a dic of attributes in format {attr_name:attr_value}
	"""
	normal_attrs={}
	normal_db_attrs=db_main.getHandle().get("normal_users","user_id=%s"%user_id)
	if len(normal_db_attrs)==1:
	    normal_attrs["normal_username"]=normal_db_attrs[0]["normal_username"]
	    normal_attrs["normal_password"]=normal_db_attrs[0]["normal_password"]
	return normal_attrs

    def __fetchNormalUserAttrsByNormalUsername(self,normal_username):
	"""
	    fetch normal user info from "normal_users" table, using normal username of user
	    return a dic of attributes in format {attr_name:attr_value} or None if normal_username
	    doesn't exists
	"""
	normal_attrs={}
	normal_db_attrs=db_main.getHandle().get("normal_users","normal_username=%s"%dbText(normal_username))
	if len(normal_db_attrs)==1:
	    normal_attrs["user_id"]=normal_db_attrs[0]["user_id"]
	    normal_attrs["normal_username"]=normal_db_attrs[0]["normal_username"]
	    normal_attrs["normal_password"]=normal_db_attrs[0]["normal_password"]
	    return normal_attrs
	else:
	    return None

    def __fetchVoipUserAttrsByUserID(self,user_id):
	"""
	    fetch voip user info from "voip_users" table, using user_id of user
	    return a dic of attributes in format {attr_name:attr_value}
	"""
	voip_attrs={}
	voip_db_attrs=db_main.getHandle().get("voip_users","user_id=%s"%user_id)
	if len(voip_db_attrs)==1:
	    voip_attrs["voip_username"]=voip_db_attrs[0]["voip_username"]
	    voip_attrs["voip_password"]=voip_db_attrs[0]["voip_password"]
	return voip_attrs

    def __fetchUserAttrs(self,user_id):
	"""
	    return a dictionary of user attributes in format {attr_name:attr_value}
	"""
	user_attrs={}
	db_user_attrs=db_main.getHandle().get("user_attrs","user_id=%s"%user_id)
	for user_dic in db_user_attrs:
	    user_attrs[user_dic["attr_name"]]=user_dic["attr_value"]
	return user_attrs

    def __fetchPersistentLanAttrs(self,user_id):
	"""
	    return a dictionary of persistent_lan_users table attributes in format {attr_name:attr_value}
	"""
	plan_attrs={}
	plan_db_attrs=db_main.getHandle().get("persistent_lan_users","user_id=%s"%user_id)
	if len(plan_db_attrs)==1:
	    for attr_name in ["persistent_lan_ip","persistent_lan_mac","persistent_lan_ras_id"]:
		plan_attrs[attr_name]=plan_db_attrs[0][attr_name]
	return plan_attrs
