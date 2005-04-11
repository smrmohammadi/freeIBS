{viewTable title="VoIP Username and Password" table_width="380" nofoot="TRUE"} 
    {addEditTD type="left"}
	{canDo perm_name="CHANGE VOIP USER ATTRIBUTES"}
	    {editCheckBox edit_tpl_name="voip_username"}
	{/canDo}
	VOIP Username
    {/addEditTD}

    {addEditTD type="right"}
	{ifHasAttr var_name="voip_username" object="user"}
	    {$user_attrs.voip_username}
	{/ifHasAttr}
	{helpicon subject="voip username" category="user"}
    {/addEditTD}

    {addEditTD type="left"}
	Password
    {/addEditTD}

    {addEditTD type="right"}
<!--	<a class="link_in_body" href="change_password.php">
	    Change Password
	</a>--> &lt; Hidden &gt; 
	{helpicon subject="voip password" category="user"}
    {/addEditTD}
{/viewTable}
