import threading
import time
import traceback
import sys
from core import defs
from core.threadpool import thread_main
from core.ibs_exceptions import *

#priority 100 is for shutdown process

class Scheduler:
    eventObj=None
    __events=None
    tlock=None
    MAX_WAIT_TIME=30 #secs
    
    def __init__(self):
	self.tlock=threading.RLock()
	self.eventObj=threading.Event()
	self.eventObj.clear()
	self.__events=[]
    
    def loop(self):
	while 1:
	    next_evt=self.nextEvent()
	    if next_evt<=0:
		self.doEvent()
		continue
	    self.eventObj.wait(next_evt)
	    self.eventObj.clear()

    def __getEventIndex(self,time_to_run,priority):
        i=0
    	for i in range(len(self.__events)): #sequential search, list is sorted, so there are better 
	    if self.__events[i]["timeToRun"]==time_to_run:
		if priority > self.__events[i]["priority"]:
		    i-=1
		    break
		else:
		    break
	    elif self.__events[i]["timeToRun"]>time_to_run:
		break
	return max(i,0)

    def addEvent(self,secs_from_now,method,args,priority):
	"""
	    add a new event to event schedueler
	    secs_from_now(integer): seconds from now that the event will be run
	    method(Callable object): method that will be called
	    args(list): list of arguments passed to method
	    priority(integer): priority of job. Greater numbers favored more. it should be less than 20
	    		       priority 100 is reserved for shutdown method
	"""
	time_to_run=self.now()+secs_from_now
        self.tlock.acquire() 
        try:
	    if priority==100:
		new_event_index=0
	    else:
	        new_event_index=self.__getEventIndex(time_to_run,priority)
	    self.__events.insert(new_event_index,{"timeToRun":time_to_run,
						  "method":method,
						  "args":args,
						  "priority":priority})
	finally:
	    self.tlock.release()
	    if new_event_index==0:
	        self.eventObj.set() 

    def nextEvent(self): #no locking, return time to next event
            self.tlock.acquire()
            try:
                if len(self.__events) >0:
                    t=self.__events[0]["timeToRun"]-self.now()
                else:
                    t=self.MAX_WAIT_TIME
            finally:
                self.tlock.release()
                    
	    if t>self.MAX_WAIT_TIME:
		return self.MAX_WAIT_TIME
	    return t

    def removeEvent(self,method,args): #inefficient way
	self.tlock.acquire()
	entry_found=0
	try:
	    for i in self.__events:
		if i["method"]==method and i["args"]==args:
		    self.__events.remove(i)
		    entry_found=1
		    break
	finally:
	    self.tlock.release()
	
	if not entry_found:
	    toLog("event.removeEvent: Couldn't found event to delete %s %s"%(method,args),LOG_DEBUG,defs.DEBUG_ALL)
	
    def doEvent(self):
	self.tlock.acquire()
	try:
		job=self.__events.pop(0)
	finally:
	    self.tlock.release()
	
	if defs.LOG_EVENTS:
	    toLog("Event Scheduler: Running Method:%s Arguments: %s"%(job["method"],job["args"]),LOG_DEBUG)
	
	if job["priority"]==100: #run shutdown method in main thread, not a new thread
            apply(job["method"],job["args"])
	else:
    	    try:
            	thread_main.runThread(job["method"],job["args"],"event")
    	    except:
        	logException(LOG_ERROR,"Unhandled exception on event loop")
	
    def now(self):
	return int(time.time())

    def printMe(self):
        for evt in self.__events:
	    print evt

def initSched():
    global sched
    sched=Scheduler()

def addEvent(secsFromNow,method,args,priority=0):
    sched.addEvent(secsFromNow,method,args,priority)

def removeEvent(method,args):
    sched.removeEvent(method,args)

def startLoop():
    sched.loop()

