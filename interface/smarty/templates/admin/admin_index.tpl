{include file="admin_header.tpl" title="Home" selected=""}

<table border=0 width="100%" height="100%" cellspacing=0 cellpadding=0>
    <tr>
	<td colspan=2 height=30>
	</td>
    </tr>	
    <tr>
	<td valign="top" align="center"> 
		{viewTable title="User" table_width="200" nofoot="TRUE" color="red" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/user/user_info.php" class="page_menu">User Informaion</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/user/user_list.php" class="page_menu">User List</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/user/add_new_user.php" class="page_menu">Add New User</a>
		    {/menuTR}
		{/viewTable}
	</td>
	<td valign="top" align="center">
		{viewTable title="Group" table_width="200" nofoot="TRUE" color="green" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/group/group_list.php" class="page_menu">Group List</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/group/add_new_group.php" class="page_menu">Add New Group</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		{/viewTable}
	</td>
    </tr>
    <tr>
	<td valign="top" align="center">
		{viewTable title="Report" table_width="200" nofoot="TRUE" color="blue" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		{/viewTable}
	</td>
	<td valign="top" align="center">
		{viewTable title="Graph" table_width="200" nofoot="TRUE" color="brown" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}

		{/viewTable}
	</td>
    </tr>
    <tr>
	<td valign="top" align="center">
		{viewTable title="Admin" table_width="200" nofoot="TRUE" color="violet" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/admins/admin_list.php" class="page_menu">Admin List</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/admins/add_new_admin.php" class="page_menu">Add New Admin</a>
		    {/menuTR}
		{/viewTable}
	</td>
	<td valign="top" align="center">
		{viewTable title="Setting" table_width="200" nofoot="TRUE" color="aqua" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/charge/charge_list.php" class="page_menu">Charge</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/ras/ras_list.php" class="page_menu">RAS</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/ippool/ippool_list.php" class="page_menu">IPpool</a>
		    {/menuTR}
		{/viewTable}
	</td>
    </tr>
</table>


{addRelatedLink}
    <a href="/IBSng/admin/user/user_info.php" class="RightSide_links">
	User
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/report/" class="RightSide_links">
	Report
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/admins/admin_list.php" class="RightSide_links">
	Admin
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/setting/" class="RightSide_links">
	Setting
    </a>
{/addRelatedLink}


{setAboutPage title="Home"}

{/setAboutPage}

{include file="admin_footer.tpl"}

