"""
    tc command line wrapper
"""
import os
from core.ibs_exceptions import *
class TC:
    def addQdisc(self,interface,*args):
	self.runTC("qdisc add dev %s %s"%(interface," ".join(args)))

    def delQdisc(self,interface,*args):
    	self.runTC("qdisc del dev %s %s"%(interface," ".join(args)))

    def addClass(self,interface,*args):
	self.runTC("class add dev %s %s"%(interface," ".join(args)))

    def changeClass(self,interface,*args):
	self.runTC("class change dev %s %s"%(interface," ".join(args)))

    def delClass(self,interface,*args):
    	self.runTC("class del dev %s %s"%(interface," ".join(args)))

    def addFilter(self,interface,*args):
	self.runTC("filter add dev %s %s"%(interface," ".join(args)))

    def delFilter(self,interface,*args):
    	self.runTC("filter del dev %s %s"%(interface," ".join(args)))

    def runTC(self,command):
	ret_val=os.system("%s %s"%(defs.BW_TC_COMMAND,command))
	if ret_val!=0:
	    toLog("tc command '%s %s' returned non zero value %s"%(defs.BW_TC_COMMAND,command,ret_val),LOG_DEBUG)

