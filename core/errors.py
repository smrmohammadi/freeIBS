from core.ibs_exceptions import *

GENERAL_ERRORS={
    "NO_ERROR_TEXT":"Can't find Error Text",
    "USER_NOT_FOUND":"User not found",
    "NOT_ONLINE":"User %s is not online on %s , %s", #arguments username,ras_ip,port
    "INVALID_AUTH_TYPE":"Invalid Authentication type",
    "INTERNAL_ERROR":"Internal Error",
    "RANGE_ERROR":"Invalid range",
    "RANGE_END_LESS_THAN_START":"%s Range End is equal or less than Start",
    "RANGE_IS_TOO_LARGE":"%s Range is too large",
    "INVALID_CREDIT_LOG_ACTION":"Invalid credit log action",
    "INVALID_DATE_UNIT":"Invalid date unit %s",
    "INVALID_DATE_TYPE":"Invalid date type %s",
    "INVALID_DATE":"Invalid date format %s",
    "ACCESS_DENIED":"Access Denied",
    "INVALID_INT_VALUE":"%s must be an integer",
    "INVALID_BOOL_VALUE":"invalid boolean value %s",
    "INVALID_FLOAT_VALUE":"%s must be a valid floating point",
    "INVALID_STRING_VALUE":"%s must be an string",
    "INVALID_LIST_VALUE":"%s must be a list",
    "INVALID_IP_ADDRESS":"Invalid IP Address %s",
    "INVALID_REL_DATE_UNIT":"Invalid Relative Date Unit %s",
    "INVALID_REL_DATE":"Invalid Relative Date %s",
    "INVALID_TIME_STRING":"Invalid Time String %s",
    "TIME_OUT_OF_RANGE":"Time Out of Range",
    "INVALID_DAY_OF_WEEK":"'%s' is not a valid day of week",
    "INCOMPLETE_REQUEST":"Incomplete request, argument %s not found",
    "FROM_VALUE_INVALID":"Invalid From value %s",
    "TO_VALUE_INVALID":"Invalid To value %s",
    "ATTR_NOT_FOUND":"Attribute %s not found",
    "INVALID_ORDER_BY":"Invalid Order By value %s",
    "INVALID_MAC_ADDRESS":"Mac Address %s is invalid"
    
}

USER_ACTIONS_ERRORS={
    "INVALID_MULTI_LOGIN":"Invalid Multi Login Value",
    "CREDIT_NOT_FLOAT":"Credit must be a float number",
    "CREDIT_MUST_BE_POSITIVE":"Credit must be positive number",
    "INVALID_CREDIT_ACTION":"Invalid credit change action %s",
    "BAD_NORMAL_USERNAME":"Bad characters in username",
    "BAD_PASSWORD":"Bad characters in password",
    "BAD_EMAIL":"Invalid email address %s",
    "INVALID_REL_EXP_DATE":"Relative Expiration Date is Invalid",
    "INVALID_USER_COUNT":"Invalid count of users %s",
    "COUNT_NOT_INTEGER":"User count should be positive integer",
    "NORMAL_COUNT_NOT_MATCH":"Normal Usernames count isn't equal to updating users count. Updating %s number of users while there are %s normal usernames",
    "INVALID_PASSWORD_LENGTH":"Invalid password length %s",
    "ACCESS_TO_SAVED_USER_LIST_DENIED":"You don't have access to saved username/password list",
    "NORMAL_USERNAME_EXISTS":"Normal username %s already exists",
    "INVALID_OPERATOR":"Invalid operator %s",
    "DELETE_USER_IS_ONLINE":"Can't delete user with id %s, because he is online",
    "INVALID_ABS_EXP_DATE":"Absolute Expiration Date is Invalid: %s",
    "INVALID_RADIUS_ATTRIBUTE":"Radius Attributes %s is not in radius dictionary",
    "PERSISTENT_LAN_MAC_EXISTS":"Persistent Lan %s already exists",
    "PLAN_MAC_COUNT_NOT_MATCH":"Number of Mac Addresses count isn't equal to updating users count. Updating %s number of users while there are %s macs",
    "RAS_IS_NOT_PERSISTENT_LAN":"Ras %s is not Persistent Lan",
    "CAN_NOT_NEGATE_CREDIT":"Can not negate credit of user %s, current credit is %s"
}

