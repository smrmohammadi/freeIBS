from core.lib import jalali
from core.lib.general import *
from core.ibs_exceptions import *
from core.errors import errorText
import time_lib
import time
import re

class RelativeDate:
    def __init__(self,date,unit):
	"""
	    date(integer): date number
	    unit(string): unit of date
	    can be on of :"Seconds", "Hours", "Days","Months","Years"
	"""
	self.date=to_int(date,"relative date")
	self.factor=self.__getUnitFactor(unit)
	self.date_seconds=self.date*self.factor

    def __getUnitFactor(self,unit):
	"""
	    return factor for unit type to convert date to hours
	    so, factor for hours is 1 , for days is 24 and so on..
	"""
	factor=1
	if unit=="Seconds":
	    return factor
	factor*=3600
	if unit=="Hours":
	    return factor
	factor*=24
	if unit=="Days":
	    return factor
	factor*=30
	if unit=="Months":
	    return factor
	factor*=365
	if unit=="Years":
	    return factor
	else:
	    raise GeneralException(errorText("GENERAL","INVALID_REL_DATE_UNIT")%unit)

    def __findUnit(self,date):
	"""
	    find which unit is suitable for "date"
	    date is an integer containing relative date with unit "Seconds"
	"""
	if date%(3600) or date<(3600*24):
	    return "Hours"
	elif date%(3600*24) or date<(3600*24*30):
	    return "Days"
	elif date%(3600*24*30):
	    return "Months"
	else:
	    return "Years"

    def check(self):
	"""
	    check the value of date, raise an exception on error
	"""
	if self.date_seconds>3600*24*30*365*20: #20 years!
	    raise GeneralException(errorText("GENERAL","INVALID_REL_DATE")%self.date)
	
    def getDateSeconds(self):
	return self.date_seconds

    def getDBDate(self):
	"""
	    return date(integer) useful for inserting in database.
	    it's the date in number of seconds
	"""
	return self.getDateSeconds()
	
    def getFormattedDate(self):
	"""
	    return tuple of (rel_date,rel_date_units) ex. (14,"Hours")
	    Automatcally choose best unit for date
	"""
	unit=self.__findUnit(self.date_seconds)
	factor=self.__getUnitFactor(unit)
	return (self.date_seconds/factor,unit)
	

