{userInfoTable title="Internet Charge" nofoot="TRUE"}
    {userInfoTD type="user_left"}
	{strip}
	    {canDo perm_name="CHANGE NORMAL USER ATTRIBUTES"}
		{editCheckBox edit_tpl_name="normal_charge"}
	    {/canDo}
	    Normal Charge
	{/strip}
    {/userInfoTD}
    {userInfoTD type="user_right"}
		{ifHasAttr object="user" var_name="normal_charge"}
		    {$user_attrs.normal_charge}  
		{/ifHasAttr} 
    {/userInfoTD}
    {userInfoTD type="group"}
		{ifHasAttr object="group" var_name="normal_charge"}
		    {$group_attrs.normal_charge}  
		{/ifHasAttr} 
		{helpicon subject="normal charge" category="user"}
    {/userInfoTD}

{/userInfoTable}