USER_ERRORS={
    "DUPLICATE_ATTR_REGISTRATION":"Duplicate registration of attribute %s",
    "UNREGISTERED_ATTRIBUTE":"Attribute %s not registered",
    "UNKNOWN_ATTRIBUTE_ACTION":"Unknown attribute action %s",
    "USERID_DOESNT_EXISTS":"User with user id %s does not exists",
    "NORMAL_USERNAME_DOESNT_EXISTS":"User with normal username %s does not exists",
    "ACCESS_TO_USER_DENIED":"You have not access to user id %s",
    "CANT_FIND_INSTANCE":"User %s is not online on %s %s",
    "USER_IN_BLACKLIST":"User ID %s is in load black list"
}

USER_LOGIN_ERRORS={
    "USER_LOCKED":"User is locked",
    "NO_CHARGE_DEFINED":"User doesn't have charge for type %s",
    "NO_APPLICABLE_RULE":"No rule can be applied",
    "ABS_EXP_DATE_REACHED":"absolute expiration date has reached",
    "CREDIT_FINISHED":"Credit has finished",
    "REL_EXP_DATE_REACHED":"Relative expiration date has reached",
    "WRONG_PASSWORD":"Wrong password",
    "MAX_CONCURRENT":"Maximum number of concurrent logins reached",
    "USER_IP_NOT_AVAILABLE":"Client IP Address not available for user %s",
    "MAX_CHECK_ONLINE_FAILS_REACHED":"Maximim check online fails reached",
    "DAY_TIME_USAGE":"Day usage time limit exceeded",
    "DAY_TRANSFER_USAGE":"Day usage transfer limit exceeded"

}

ADMIN_LOGIN_ERRORS={
    "NO_SUCH_ADMIN":"No such admin %s",
    "INCORRECT_PASSWORD":"Incorrect password",
    "ADMIN_LOCKED":"admin account is locked",
    "ADDRESS_BANNED":"You are not authorized to login from this address"    
}

ADMIN_ERRORS={
    "ADMIN_ID_INVALID":"Admin ID %s is invalid",
    "ADMIN_USERNAME_INVALID":"Admin Username %s is invalid",
    "ADMIN_USERNAME_TAKEN":"Admin Username %s is already taken",
    "BAD_USERNAME":"Admin Username %s contains illegal characters",
    "BAD_PASSWORD":"Admin Password contains illegal characters",
    "NEGATIVE_DEPOSIT_NOT_ALLOWD":"You don't have enough deposit, you need %s more deposit"#needed deposit
}

PERM_ERRORS={
    "INVALID_PERMISSION_VALUE":"Invalid permission value: %s", #more decriptive message as argument
    "DONT_HAVE_PERMISSION":"Admin don't have permission",
    "DUPLICATE_PERM_NAME":"Duplicate permission registration %s",
    "NO_SUCH_PERMISSION":"No Such Permission %s",
    "DEPENDENCY_NOT_SATISFIED":"Dependency Permission %s not satisfied for %s",#1- dependency perm 2- perm
    "ALREADY_HAS_PERMISSION":"Admin already has permission %s",
    "DEPENDENT_PERMISSION":"Permission %s is needed by %s",
    "NO_VALUE_TO_DELETE":"Permission hasn't any value to delete",
    "PERMISSION_NOT_HAVE_THIS_VALUE":"Permission doesn't have value %s",
    "DUPLICATE_TEMPLATE_NAME":"Duplicate Permission Template name %s",
    "INVALID_PERM_TEMPLATE_NAME":"Invalid Permission Template name %s",
    "PERMISSION_ALREADY_HAS_VALUE":"Permission %s already has value %s"
}

DEFS_ERRORS={
    "INVALID_DEFINITION_NAME":"Invalid Definition Name %s",
    "UNSUPPORTED_TYPE":"%s has unsupported type %s" #1-def name 2- type
}

GROUP_ERRORS={
    "GROUP_ID_INVALID":"Group id %s is invalid",
    "GROUP_NAME_INVALID":"Group name %s is invalid",
    "GROUP_NAME_TAKEN":"Group name %s already exists",
    "ACCESS_TO_GROUP_DENIED":"You don't have access to group %s",
    "GROUP_CHANGE_DENIED":"You can't change group %s",
    "GROUP_USED_IN_USER":"Group %s used in users '%s' "
}