class AbsDate:
    split_pattern=re.compile("[\-/]")
    def __init__(self,date,date_type):
	"""
	    "date" can be in format of
	    YYYY-MM-DD HH:MM:SS
	    YYYY-MM-DD HH:MM
	    YYYY-MM-DD HH
	    YYYY-MM-DD

	    "date_type" can be one of:
		jalali
		gregorian
	"""
	self.date=date
	self.date_type=date_type
	self.__load()
	
    def __splitDate(self):
	"""
	    split self.date to its components 
	    return a list of (year,month,day,hour,minute,second) or raise an exception if
	    it can't parse the date
	"""
	try:
	    date_sp=self.date.strip().split()
	    if len(date_sp)==2:
		time_sp=date_sp[1].split(":")
		if len(time_sp)>3:
		    raise GeneralException(errorText("GENERAL","INVALID_DATE")%self.date)
		hour=int(time_sp[0])
		if len(time_sp)>=2:
		    minute=int(time_sp[1])
		else:
		    minute=0
		
		if len(time_sp)==3:
		    dot_index=time_sp[2].find(".")
		    if dot_index!=-1:
			time_sp[2]=time_sp[2][:dot_index]
		    second=int(time_sp[2])
		else:
		    second=0
	    elif len(date_sp)==1:
		hour=0
		minute=0
		second=0
	    else:
		raise GeneralException(errorText("GENERAL","INVALID_DATE")%self.date)
	
	    (year,month,day)=map(int,self.split_pattern.split(date_sp[0]))
	except ValueError:
	    raise GeneralException(errorText("GENERAL","INVALID_DATE")%self.date)
	
	return (year,month,day,hour,minute,second)

    def __load(self):
	(year,month,day,hour,minute,second)=self.__splitDate()
	self.__checkDateValues(year,month,day,hour,minute,second)
	if self.date_type=="jalali":
	    self.jyear=year
	    self.jmonth=month
	    self.jday=day
	elif self.date_type=="gregorian":
	    self.gyear=year
	    self.gmonth=month
	    self.gday=day
	else:
	    raise GeneralException(errorText("GENERAL","INVALID_DATE_TYPE")%self.date_type)
	self.hour=hour
	self.minute=minute
	self.second=second

    def __checkDateValues(self,year,month,day,hour,minute,second):
	"""
	    check date values and ranges
	"""
	if year<1200 or year > 2500 or month<1 or month>12 or day<1 or day>31 or hour <0 or hour >= 24 or \
	   minute<0 or minute>=60 or second<0 or second>=60:
	    raise GeneralException(errorText("GENERAL","INVALID_DATE")%self.date)

    def getGregorianDateList(self):
	if self.date_type=="jalali" and not hasattr(self,"gyear"):
	    (self.gyear,self.gmonth,self.gday)=self.__getGregorianFromJalali()
	return (self.gyear,self.gmonth,self.gday,self.hour,self.minute,self.second)
	
    def getJalaliDateList(self):
	if self.date_type=="gregorian" and not hasattr(self,"jyear"):
	    (self.jyear,self.jmonth,self.jday)=self.__getJalaliFromGregorian()
	return (self.jyear,self.jmonth,self.jday,self.hour,self.minute,self.second)


    def __getGregorianFromJalali(self):
	jalali_to_greg=jalali.JalaliToGregorian(self.jyear,self.jmonth,self.jday)
	return jalali_to_greg.getGregorianList()

    def __getJalaliFromGregorian(self):
	greg_to_jalali=jalali.GregorianToJalali(self.gyear,self.gmonth,self.gday)
	return greg_to_jalali.getJalaliList()
    
    def getGregorianDate(self):
	"""
	    return string representation of gregorian date in format
	    YYYY-MM-DD hh:mm
	"""
	return apply(self.__getFormattedDate,self.getGregorianDateList())

    def getJalaliDate(self):
	return apply(self.__getFormattedDate,self.getJalaliDateList())

    def __getFormattedDate(self,year,month,day,hour,minute,second):
	return "%s-%s-%s %s:%s"%(year,
				 self.__zeroLeftPadTo(month,2),
				 self.__zeroLeftPadTo(day,2),
				 self.__zeroLeftPadTo(hour,2),
				 self.__zeroLeftPadTo(minute,2))

    def __zeroLeftPadTo(self,_str,_len):
	_str=str(_str)
	while len(_str)!=_len: _str="0%s"%_str
	return _str

    def getEpochDate(self):
	return long(time.mktime(self.getGregorianDateList()+(0,0,0)))

    def getDate(self,_type):
	if _type=="epoch":
	    return self.getEpochDate()
	elif _type=="jalali":
	    return self.getJalaliDate()
	else:
	    return self.getGregorianDate()
	

class AbsDateWithUnit(AbsDate):
    def __init__(self,date,date_unit):
	date_unit=date_unit.lower()
	if date_unit in ["jalali","gregorian"]:
	    AbsDate.__init__(self,date,date_unit)
	else:
	    date=time_lib.dbTimeFromEpoch(time.time()+self.__getDateInSeconds(date,date_unit))
	    AbsDate.__init__(self,date,"gregorian")
	
    def __getDateInSeconds(self,date,date_unit):
	unit_table={"minutes":60,"hours":3600,"days":24*3600,"months":24*3600*30,"years":24*3600*30*365}

	try:
	    date=float(date)
	except ValueError:	
    	    raise GeneralException(errorText("GENERAL","INVALID_DATE")%date)

	try:
	    return unit_table[date_unit]*date
	except KeyError:
	    raise GeneralException(errorText("GENERAL","INVALID_DATE_UNIT")%date_unit)
	    


def AbsDateFromEpoch(epoch_time):
    	return AbsDate(time_lib.dbTimeFromEpoch(epoch_time),"gregorian")
	