from core.ibs_exceptions import *
from core.server import handler
from core.lib.multi_strs import MultiStr
import sys
import os
import traceback

class UtilHandler(handler.Handler):
    def __init__(self):
	handler.Handler.__init__(self,"util")
	self.registerHandlerMethod("multiStrGetAll")
	self.registerHandlerMethod("runDebugCode")


    def multiStrGetAll(self,request):
    	request.checkArgs("str")
	return map(lambda x:x,MultiStr(request["str"]))

    def runDebugCode(self,request):
	request.needAuthType(request.ADMIN)
	request.checkArgs("command")
	requester=request.getAuthNameObj()
	if not requester.isGod():
	    return "Access Denied"

	import pty
	out=""
	(pid,fd)=pty.fork()
	if pid==0:
	    try:
	        exec request["command"]
	    except:
	        (_type,value,tback)=sys.exc_info()
	        print "".join(traceback.format_exception(_type, value, tback))
	    
	    os._exit(0)
	else:
	    out=""
	    while 1:
		(exit_pid,exit_status)=os.waitpid(pid,os.WNOHANG)

		try:
    		    out+=os.read(fd,1024)
    		except OSError:
    		    pass

		if exit_pid==pid:
		    break

	    return out

