import traceback
import time
import threading
import defs
import sys

LOG_DEBUG=0
LOG_ERROR=2
LOG_RADIUS=4
LOG_SERVER=8
LOG_QUERY=16


class DBException (Exception):
    def __init__(self,str_error):
        toLog("dbException: %s"% str_error,LOG_ERROR)
        self.str_error=str_error
    def __str__(self):
        return self.str_error


class ThreadException (Exception):
    def __init__(self,str_error):
        toLog("threadException: %s" % str_error,LOG_ERROR)
        self.str_error=str_error
    def __str__(self):
        return self.str_error

class IBSException(Exception):
    """
	IBSException, used for internally errors, that must be logged
    """
    def __init__(self,str_error):
        toLog("IBSException: %s" % str_error,LOG_ERROR)
        self.str_error=str_error
    def __str__(self):
        return self.str_error



class PermissionException (Exception):
    def __init__(self,str_error):
        toLog("PermissionException: %s"%str_error,LOG_DEBUG,defs.DEBUG_ALL)
        self.str_error=str_error
    def __str__(self):
        return self.str_error
		

class HandlerException (Exception):
    def __init__(self,strError):
        toLog("HandlerException: ",LOG_ERROR)
        self.strError=strError
    def __str__(self):
        return self.strError

class XMLRPCFault (Exception):
    def __init__(self,str_error):
	self.str_error=str_error
    
    def __str__(self):
	return self.str_error

class RSHException (Exception):
    def __init__(self,strError):
        toLog("rshException: " + strError,LOG_ERROR)
        self.strError=strError
    def __str__(self):
        return self.strError


class IBSError(Exception):
    pass

class GeneralException (IBSError):
    def __init__(self,strError):
	if(defs.DEBUG_LEVEL>=defs.DEBUG_ALL):
	    last_stack = traceback.extract_stack()[-2]
    	    toLog("GeneralException: in (%s,%s,%s) : %s"%
		(last_stack[0],last_stack[2],last_stack[1],strError),LOG_DEBUG)
        self.strError=strError
    def __str__(self):
        return self.strError

class LoginException (IBSError):
    def __init__(self,str_error):
        toLog("loginException: %s"%str_error,LOG_DEBUG)
        self.str_error=str_error
    def __str__(self):
        return self.str_error



class Logger:

    
    def __init__(self,file_name):

        self.re_open=0
	self.file_name=file_name
        self.open()
	self.tlock=threading.RLock()

    def open(self):     
	    try:
    		self.fd=open(self.file_name,"a+")
	    except IOError,(errno,errStr):
        	print "Warning: Can't open log file" + errStr
		raise
	    except Exception,e:
        	print "Warning: Can't open log file" + str(e)
		raise
        
    def write(self,_str,add_stack=0):
	self.tlock.acquire()
	try:
    	    try:
        	if self.re_open==1:
            	    self.reOpenFD()

        	self.fd.write(self.timeStr() + " " + _str + "\n") 
		if add_stack:
		    self.fd.write("\n%s"%self.stackTrace())
        	self.re_open=0
        	self.fd.flush()
            
    	    except IOError,(errNo,errStr):
        	if self.re_open!=1:
            	    self.re_open=1
            	    self.write(str,level)
        
	finally:
	    self.tlock.release()

    def stackTrace(self):
        retStr=""
        stackList=traceback.format_list(traceback.extract_stack())
        for tmp in stackList:
            retStr+=tmp
        return retStr

    def timeStr(self):
        return time.strftime("%Y/%m/%d-%H:%M:%S")

    def reOpenFD(self):
        self.fd.close()
        self.open()



def init():
    global debug_log_handle,error_log_handle,radius_log_handle,server_log_handle,query_log_handle
    debug_log_handle=Logger("/var/log/IBSng/ibs_debug.log")
    error_log_handle=Logger("/var/log/IBSng/ibs_error.log")
    radius_log_handle=Logger("/var/log/IBSng/ibs_radius.log")
    server_log_handle=Logger("/var/log/IBSng/ibs_server.log")
    query_log_handle=Logger("/var/log/IBSng/ibs_queries.log")

def toLog(_str,log_file,debug_level=0,add_stack=0): 
    """
	log _str to a log file that explained by log_file
	if IBS debug_level is more than debug_level
	_str(string): string to log
	log_file(integer): explained by LOG_DEBUG , LOG_ERROR , LOG_RADIUS, LOG_SERVER definitions (on top of this file)
	debug_level(integer): minimum debug level to log this event
    """
    if debug_level>defs.DEBUG_LEVEL: 
	return

    if log_file&LOG_ERROR:
        error_log_handle.write(_str,add_stack)
    elif log_file&LOG_RADIUS:
	radius_log_handle.write(_str,add_stack)
    elif log_file&LOG_SERVER:
	server_log_handle.write(_str,add_stack)
    elif log_file&LOG_QUERY:
	query_log_handle.write(_str,add_stack)
    else:
	debug_log_handle.write(_str,add_stack)

def logException(log_file,extra_str="",debug_level=0):
    (_type,value,tback)=sys.exc_info()
    toLog(extra_str+"".join(traceback.format_exception(_type, value, tback)),log_file,debug_level)
