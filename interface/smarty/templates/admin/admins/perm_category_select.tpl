{* Show Permissions of one category
    
*}
{config_load file=perm_category_names.conf}
{include file="admin_header.tpl" title="Add Permission to admin"}
{include file="err_head.tpl"}

Adding permission to "{$admin_username}"<br>
<center>
    <h2> 
	
	Please Select Permission category
    </h2>

    <table>
	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=ADMIN&admin_username={$admin_username}">{#ADMIN#}</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=USER&admin_username={$admin_username}">{#USER#}</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=CHARGE&admin_username={$admin_username}">{#CHARGE#}</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=GROUP&admin_username={$admin_username}">{#GROUP#}</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=RAS&admin_username={$admin_username}">{#RAS#}</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=MISC&admin_username={$admin_username}">{#MISC#}</a>


    </table>
</center>
</form>
{if $can_change eq TRUE}
{addRelatedLink}
    <a href="/IBSng/admin/admins/show_perm_categories.php?admin_username={$admin_username}" class="RightSide_links">
	Add New Permission to <b>{$admin_username|capitalize}</b>
    </a>
{/addRelatedLink}
{/if}
{addRelatedLink}
    <a href="/IBSng/admin/admins/admin_perms_list.php?admin_username={$admin_username}" class="RightSide_links">
	<b>{$admin_username|capitalize}</b> Permissions
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/admins/admin_info.php?admin_username={$admin_username}" class="RightSide_links">
	Admin <b>{$admin_username|capitalize}</b> info
    </a>
{/addRelatedLink}
{addRelatedLink}
    <a href="/IBSng/admin/admins/admin_list.php" class="RightSide_links">
	Admin List
    </a>
{/addRelatedLink}
{addRelatedLink}
    <a href="/IBSng/admin/admins/add_new_admin.php" class="RightSide_links">
	Add New Admin
    </a>
{/addRelatedLink}

{setAboutPage title="Add New Permission"}

{/setAboutPage}

{include file="admin_footer.tpl"}