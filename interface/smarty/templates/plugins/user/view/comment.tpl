{viewTable title="Comment" nofoot="TRUE" table_width="380"}
    {addEditTD type="left" comment=TRUE}
	{strip}
	    {if $can_change} {editCheckBox edit_tpl_name="comment"} {/if}
	    Comment
	{/strip}
    {/addEditTD}
    {addEditTD type="right" comment=TRUE}
	{ifHasAttr object="user" var_name="comment"}
	    {$user_attrs.comment|nl2br}
	{/ifHasAttr} 
	{helpicon subject="comment" category="user"}
    {/addEditTD}
{/viewTable}