CHARGE_ERRORS={
    "INVALID_CHARGE_ID":"Invalid Charge ID %s",
    "INVALID_CHARGE_NAME":"Invalid Charge Name %s",
    "CHARGE_NAME_EXISTS":"Charge name %s already exists",
    "RULE_HAS_OVERLAP":"New Rule has overlap with %s",
    "INVALID_RULE_ID_IN_CHARGE":"Invalid charge_rule_id '%s' in %s",
    "INVALID_CHARGE_TYPE":"Invalid charge type %s",
    "ACCESS_TO_CHARGE_DENIED":"You don't have access to charge %s",
    "INVALID_RULE_START_TIME":"Invalid Rule Start Time: %s",#err msg
    "INVALID_RULE_END_TIME":"Invalid Rule End Time: %s",#err msg
    "INVALID_DAY_OF_WEEK":"Charge Rule Day of week error: %s",
    "ASSUMED_KPS_NOT_INTEGER":"Assumed Kps should be an integer",
    "ASSUMED_KPS_NOT_POSITIVE":"Assumed KPS should be positive integer",
    "BANDWIDTH_LIMIT_NOT_INTEGER":"Bandwidth Limit should be an integer",
    "BANDWIDTH_LIMIT_NOT_POSITIVE":"Bandwidth Limit should be positive integer",
    "CPM_NOT_NUMERIC":"Charge Per Minute should be numeric",
    "CPM_NOT_POSITIVE":"Charge Per Minute should be positive integer",
    "CPK_NOT_NUMERIC":"Charge Per Kilobyte should be numeric",
    "CPK_NOT_POSITIVE":"Charge Per Kilobyte should be positive integer",
    "ANOTHER_CHARGE_TYPE_REQUIRED":"Charge Type of %s is required",
    "NO_PORT_SELECTED":"No Port is selected",
    "RULE_END_LESS_THAN_START":"Rule End time is less than or equal to Start time",
    "INVALID_CHARGE_RULE_ID":"Invalid Charge Rule ID %s",
    "CHARGE_RULE_NOT_IN_CHARGE":"Charge Rule with ID %s is not in charge %s",
    "CHARGE_USED_IN_USER":"Charge %s is used in user(s) with id(s) '%s' ",
    "CHARGE_USED_IN_GROUP":"Charge %s is used in group(s) with id(s) '%s' ",
    "BW_LEAF_NAMES_SHOULD_BOTH_SET":"Bandwidth leafs should both be disabled or both be enabled"

}

RAS_ERRORS={
    "DUPLICATE_TYPE_REGISTRATION":"Duplicate Registration of ras type %s",
    "RAS_TYPE_NOT_REGISTERED":"Ras type %s is not registered",
    "INVALID_RAS_IP":"Invalid Ras IP %s",
    "INVALID_RAS_ID":"Invalid Ras ID %s",
    "RAS_IP_ALREADY_EXISTS":"Ras IP %s Already Exists",
    "RAS_USED_IN_RULE":"Ras used in charge rule %s, delete the charge rule first",
    "INVALID_PORT_NAME":"Invalid Port Name %s",
    "RAS_ALREADY_HAS_PORT":"Ras already has port with name %s",
    "INVALID_PORT_TYPE":"Invalid Port Type %s",
    "RAS_DONT_HAVE_PORT":"Ras doesn't have port %s",
    "RAS_DONT_HAVE_ATTR":"Ras doesn't have attribute %s",
    "NO_SUCH_INACTIVE_RAS":"There's no Inactive ras with ip %s",
    "RAS_IS_INACTIVE":"Ras with ip %s is inactive, you should reactive it instead of adding",
    "RAS_ALREADY_HAVE_IPPOOL":"Ras already have ippool %s",
    "RAS_DONT_HAVE_IPPOOL":"Ras doesn't have IPpool %s"
}

IPPOOL_ERRORS={
    "NO_FREE_IP":"All %s IP Pool IPs are used",
    "IP_NOT_IN_USED_POOL":"IP %s is not in 'used list' of IP Pool %s",
    "INVALID_IP_POOL_ID":"Invalid IP Pool id %s",
    "INVALID_IP_POOL_NAME":"Invalid IP Pool name %s",
    "BAD_IP_POOL_NAME":"Bad IP Pool name %s. IP Pool name should only contain alphanumeric and _(underline)",
    "IP_POOL_NAME_ALREADY_EXISTS":"IP Pool name %s already exists",
    "IP_ALREADY_IN_POOL":"IP %s already exists in IP Pool",
    "IP_NOT_IN_POOL":"IP %s does not exist in IP Pool",
    "IPPOOL_USED_IN_RAS":"IP Pool Used In ras %s, delete it from ras first"
}

