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

{include file="admin_footer.tpl"}