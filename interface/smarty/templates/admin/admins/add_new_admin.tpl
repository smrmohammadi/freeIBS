{* Admin Add New Admin
    username: new admin username
    password: new admin password
    name: new admin name
    comment: comments about new admin
    
    Success: client will be redirected to the new admin information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Admin"}
{include file="err_head.tpl"}

<form method=POST>
    {addEditTable title="Add New Admin"}
	{addEditTD type="left" err="username_err"}
	    Username
	{/addEditTD}

	{addEditTD type="right"}
	    <input class=text type=text name=username value='{$username}'>
	    {helpicon subject='username' category='admin'}
	{/addEditTD}

	{addEditTD type="left" err="password_err"}
	    Password
	{/addEditTD}

	{addEditTD type="right"}
    	    <input class=text type=password name=password1>
	{/addEditTD}

	{addEditTD type="left" err="password_err"}
	    Confirm Password
	{/addEditTD}

	{addEditTD type="right"}
    	    <input class=text type=password name=password2>
	{/addEditTD}

	{addEditTD type="left" err="name_err"}
	    Name
	{/addEditTD}

	{addEditTD type="right"}
    	    <input class=text type=text name=name value="{$name}">
	{/addEditTD}
	
	{addEditTD type="left" err="name_err" comment=TRUE}
	    Comment
	{/addEditTD}

	{addEditTD type="right" comment=TRUE}
	    <textarea class=text name=comment>{$comment}</textarea>
	{/addEditTD}
	
    {/addEditTable}
</form>


{include file="admin_footer.tpl"}