class Group:
    def __init__(self,group_id,group_name,comment,owner_id,attributes):
	self.group_id=group_id
	self.group_name=group_name
	self.comment=comment
	self.owner_id=owner_id
	self.attributes=attributes
	
    def hasAttr(self,attr_name):
	return self.attributes.has_key(attr_name)

    def getAttr(self,attr_name):
	try:
	    return self.attributes[attr_name]
	except KeyError:
	    raise GeneralException(errorText("GENERAL","ATTR_NOT_FOUND")%attr_name)

    def getGroupName(self):
	return self.group_name

    def getGroupID(self):
	return self.group_id

    def getComment(self):
	return self.comment

    def getOwnerID(self):
	return self.owner_id

    def getAttrs(self):
	return self.attributes