BANDWIDTH_ERRORS={
    "NO_FREE_ID":"No ID is available from pool %s",
    "INVALID_INTERFACE_ID":"Interface ID %s is invalid",
    "INVALID_INTERFACE_NAME":"Interface Name %s is invalid",
    "INVALID_NODE_ID":"Node ID %s is invalid",
    "INVALID_LEAF_ID":"Leaf ID %s is invalid",
    "INVALID_LEAF_NAME":"Leaf Name %s is invalid",
    "LEAF_ID_NOT_FOUND":"Leaf with id %s not found",
    "NODE_ID_NOT_FOUND":"Node with id %s not found",
    "INTERFACE_NAME_ALREADY_EXISTS":"Interface %s already defined",
    "INVALID_INTERFACE_NAME":"Invalid Interface name %s",
    "INTERFACE_HAS_ROOT_NODE":"Interface %s already has root node",
    "INVALID_LIMIT_KBITS":"Limits Kbit/s '%s' should be greater than zero integer",
    "INVALID_LEAF_NAME":"Invalid Leaf name %s",
    "INVALID_TOTAL_LIMIT_KBITS":"Total Limit Kbit/s '%s' should be an integer, both should be positive, or both should be negative(disabled)",
    "LEAF_NAME_ALREADY_EXISTS":"Leaf name %s already defined",
    "INVALID_PROTOCOL":"Invalid Protocol %s",
    "LEAF_HAS_THIS_FILTER":"Leaf %s already has filter %s %s",
    "INVALID_FILTER":"Invalid Filter %s",
    "LEAF_DOESNT_HAVE_SERVICE":"Leaf %s doesn't have service with id %s",
    "NODE_HAS_CHILDREN":"Node has children, delete them first",
    "LEAF_USED_IN_CHARGE":"Leaf used in charge %s",
    "CANT_DELETE_ROOT_NODE":"You can't delete root node, delete interface instead",
    "LEAF_HAS_SERVICES":"Leaf has services, delete them first",
    "INVALID_STATIC_IP_ID":"BW StaticIP ID %s is invalid",
    "INVALID_STATIC_IP":"BW StaticIP %s is invalid",
    "STATIC_IP_EXISTS":"BW StaticIP %s is already exists in %s",

}


PLUGIN_ERRORS={
    "INVALID_HOOK":"Invalid Hook name %s"
}

def errorText(event,error,add_error_key=True):
    """
	return "error" text representation in "event"
	event is a text that shows which dictionary we use for errors
	ex. it can be "NORMAL_USER_LOGIN", ...
	error is name of error that we want text for
	
	NOTE: there may be %s is retuened strings in such cases you must use % operator 
	       after the returned string and overrid %s values
    """
    try:
	error_map={"USER_ACTIONS":USER_ACTIONS_ERRORS,
		   "USER":USER_ERRORS,
		   "USER_LOGIN":USER_LOGIN_ERRORS,
		   "GENERAL":GENERAL_ERRORS,
		   "PLUGINS":PLUGIN_ERRORS,
		   "ADMIN_LOGIN":ADMIN_LOGIN_ERRORS,
		   "ADMIN":ADMIN_ERRORS,
		   "PERMISSION":PERM_ERRORS,
		   "DEFS":DEFS_ERRORS,
		   "GROUPS":GROUP_ERRORS,
		   "CHARGES":CHARGE_ERRORS,
		   "RAS":RAS_ERRORS,
		   "IPPOOL":IPPOOL_ERRORS,
		   "BANDWIDTH":BANDWIDTH_ERRORS
		  }
		   
	err_str=error_map[event][error]

	if add_error_key:
	    err_str="%s|%s"%(error,err_str)
	return err_str

    except:
	logException(LOG_ERROR,"errorText: can't find error for %s,%s"%(event,error))
	raise GeneralException(GENERAL_ERRORS["NO_ERROR_TEXT"])

