{include file="admin_header.tpl" title="Add New Admin" selected=""}

<a href="admins/admin_list.php">Admins</a>
<a href="charge/charge_list.php">Charge</a>
<a href="group/group_list.php">Group</a>
<a href="misc">Misc</a>
<a href="ras/ras_list.php">Ras</a>
<a href="user/user_info.php">User</a>
<a href="ippool/ippool_list.php">IPpool</a>


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

