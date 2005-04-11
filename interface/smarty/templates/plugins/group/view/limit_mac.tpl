{viewTable title="Limit Mac Address" nofoot="TRUE"}
    {addEditTD type="left" comment=TRUE}
	{strip}
	    {if $can_change}{editCheckBox edit_tpl_name="limit_mac"}{/if}
	    Limit Mac Address
	{/strip}
    {/addEditTD}
    {addEditTD type="right" comment=TRUE}
	{ifHasAttr object="group" var_name="limit_mac"}
	    {$group_attrs.limit_mac|replace:",":"<br>"}
	{/ifHasAttr} 
	{helpicon subject="limit mac address" category="user"}
    {/addEditTD}

{/viewTable}
