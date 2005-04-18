from core.user import user_main
from core.ras import ras_main
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.sort import SortedList
from core.lib.date import *

def getFormattedOnlineUsers(date_type):
    """
	return a list of online user dics.
	return value is a list to be sortable
    """
    onlines_dic=user_main.getOnline().getOnlineUsersByRas()
    onlines=[]
    for (ras_id,unique_id) in onlines_dic:
	user_obj=onlines_dic[(ras_id,unique_id)]
	try:
		instance=user_obj.getInstanceFromUniqueID(ras_id,unique_id)
		if instance==None:
		    continue
	        instance_info=user_obj.getInstanceInfo(instance)
		report_dic={"user_id":user_obj.getUserID(),
	    	         "service":user_obj.getType(),
	    		 "ras_ip":ras_main.getLoader().getRasByID(instance_info["ras_id"]).getRasIP(),
			 "unique_id":instance_info["unique_id"],
			 "unique_id_val":instance_info["unique_id_val"],
			 "login_time":AbsDateFromEpoch(user_obj.getTypeObj().getLoginTime(instance)).getDate(date_type),
			 "login_time_epoch":user_obj.getTypeObj().getLoginTime(instance),
			 "duration_secs":time.time()-user_obj.getTypeObj().getLoginTime(instance),
			 "attrs":instance_info["attrs"],
			 "owner_id":user_obj.getLoadedUser().getBasicUser().getOwnerObj().getAdminID(),
			 "owner_name":user_obj.getLoadedUser().getBasicUser().getOwnerObj().getUsername(),
			 "current_credit":user_obj.calcCurrentCredit()
    			 }
		report_dic.update(user_obj.getTypeObj().getOnlineReportDic(instance))
	    	onlines.append(report_dic)
	except:
		logException(LOG_DEBUG)
		pass
    return onlines

def sortOnlineUsers(onlines,sort_by,desc):
    sort_by_list=["user_id","normal_username","login_time_epoch","duration_secs","in_bytes","out_bytes","ras_ip","owner_name","unique_id_val","voip_username"]
    if sort_by not in sort_by_list:
	sort_by="login_time_epoch"
    sorted_list=SortedList(onlines)
    sorted_list.sortByPostText("[\"%s\"]"%sort_by,desc)
    return sorted_list.getList()
