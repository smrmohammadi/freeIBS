{* Add New User
    count: new group
    credit: 
    owner_name:
    group_name:
    credit_comment
    
    Success: client will be redirected to the new users information page
    Failure: this page is shown again with error message at top of the page

*}

{include file="admin_header.tpl" title="Add New Users" selected="Add User"}
{include file="err_head.tpl"}

<form method=POST>
	{addEditTable title="Add New Users" table_width="320"}
	{addEditTD type="left" err="count_err"}
	    Count
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=count value="{$count}" class=text>
	    {helpicon subject="count" category="user"}
	{/addEditTD}

	{addEditTD type="left" err="credit_err"}
	    Credit
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=credit value="{$credit}" class=text>
	    {helpicon subject="credit" category="user"}
	{/addEditTD}

	{addEditTD type="left" err="credit_comment_err"}
	    Credit Change Comment
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=credit_comment value="{$credit_comment}" class=text>
	    {helpicon subject="credit_comment" category="user"}
	{/addEditTD}

	{addEditTD type="left" err="credit_comment_err"}
	    Owner
	{/addEditTD}

	{addEditTD type="right"}
		{if canDo("CHANGE_USER_OWNER")}
		    {admin_names_select name="owner_name" default="owner_name"}
		{else}
		    {$auth_name}
		    <input type=hidden name="owner_name" value="{$auth_name}" class=text>
		{/if}
		{helpicon subject="owner" category="user"}
	{/addEditTD}
	    
	{addEditTD type="left" err="credit_comment_err"}
	    Group
	{/addEditTD}

	{addEditTD type="right"}
	    {group_names_select name="group_name" default="group_name"}
	    {helpicon subject="group" category="user"}
	
	{/addEditTD}
    {/addEditTable}
</form>
{include file="admin_footer.tpl"}
