{userInfoTable title="IPpool" nofoot="TRUE"}
    {userInfoTD type="user_left"}
        {if $can_change}{editCheckBox edit_tpl_name="ippool"}{/if}
        IPpool
    {/userInfoTD}
    {userInfoTD type="user_right"}
	{ifHasAttr object="user" var_name="ippool"}
	    {$user_attrs.ippool}  
	{/ifHasAttr} 
    {/userInfoTD}
    {userInfoTD type="group"}
	{ifHasAttr object="group" var_name="ippool"}
	    {$group_attrs.ippool}  
	{/ifHasAttr} 
	{helpicon subject="ippool" category="user"}
    {/userInfoTD}

{/userInfoTable}
