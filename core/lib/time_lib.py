from core.lib.general import *
from core.errors import errorText
from core.ibs_exceptions import *
import time

def dbTimeFromEpoch(epoch_time):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(epoch_time))


#############################33
def cur_day_of_week():
    return time.localtime()[6]
    
def dbTimeToEpoch(dbTime):
    return time.mktime(dbTimeToList(dbTime))

def dbTimeToList(dbTime):
    dot=dbTime.find(".")
    if dot ==-1:
	plus=dbTime.find("+") #old postgresqls date representation
	if plus==-1:
	    dot=len(dbTime)
	else:
	    dot=plus
    
    try:
	ret=list(time.strptime(dbTime[:dot],"%Y-%m-%d %H:%M:%S"))
	ret[8]=0
	return ret
    except:
	logException()
	raise generalException("Invalid dbTime: " + str(dbTime))
	

def getEpochTimeFromHourOfDay(hour,_min=0,sec=0,dayToAdd=0):
    tm=list(time.localtime())
    tm[3]=hour
    tm[4]=_min
    tm[5]=sec
    tm[2]+=dayToAdd
    
    return time.mktime(tm)

def epochTimeFromRadiusTime(rad_time):
    sp=rad_time.split()
    if sp[0].startswith('.') or sp[0].startswith('*'):
        sp[0]=sp[0][1:]
    formatted_time=sp[5]+ " " + sp[3] + " " + sp[4] + " " + sp[0][:sp[0].find('.')]

    time_list=list(time.strptime(formatted_time,'%Y %b %d %H:%M:%S'))
    time_list[8]=-1 #daylight saving flag
    epoch=time.mktime(time_list)
    return epoch
    

def epochTimeFromRadiusUTCTime(rad_time):
    return epochTimeFromRadiusTime(rad_time)-time.timezone

def timeConditionToEpoch(condValue,condType,now=0):
    if now==0:
	now = time.time()
	
    #just because from and to conditions are somehow similar
    #convert "to" conditions to "from", then negate the condValue
    if condType.startswith("to"):
	condType = "from" + condType[2:]
	if condType != "from":
	    if condValue.startswith("-"):
		condValue = condValue[1:]
	    else:
		condValue = "-" + condValue
	
	
    if condType=="fromDays":
	return now - (integer(condValue) * 24 * 60 * 60)

    if condType=="fromYears":
	return now - (integer(condValue) * 365 * 24 * 60 * 60)

    if condType=="fromMonths":
	return now - (integer(condValue) * 30 * 24 * 60 * 60)

    if condType=="fromHours":
	return now - (integer(condValue) * 60 * 60)

    if condType=="from":
	return dbTimeToEpoch(condValue+" 0:0:0")
    
    raise generalException("timeCondition: invalid condition")


def getDurationInSec(duration,unit):
    duration=integer(duration)
    if unit=="seconds":
	return duration
    elif unit=="minutes":
	return duration*60
    elif unit=="hours":
	return duration*3600
    elif unit=="days":
	return duration*3600*24
    else:
	raise generalException("Invalid duration unit %s"%unit)

def secondsFromMorning():
    """
	return number of seconds from 00:00:00 of today
    """
    tm=time.localtime()
    return tm[3]*3600+tm[4]*60+tm[5] # now , elapsed seconds from 00:00:00 of today


class Time:
    """
	Time class provoid method to handle time types
    """
    def __init__(self,time_str):
	"""
	    time_str(string): string representing time. it may be not fully described time 
			      ex. 12, 12:3, 12:30:12 are valid inputs
	
	    This method may raise GeneralException on bad time_strs
	    Genrated Exceptions doesn't containg key, as described in errors.errorText	
	"""
	self.time_str=time_str
	(self.formatted_time,self.hour,self.minute,self.second)=self.__formatTime(time_str)


    def __cmp__(self,time_obj):
	return cmp(self.getSecondsFromMorning(),time_obj.getSecondsFromMorning())

    def __formatTime(self,time_str):
	"""
	    check if time_str is valid and complete it if necessary
    	    for ex. it will change 12:30 to 12:30:00 and 12 to 12:00:00
	    raise an general exception on error
	    return completed time_str on success
	"""
	time_str=self.__completeTime(time_str)
	(hour,minute,second)=map(int,time_str.split(":"))
	if hour>24 or hour<0 or minute>60 or minute<0 or second>60 or second<0:
    	    raise GeneralException(errorText("GENERAL","TIME_OUT_OF_RANGE",0))
	return (time_str,hour,minute,second)

    def __completeTime(self,time_str):
	if time_str=="24":
	    time_str="23:59:59"
	elif re.match("^[0-9]{1,2}$",time_str):
    	    time_str="%s:00:00"%time_str
	elif re.match("^[0-9]{1,2}:[0-9]{1,2}$",time_str):
    	    time_str="%s:00"%time_str
	elif re.match("^[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}$",time_str):
    	    pass
	else:
    	    raise GeneralException(errorText("GENERAL","INVALID_TIME_STRING",0)%time_str)

	return time_str

    def getSecondsFromMorning(self):
	return self.hour*3600+self.minute*60+self.second

    def getFormattedTime(self):
	return self.formatted_time

