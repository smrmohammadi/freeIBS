class SortedList:
    def __iter__(self):
	return iter(self.list)

    def __getitem__(self,_index):
	return self.list[_index]
    
    def __init__(self,list):
	self.list=list

    def sortByIndex(self,_index,desc):
	"""
	    Sort list by value of objects of index of list !
	    list should be a list of lists then
	"""
	return self.sortByPostText("[%s]"%_index,desc)

    def sortByPostText(self,post_text,desc):
	"""
	    Sort list using post_text after each item of list
	    ex. if list is [[1,2,3],[2,3,4]] and we want to sort the list with first item of
	    each member, post_text is "[0]" so for each member we compare m[0]s
	"""
	
	return self.__sort(post_text,"",desc)

    def sort(self,desc):
	"""
	    sort the internal list
	    desc show descending flag
	"""
	self.__sort("","",desc)
        
    def __sort(self,post_text,pre_text,desc):
        
	def __sortFunc(m1,m2):
	    m1_val=eval("%sm1%s"%(pre_text,post_text))
	    m2_val=eval("%sm2%s"%(pre_text,post_text))
	    return cmp( m1_val , m2_val )
	
	self.list.sort(__sortFunc)
	if desc:
	    self.list.reverse()

    def getList(self):
	"""
	    get sorted list after calling self.sort* methods
	"""
	return self.list	    


class SortedDic:
    def __init__(self,dic):
	self.dic=dic
	self.sorted_list=SortedList(self.__dic2list(dic))
    
    def __dic2list(self,dic):
	"""
	    convert the dic into a list by creating and array and put the key of dic in first index and
	    dic value in second index
	    summary: {x:y,z:c}->[[x,y],[z,c]]
	"""
	return map(lambda x:[x,dic[x]],dic)

    def sortByKey(self,desc):
	self.sortByPostText("[0]",desc)
	
    def sortByPostText(self,post_text,desc):
	self.sorted_list.sortByPostText(post_text,desc)    

    def getList(self):
	"""
	    return sorted list produced from dic. to understand list format see __dic2list
	"""
	return self.sorted_list.getList()

####NOT CHECKED
	
def sortListWithHash(list,order_by,order_by_hash,default,desc):
    """
	sort "list" by "order_by" using "order_by_hash" to determine index or "postText"
	"order_by_hash" is a hash in format {order_by_name=>postText of list}
	ex. list is [[index,connect_time],...] order_by_hash {index:"[0]",connect_time:"[1]"}
	default is used if "order_by" argument is not in "order_by_hash" hash
	desc is a boolean "0" or "1"
    """
    if order_by_hash.has_key(order_by):
	return sortList(list,order_by_hash[order_by],"",desc)
    else:
	return sortList(list,order_by_hash[default],"",desc)