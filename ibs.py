#! /usr/bin/python -O
print "importing required files ..."
import signal
import sys
import os
from core.debug import thread_debug
from core.event import event
import core.main


def sigHandler(signum,frame):
    main.mainThreadShutdown()
    sys.exit()

print "forking ..."
pid=os.fork()
print "IBS started with pid=%d"%pid
if pid == 0:
    try:
	print "overriding signal handlers ..."
        signal.signal(signal.SIGTERM,sigHandler)
        signal.signal(signal.SIGHUP,signal.SIG_IGN)
	print "calling main.init..."
	thread_debug.debug_me()
        core.main.init()
	print "Successfully initialized, entering event loop ..."
        event.startLoop()
    finally:
#	core.main.mainThreadShutdown()
	print "Shutting down"
	
