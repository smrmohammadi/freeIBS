from core.lib.sort import SortedList

class Tariff:
    def __init__(self,tariff_id,tariff_name,comment,prefixes):
	"""
	    tariff_id(integer): unique id of tariff
	    prefixes(list of Prefix instances): list of Prefix instances containing all Prefixes
	"""
	self.tariff_id=tariff_id
	self.tariff_name=tariff_name
	self.comment=comment
	self.prefixes_code={} #prefix_code=>obj
	self.prefixes_id={} #prefix_id=>obj
	self.__addPrefixes(prefixes)
	
    def __addPrefixes(self,prefixes):
	for prefix in prefixes:
	    self.prefixes_code[prefix.getPrefixCode()]=prefix
	    self.prefixes_id[prefix.getPrefixID()]=prefix
    
    ###################################
    def getTariffID(self):
	return self.tariff_id
	
    def getTariffName(self):
	return self.tariff_name

    ###################################
    def getPrefixByCode(self,code):
	try:
	    return self.prefixes_code[code]
	except KeyError:
	    raise GeneralException(errorText("VOIP_TARIFF","TARIFF_DOESNT_HAVE_PREFIX_CODE")%(self.getTariffName(),code))
	    
    def hasPrefixCode(self,code):
	return self.prefixes_code.has_key(code)
    
    ###################################
    def getPrefixByID(self,_id):
	try:
	    return self.prefixes_id[_id]
	except KeyError:
	    raise GeneralException(errorText("VOIP_TARIFF","TARIFF_DOESNT_HAVE_PREFIX_ID")%(self.getTariffName(),_id))
    
    def hasPrefixID(self,_id):
	return self.prefixes_id.has_key(_id)

    ####################################
    def getInfo(self,include_prefixes=False):
	info={"tariff_id":self.getTariffID(),
	      "tariff_name":self.getTariffName(),
	      "comment":self.comment}
	
	if include_prefixes:
	    info["prefixes"]=self.__getPrefixesInfo()

	return info

    def __getPrefixesInfo(self):
	prefixes=map(lambda prefix:prefix.getInfo(),self.prefixes_id.itervalues())
	sorted=SortedList(prefixes)
	sorted.sortByPostText("['prefix_name']",False)
	return sorted.getList()
    #####################################
    def findPrefix(self,called_number):
	"""
	    find and return Prefix Object for called_number. Prefix is selected using longest match algorithm.
	    return None if called_number has no defined prefix
	    XXX: using sequential search!
	"""
	longest_len=0
	longest_code=""
	for code in self.prefixes_code.iterkeys():
	    if called_number.startswith(code) and len(code)>longest_len:
		longest_len=len(code)
		longest_code=code
    
	if longest_len:
	    return self.getPrefixByCode(longest_code)
	else:
	    return None
	    
	
class Prefix:
    def __init__(self,prefix_id,prefix_code,prefix_name,cpm,free_seconds,min_duration,round_to):
	"""
	    cpm(float): charge per minute
	    free_seconds(int): number of free seconds for this prefix. free seconds doesn't count as
				user duration
	    min_duration(int): if duration of call is less than this, it's supposed to be missed call
	    round_to(int): round duration of calls to this destination , to this amount of seconds
	    
	"""
	self.prefix_id=prefix_id
	self.prefix_code=prefix_code
	self.prefix_name=prefix_name
	self.cpm=cpm
	self.free_seconds=free_seconds
	self.min_duration=min_duration
	self.round_to=round_to    

    def getPrefixCode(self):
	return self.prefix_code
	
    def getPrefixName(self):
	return self.prefix_name	
    
    def getPrefixID(self):
	return self.prefix_id

    def getCPM(self):
	return self.cpm
	
    def getFreeSeconds(self):
	return self.free_seconds

    def getMinDuration(self):
	return self.min_duration

    def getRoundTo(self):
	return self.round_to
    
    def getInfo(self):
	return {"prefix_id":self.getPrefixID(),
		"prefix_code":self.getPrefixCode(),
		"prefix_name":self.getPrefixName(),
		"cpm":self.getCPM(),
		"free_seconds":self.getFreeSeconds(),
		"min_duration":self.getMinDuration(),
		"round_to":self.getRoundTo()
		}