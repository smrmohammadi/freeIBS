{userInfoTable title="User Expiration Date" nofoot="TRUE"} 
    {userInfoTD type="user_left"}
	{if $can_change}{editCheckBox edit_tpl_name="rel_exp_date"}{/if}Relative Expiration Date:
    {/userInfoTD}

    {userInfoTD type="user_right"}
	{ifHasAttr var_name="rel_exp_date" object="user"}
	    {$user_attrs.rel_exp_date} {$user_attrs.rel_exp_date_unit}
	{/ifHasAttr}
    {/userInfoTD}

    {userInfoTD type="group"}
	{ifHasAttr var_name="rel_exp_date" object="group"}
	    {$group_attrs.rel_exp_date} {$group_attrs.rel_exp_date_unit}
	{/ifHasAttr}
	{helpicon subject="relative expiration date" category="user"}		    
    {/userInfoTD}
    
{/userInfoTable}
