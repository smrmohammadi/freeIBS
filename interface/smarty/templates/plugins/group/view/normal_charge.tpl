{viewTable title="Normal Charge"}
    {addEditTD type="left"}
	{strip}
	    {if $can_change}{editCheckBox edit_tpl_name="normal_charge"}{/if}
	    Normal Charge
	{/strip}
    {/addEditTD}
    {addEditTD type="right"}
		{ifHasAttr object="group" var_name="normal_charge"}
		    {$group_attrs.normal_charge}  
		{/ifHasAttr} 
		{helpicon subject="normal charge" category="user"}
    {/addEditTD}

{/viewTable}
