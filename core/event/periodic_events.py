from core.threadpool import thread_main
from core.event import event
from core.ibs_exceptions import *

def init():
    global pe_manager
    pe_manager=PeriodicEventsManager()

def postInit():
    getManager().postInit()
    
def getManager():
    return pe_manager


class PeriodicEvent:
    def __init__(self,name,interval,args,run_at_startup):
	"""
	    name(str): name string used for debugins
	    interval(int): interval seconds to run event
	    args(list): list of arguments
	    run_at_startup(int): if this flag is set, this event is run at ibs startup and next
				   run will be "interval" seconds.
				   if this flag isn't set, first function run will be in "interval"
				   seconds, and it doesn't run on startup
				   if run_at_startup is 1, self.run will run on a new thread
				   if run_at_startup is 2, self.run will run on main thread, and ibs won't
				      completely start until it finishes
	    
	"""
	self.interval=interval
	self.args=args
	self.run_at_startup=run_at_startup


    def run_startup(self,*args):
	"""
	    if self.run_at_startup flag is set, this method will be called at ibs startup
	    the default is call self.run method with arguments, but it may have diffrent
	    implemention. Children may override this method too
	"""
	apply(self.run,args)

    def run(self,*args):
	"""
	    run this event, children must override this method and implement the job
	    this event should do. run method calls periodicly in interval self.interval
	    if self.run_at_startup flag is set, run_startup method is called at ibs start, and
	    run method will be called periodicly after it.
	"""
	pass
    

class PeriodicEventsManager:
    def __init__(self):
	self.events=[]

    def register(self,periodic_event):
	"""
	    register "periodic_event" to run periodicly
	    periodic_event(PeriodicEvent instance): Periodic event to run 
	"""
	if not isinstance(periodic_event,PeriodicEvent):
	    raise IBSException("PeriodicEventManager.register needs an PeriodicEvent Instance")
	self.events.append(periodic_event)

    
    def postInit(self):
	"""
	    this function will be called, after initialization of all other modules
	"""
	self.__setStartupEvents()
	
    def runEvent(self,_index,*args):
	try:
	    ev=self.events[_index]
	except:
	    logException(LOG_ERROR,"periodicEvents.runEvent Invalid index %s"%_index)
	else:
	    try:
		apply(ev.run,args)
	    except:
		logException(LOG_ERROR,"periodicEvents.runEvent exception for method: %s args: %s"%
										(ev.name,ev.args))
	self.__setNextEvent(_index)

    def __setStartupEvents(self):
	for _index in range(len(self.events)):
	    ev=self.events[_index]
	    if ev.run_at_startup==1:
	        thread_main.runThread(ev.run,ev.args,"event")
	    elif ev.run_at_startup==2:
		apply(ev.run,ev.args)
	    
	    self.__setNextEvent(_index)

    def __setNextEvent(self,_index):
	ev=self.events[_index]
	event.addEvent(ev.interval,self.runEvent,[_index]+ev.args)
