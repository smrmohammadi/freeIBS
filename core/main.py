import traceback
import sys
import time
import ibs_exceptions
from core.lib.general import *

SHUTDOWN=False
NO_LOGIN=True

def init():
    ibs_exceptions.init()
    ibs_exceptions.toLog("IBS starting...",ibs_exceptions.LOG_DEBUG)
    unSetShutdownFlag()
    setStartingFlag()

    from core.threadpool import thread_main
    thread_main.init()

    import core.plugins.plugin_loader
    core.plugins.plugin_loader.init()

    from core.event import event
    event.initSched()

    import core.event.daily_events
    core.event.daily_events.init()

    import core.event.periodic_events
    core.event.periodic_events.init()

    from core.db import db_main
    db_main.init()

    import core.defs
    core.defs.init()

    from core.server import server
    server.init()    


    import core.admin.admin_main
    core.admin.admin_main.init()

    import core.login.login_main
    core.login.login_main.init()

    import core.defs_lib.defs_main
    core.defs_lib.defs_main.init()

    import core.charge.charge_main
    core.charge.charge_main.init()

    import core.group.group_main
    core.group.group_main.init()

    import core.user.user_main
    core.user.user_main.init()

    import core.util.util_main
    core.util.util_main.init()
    
    import core.ippool.ippool_main
    core.ippool.ippool_main.init()

    import core.report.report_main
    core.report.report_main.init()
    
    import core.bandwidth_limit.bw_main
    core.bandwidth_limit.bw_main.init()

    import core.ras.ras_main
    core.ras.ras_main.init()

    import radius_server.rad_server
    radius_server.rad_server.init()
    
    ibs_exceptions.toLog("Starting server",ibs_exceptions.LOG_DEBUG)
    server.startServer()    

    ibs_exceptions.toLog("Modules Initialized, Entering Post Inits",ibs_exceptions.LOG_DEBUG)
    runPostInits()

    unSetNoLoginFlag()
    ibs_exceptions.toLog("IBS successfully started.",ibs_exceptions.LOG_DEBUG)
    sys.excepthook=sys_except_hook

    unsetStartingFlag()
    
############################################
post_init_methods=[]

def runPostInits():
    for method in post_init_methods:
	apply(method,[])

def registerPostInitMethod(method):
    post_init_methods.append(method)

#######################
def mainThreadShutdown(): 
    """
	XXX to be fixed later
	we must call this in main event loop(main thread)
    """
    ibs_exceptions.toLog("Shutting down @ %s"%time.localtime(),ibs_exceptions.LOG_DEBUG)
    setNoLoginFlag()
    setShutdownFlag()
    import radius_server.rad_server
    radius_server.rad_server.shutdown()
    from core.server import server    
    server.shutdown()
    from core.threadpool import thread_main
    thread_main.shutdown(10)
    from core.db import db_main
    db_main.shutdown()
    thread_main.shutdown(30)
    sys.exit(0)

def shutdown():
    event.addEvent(0,mts,[],-100)
########################    
    
def isShuttingDown(): #check for this in long last jobs, and see wether we must release out thread
    return SHUTDOWN
    
def setShutdownFlag():
    global SHUTDOWN
    SHUTDOWN=True

def unSetShutdownFlag():
    global SHUTDOWN
    SHUTDOWN=False

def noLoginSet():
    return NO_LOGIN

def setNoLoginFlag():
    global NO_LOGIN
    NO_LOGIN=True

def unSetNoLoginFlag():
    global NO_LOGIN
    NO_LOGIN=False

def isStarting():
    return STARTING

def setStartingFlag():
    global STARTING
    STARTING=True

def unsetStartingFlag():
    global STARTING
    STARTING=False

def sys_except_hook(_type,value,tback):
    ibs_exceptions.toLog("Unhandled sys exception :%s %s " %(_type,value),ibs_exceptions.LOG_ERROR)
    ibs_exceptions.toLog("".join(traceback.format_exception(_type, value, tback)),ibs_exceptions.LOG_ERROR)
