{* Admin List
    
*}
{include file="admin_header.tpl" title="Admin List"}
{include file="err_head.tpl"}

<center>
    <table>
	<tr>	
	    <th>
		ID
	    <th>
		Username
	    <th>
		Name
	    <th>
		Deposit
		
	{section name=index loop=$admin_infos}
	    <tr>
		<td>
		    {$admin_infos[index].admin_id}
		<td>
		    {$admin_infos[index].username}
		<td>
		    {$admin_infos[index].name}
		<td>
		    {$admin_infos[index].deposit}
		<td>
		    <a href="/IBSng/admin/admins/admin_info.php?admin_username={$admin_infos[index].username}">
			info
		    </a>
	
	{/section}



    </table>
</center>
</form>

{include file="admin_footer.tpl"}