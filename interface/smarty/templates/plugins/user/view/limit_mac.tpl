{userInfoTable title="Limit Mac Address" nofoot="TRUE"}
    {userInfoTD type="user_left" comment=TRUE}
        {if $can_change}{editCheckBox edit_tpl_name="limit_mac"}{/if}
        Limit Mac Address
    {/userInfoTD}
    {userInfoTD type="user_right" comment=TRUE}
	{ifHasAttr object="user" var_name="limit_mac"}
	    {$user_attrs.limit_mac|replace:",":"<br>"}
	{/ifHasAttr} 
    {/userInfoTD}
    {userInfoTD type="group" comment=TRUE}
	{ifHasAttr object="group" var_name="limit_mac"}
	    {$group_attrs.limit_mac|replace:",":"<br>"}
	{/ifHasAttr} 
	{helpicon subject="Limit Mac Address" category="user"}
    {/userInfoTD}

{/userInfoTable}
