{viewTable title="Internet Username and Password" table_width="380" nofoot="TRUE"} 
    {addEditTD type="left"}
	{canDo perm_name="CHANGE NORMAL USER ATTRIBUTES"}
	    {editCheckBox edit_tpl_name="normal_username"}
	{/canDo}
	Internet Username
    {/addEditTD}

    {addEditTD type="right"}
	{ifHasAttr var_name="normal_username" object="user"}
	    {$user_attrs.normal_username}
	{/ifHasAttr}
	{helpicon subject="normal username" category="user"}
    {/addEditTD}

    {addEditTD type="left"}
	Password
    {/addEditTD}

    {addEditTD type="right"}
	<a class="link_in_body" href="change_password.php">
	    Change Password
	</a>
	{helpicon subject="normal password" category="user"}
    {/addEditTD}
{/viewTable}
