{* Admin Info
    Shows one admin information, on error, client is redirected to admin_list
    so no error will be shown here
*}
{include file="admin_header.tpl" title="Admin Information"}

{include file="err_head.tpl"}
<center>
{if $update_success}
    Admin Info Updates Successfully
{/if}
    <table>
	<tr>	
	    <td>
		Admin Username:
	    <td>
		{$username}
	    <td>
		Admin ID:
	    <td>
		{$admin_id}
	<tr>
	    <td>
		Name:
	    <td>
		{if $is_editing}
		    <form method=POST action="admin_info.php">
		    <input type=hidden name=admin_username value={$username}>
		    <input type=text name=name value="{$name}">
		{else}		
		    {$name}
		{/if}
	    <td>
		Creator:
	    <td>
		{$creator}
	<tr>
	    <td>
		Deposit:
	    <td>
		{$deposit}
	    <td>
	    <td>
	<tr>
	    <td>
		Comment:
	    <td colspan=3>
		{if $is_editing}
		    <textarea name=comment>{$comment}</textarea>
		{else}
		    {$comment}
		{/if}
    </table>
</center>
{if $is_editing}
    <input type=submit name=submit>
    </form>
{/if}
{canDo perm_name="CHANGE USER INFO" username=$username}
	{addRelatedLink}
    		<a class="RightSide_links" href="/IBSng/admin/admins/admin_info.php?edit=1&admin_username={$username}">    
		    Edit
		</a>
	{/addRelatedLink}
{/canDo}
{canDo perm_name="SEE ADMIN PERMISSIONS" username=$username}
	{addRelatedLink}
    		<a class="RightSide_links" href="/IBSng/admin/admins/admin_perms_list.php?admin_username={$username}">    
		    Permissions List
		</a>
	{/addRelatedLink}
{/canDo}

{canDo perm_name="CHANGE ADMIN PASSWORD" username=$username}
	{addRelatedLink}
    		<a class="RightSide_links" href="/IBSng/admin/admins/change_password.php?username={$username}">    
		    Change Password
		</a>
	{/addRelatedLink}
{/canDo}
{include file="admin_footer.tpl"}