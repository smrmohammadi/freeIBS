import ibs_server
from lib import *
from ibs_exceptions import *
import defs
import pwd
import os


def init():
    ibs_server.registerHandler("mailLogin",mailLoginHandler)

def mailDirHome(username,user_home=0):
    home="%s/%s"%(defs.MAILMASTER_HOME,username)
    if user_home==1:
	return home
    maildir_home=home+"/Maildir"
    return maildir_home

def createMail(username,quota_kbytes):
    maildir_home=mailDirHome(username)
    home=mailDirHome(username,1)
    (mailmaster_uid,mailmaster_gid)=pwd.getpwnam(defs.MAILMASTER_USERNAME)[2:4]
    os.mkdir(home)
    ret=os.system("/var/qmail/bin/maildirmake %s"%maildir_home)
    if ret!=0:
	raise generalException("Error occured while creating maildir for user")

    os.chown(home,mailmaster_uid,mailmaster_gid)
    os.chown(maildir_home,mailmaster_uid,mailmaster_gid)
    os.chown(maildir_home+"/cur",mailmaster_uid,mailmaster_gid)
    os.chown(maildir_home+"/new",mailmaster_uid,mailmaster_gid)
    os.chown(maildir_home+"/tmp",mailmaster_uid,mailmaster_gid)

    createDotQmailFile(username,quota_kbytes)

def changeQuota(username,quota_kbytes):
    createDotQmailFile(username,quota_kbytes)

def createDotQmailFile(username,quota_kbytes):
    fd=open("%s/.qmail-%s"%(defs.MAILMASTER_HOME,username),"w+")
    fd.write("|%s %s %s\n%s/\n"%(defs.MAIL_QUOTA_CHECK_COMMAND,username,integer(quota_kbytes),mailDirHome(username)))
    fd.close()


def deleteMail(username):
    home="%s/%s"%(defs.MAILMASTER_HOME,username)
    ret=os.system("rm -rf %s"%home)
    os.remove("%s/.qmail-%s"%(defs.MAILMASTER_HOME,username))
    

def getMailQuotaUsage(username): #use an ugly way
    fd=os.popen("%s %s/%s"%(defs.MAIL_QUOTA_USAGE,defs.MAILMASTER_HOME,username))
    line=fd.readline()
    fd.close()
    sp=line.split()
    if len(sp)!=2:
	return -1
    return integer(sp[0])

    
class mailLoginHandler(ibs_server.ServerHandler):
    def run(self):
	import User	
	self.checkAuthType("mail")
	self.checkArg("username")

	args=self.args
	userObj=User.User(args["username"])

    	if userObj.user_info["has_email"]=="f":
	    raise generalException("You don't have a mailbox")
	if userObj.isLocked():
	    raise generalException("You are locked!")
	if userObj.isExpired():
	    raise generalException("Your account has expired")
	self.write("mail:%s\r\n"%userObj.user_info["password"])
	    