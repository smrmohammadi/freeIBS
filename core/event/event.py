import threading
import time
import traceback
import sys
from core.threadpool import thread_main
from core.ibs_exceptions import *

#priority -100 is for shutdown process

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
		if priority < self.__events[i]["priority"]:
		    i-=1
		    break
		else:
		    break
	    elif self.__events[i]["timeToRun"]>time_to_run:
		i-=1
		break
    	    i+=1
	return i

    def addEvent(self,secs_from_now,method,args,priority):
	time_to_run=self.now()+secs_from_now
	new_event_index=0

        self.tlock.acquire() 
        try:
	    if priority==-100:
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
	
	if job["priority"]==-100: #run shutdown method in main thread, not a new thread
            apply(job["method"],job["args"])
	else:
    	    try:
            	thread_main.runThread(job["method"],job["args"],"event")
    	    except:
        	logException(LOG_ERROR,"Unhandled exception on event loop")
	
    def now(self):
	return int(time.time())

    def printMe(self):
        print self.__events

def initSched():
    global sched
    sched=Scheduler()

def addEvent(secsFromNow,method,args,priority=0):
    global sched
    sched.addEvent(secsFromNow,method,args,priority)

def removeEvent(method,args):
    global sched
    sched.removeEvent(method,args)

def startLoop():
    global sched
    sched.loop()
    