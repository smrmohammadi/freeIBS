#!/usr/bin/python -OO
print "importing required files ..."
import signal
import sys
import os
import syslog
import traceback
from core.debug import thread_debug
from core.event import event
import core.main


def termSigHandler(signum,frame):
    main.mainThreadShutdown()
    sys.exit(0)
    
def childWaitSigHandler(signum,frame):
    if signum==signal.SIGUSR1: #successfully started
	print "IBSng started successfully!"
	sys.exit(0)
    else:
	print "IBSng Failed to start!"
	sys.exit(1)
	
def handleUserDefinedSignals(handler):
    signal.signal(signal.SIGUSR1,handler)
    signal.signal(signal.SIGUSR2,handler)

def mainThreadInitialize():
    mainThreadSignalHandlers()
    print "Calling Initializer routins"
    thread_debug.debug_me()
    core.main.init()

def mainThreadSignalHandlers():
    handleUserDefinedSignals(signal.SIG_IGN)
    signal.signal(signal.SIGTERM,termSigHandler)
    signal.signal(signal.SIGHUP,signal.SIG_IGN)

def logToSysLog():
    syslog.openlog("IBSng",syslog.LOG_DAEMON)
    (_type,value,tback)=sys.exc_info()
    syslog.syslog(syslog.LOG_ERR,
		  "".join(traceback.format_exception(_type, value, tback)))
    syslog.closelog()
    

def start():
    handleUserDefinedSignals(childWaitSigHandler)
    print "forking ..."
    pid=os.fork()
    print "IBSng started with pid=%d"%pid
    if pid == 0:
	try:
	    try:
		mainThreadInitialize()
	        os.kill(os.getppid(),signal.SIGUSR1)
	    except:
		print "Shutting down on error"
	        os.kill(os.getppid(),signal.SIGUSR2)
		raise
	    print "Successfully initialized, entering event loop ..."
    	    event.startLoop()
	except:
#	    core.main.mainThreadShutdown()
	    logToSysLog()	    	
	    
    else:
	signal.pause()

start()    