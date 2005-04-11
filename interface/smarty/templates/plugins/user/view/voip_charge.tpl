{userInfoTable title="VoIP Charge" nofoot="TRUE"}
    {userInfoTD type="user_left"}
	{strip}
	    {canDo perm_name="CHANGE VOIP USER ATTRIBUTES"}
		{editCheckBox edit_tpl_name="voip_charge"}
	    {/canDo}
	    VoIP Charge
	{/strip}
    {/userInfoTD}
    {userInfoTD type="user_right"}
		{ifHasAttr object="user" var_name="voip_charge"}
		    {$user_attrs.voip_charge}  
		{/ifHasAttr} 
    {/userInfoTD}
    {userInfoTD type="group"}
		{ifHasAttr object="group" var_name="voip_charge"}
		    {$group_attrs.voip_charge}  
		{/ifHasAttr} 
		{helpicon subject="voip charge" category="user"}
    {/userInfoTD}

{/userInfoTable}
