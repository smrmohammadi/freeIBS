from core.admin.admin_perm import *
from core.admin import perm_loader

def init():
    perm_loader.getLoader().registerPerm("CHANGE NORMAL USER ATTRIBUTES",ChangeNormalUserAttrs)

class ChangeNormalUserAttrs (AllRestrictedSingleValuePermission,UserCatPermission,Permission):
    def init(self):
	self.setDescription("""	Can Change Normal User Attributes
		This Permission Allows admins to add,change or delete users normal attributes
		such as normal username, normal password and normal charge rule
		Normal attributes are commonly used for dialup users
		Related Permissions: ADD NEW USER, CHANGE USER OWNER, CHANGE USER ATTRIBUTES
	       """)
	self.addAffectedPage("User->Edit Attributes")
	self.addDependency("CHANGE USER ATTRIBUTES")

	