from core.threadpool import threadpool,twrapper
from core import defs


def init():
    threadpool.initThreadPool()
    init_wrappers()

def init_wrappers():
    global main_twrapper,server_twrapper,event_twrapper,radius_twrapper
    main_twrapper=twrapper.ThreadPoolWrapper(defs.MAX_OTHER_THREADS,"main")
    server_twrapper=twrapper.ThreadPoolWrapper(defs.MAX_SERVER_THREADS,"server")
    event_twrapper=twrapper.ThreadPoolWrapper(defs.MAX_EVENT_THREADS,"event")
    radius_twrapper=twrapper.ThreadPoolWrapper(defs.MAX_RADIUS_THREADS,"radius")


def shutdown(seconds):
    threadpool.getThreadPool().shutdown(seconds)
    
def runThread(method,args,wrapper_name="main"):
    if wrapper_name=="server":
	server_twrapper.runThread(method,args)
    elif wrapper_name=="event":
	event_twrapper.runThread(method,args)
    elif wrapper_name=="radius":
	radius_twrapper.runThread(method,args)
    else:
	main_twrapper.runThread(method,args)
