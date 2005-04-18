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
        toLog("DBException: %s"% str_error,LOG_ERROR)
        self.str_error=str_error

    def __str__(self):
        return self.str_error

class ThreadException (Exception):
    def __init__(self,str_error):
        toLog("ThreadException: %s" % str_error,LOG_ERROR)
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
    def __init__(self,err_str):
        toLog("HandlerException: %s"%err_str,LOG_ERROR)
        self.err_str=err_str

    def __str__(self):
        return self.err_str

class XMLRPCFault (Exception):
    def __init__(self,str_error):
	self.str_error=str_error
    
    def __str__(self):
	return self.str_error

class SnmpException (Exception):
    def __init__(self,err_str):
        toLog("SnmpException: %s" % err_str,LOG_ERROR)
        self.err_str=err_str

    def __str__(self):
        return self.err_str


class IBSError(Exception):
    def __init__(self,str_error):
	self.str_error=str_error
    
    	if(defs.DEBUG_LEVEL>=defs.DEBUG_ALL):
	    last_stack = traceback.extract_stack()[-2]
    	    toLog("%s: in (%s,%s,%s) : %s"%
		(self.__class__.__name__,last_stack[0],last_stack[2],last_stack[1],str_error),LOG_DEBUG)

    def __str__(self):
	return self.str_error

    def getErrorKey(self):
	try:
	    return self.str_error[:self.str_error.index("|")]
	except ValueError:
	    return ""

    def getErrorText(self):
	try:
	    return self.str_error[self.str_error.index("|")+1:]
	except ValueError:
	    return self.str_error
	
    
class GeneralException (IBSError):
    pass

class LoginException (IBSError):
    pass


class IPpoolFullException(Exception):
    def __init__(self,_str):
	self._str=_str

    def __str__(self):
	return self._str


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
            	    self.write(str)
        
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

    if log_file & LOG_ERROR:
        error_log_handle.write(_str,add_stack)
    elif log_file & LOG_RADIUS:
	radius_log_handle.write(_str,add_stack)
    elif log_file & LOG_SERVER:
	server_log_handle.write(_str,add_stack)
    elif log_file & LOG_QUERY:
	query_log_handle.write(_str,add_stack)
    else:
	debug_log_handle.write(_str,add_stack)

def getExceptionText():
    """
	create and return text of last exception
    """
    (_type,value,tback)=sys.exc_info()
    return "".join(traceback.format_exception(_type, value, tback))

def logException(log_file,extra_str="",debug_level=0):
    err_text=getExceptionText()
    toLog(extra_str+"\n"+err_text,log_file,debug_level)
