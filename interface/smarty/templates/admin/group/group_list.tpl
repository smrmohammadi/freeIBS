{* Group List
   $group_infos: array of associative arrays containing group infos
*}

{include file="admin_header.tpl" title="Group List"}
{include file="err_head.tpl"}

<center>
<table>
    <tr>
	<th>
	    Group ID
	<th>
	    Group Name
	<th>
	    Owner
	    	
    
    {foreach from=$group_infos item=group_info}
	<tr>
	    <td>
		{$group_info.group_id}
	    <td>
		{$group_info.group_name}
    	    <td>
		{$group_info.owner_name}
	    <td>
		<a href="/IBSng/admin/group/group_info.php?group_name={$group_info.group_name|escape:"url"}">info</a>
	
    {/foreach}
</table>
</center>
{include file="admin_footer.tpl"}
