{* IPpool Info 
    Show IP pool Informations and show IP's of each pool


*}
{include file="admin_header.tpl" title="IPpool Information"}

{include file="err_head.tpl"}
<center>

{if isset($update_successfull)}
    IP pool Updated Successfully
{/if}

{if isset($ip_added_successfull)}
    IP Added To IP Pool Successfully
{/if}

{if isset($ip_deleted_successfull)}
    IP Deleted from IP Pool Successfully
{/if}

<table border=1>
    <tr>
	<td>
	    IP Pool ID:
	<td>
	    {$ippool_id}
	<td>
	    IP Pool Name:
	<td>
	    {if $is_editing}
		<form method=POST action="ippool_info.php">
		<input type=hidden name=update value=1>
		<input type=hidden name=ippool_id value="{$ippool_id}">
		<input type=hidden name=old_ippool_name value="{$ippool_name}">
		<input type=text name="new_ippool_name" value="{$ippool_name}">
		
	    {else}
	        {$ippool_name}
	    {/if}
    <tr>
	<td>
	    Comment:
	<td colspan=3>
	    {if $is_editing}
		<textarea name="comment">{$comment|strip}</textarea>
	    {else}
	        {$comment}
	    {/if}
</table>
{if !$is_editing}
    <table>
	<tr>
	    <th>
		IP Address
	    <th>
		Status
	{foreach from=$ip_list item=ip}
	    <tr>
		<td>
		    {$ip}
	        <td>
		    {if in_array($ip,$used)}
			Used
		    {else}
			Free
		    {/if}
		<td>
		    {if $can_change}
			<a href="ippool_info.php?del_submit=1&del_ip={$ip|escape:"url"}&ippool_name={$ippool_name|escape:"url"}" {jsconfirm msg="Are you sure you want to delete $ip?"}>
			    del
			</a>
		    {/if}
	{/foreach}
    </table>

    {if $can_change}
    <table align=left>
	<tr>
	    <td>
		<a href="ippool_info.php?edit=1&ippool_name={$ippool_name|escape:"url"}">
		    Edit
		</a>
	<tr>
	    <td>
		<a href="ippool_info.php?delete=1&ippool_name={$ippool_name|escape:"url"}" 
		{jsconfirm msg="Are you sure you want to delete IP Pool? Warning: You should remove ippool from ras and users"}
		>
		    Delete
		</a>
	<tr>
	    <td>
		<form method=POST action="ippool_info.php" name="add_ip_form">
		    Add IP(s) to Pool
	    <td>
		    <input type=text name=add_ip value="{ifisinrequest name="add_ip"}"> {multistr form_name="add_ip_form" input_name="add_ip"}
	    <td>
		    <input type=hidden name=ippool_name value="{$ippool_name}">
		    <input type=submit name=add_submit value=add {jsconfirm}>
	        </form>

	<tr>
	    <td>
		<form method=POST action="ippool_info.php" name="del_ip_form">
		    Del IP(s) from Pool
	    <td>
		    <input type=text name=del_ip value="{ifisinrequest name="del_ip"}"> {multistr form_name="del_ip_form" input_name="del_ip"}
	    <td>
		    <input type=hidden name=ippool_name value="{$ippool_name}">
		    <input type=submit name=del_submit value=del {jsconfirm}>
	        </form>

    </table>
    {/if}
{/if}
{if $is_editing}
    <input type=submit value=change>
    </form>
{/if}

{include file="admin_footer.tpl"}