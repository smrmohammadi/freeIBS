from core.ibs_exceptions import *
from core.lib.time_lib import *
import time

class Interval:
    """
	This class represent time intervals in multiple day of weeks
    """

    def __init__(self,day_of_week_container,start,end):
	"""
	    day_of_week_container(DayOfWeekContainer Instance)
	    start(Time Instance)
	    end(Time Instance)
	"""
	self.dow_container=day_of_week_container
	self.start=Time(start)
	self.end=Time(end)
	
    def __lt__(self,other):
	"""
	    other can be either Interval instance or integer that is seconds from morning
	    comparing is done, by comparing start_time of interval
	"""
	if isinstance(other,Interval):
	    return self.start<other.start
	else:
	    return self.getStartSeconds()<other


    def __gt__(self,other):
	"""
	    other can be either Interval instance or integer that is seconds from morning
	    comparing is done, by comparing end_time of interval
	"""
	if isinstance(other,Interval):
	    return self.end>other.end
	else:
	    return self.getEndSeconds()>other
    
    def containsToday(self):
	return self.__getTodayOfWeek() in self.dow_container
    
    def __getTodayOfWeek(self):
	"""
	    return integer representation of today of week
	"""
	return time.localtime()[6]
    
    def containsNow(self):
	now=secondsFromMorning()
	return self.containsToday() and self>now and self<now #don't panic interval greater than is checked with start, and less that is checked with end time

    def getStartSeconds(self):
	"""
	    return start time number of seconds from 0:0
	"""
	return self.start.getSecondsFromMorning()

    def getEndSeconds(self):
	"""
	    return end time number of seconds from 0:0
	"""
	return self.end.getSecondsFromMorning()

    def hasOverlap(self,other_interval):
	"""
	    check if this interval has overlap with other_interval.
	    Two intervals has conflict if they have overlap in times of same day
	"""
	if self.dow_container.hasOverlap(other_interval.dow_container):
	    if self.getStartSeconds() > other_interval.getStartSeconds() and other_interval.getEndSeconds() > self.getStartSeconds():
		return 1

	    elif self.getStartSeconds() < other_interval.getStartSeconds() and self.getEndSeconds() > other_interval.getStartSeconds():
		return 1

	    elif self.getStartSeconds() == other_interval.getStartSeconds():
		return 1

	return 0

