{include file="admin_header.tpl" title="User Information"}
{include file="err_head.tpl"}
<form method=POST action="/IBSng/admin/user/user_info.php">
    {addEditTable title="User ID"}
	{addEditTD type="left"}
	    User ID
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=user_id class=text value="{ifisinrequest name="user_id"}">
	{/addEditTD}
		
    {/addEditTable}
</form>

<form method=POST action="/IBSng/admin/user/user_info.php">
    {addEditTable title="Normal Username"}
	{addEditTD type="left"}
	    Normal Username
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=normal_username class=text value="{ifisinrequest name="normal_username"}">
	{/addEditTD}
		
    {/addEditTable}
</form>

{include file="admin_footer.tpl"}