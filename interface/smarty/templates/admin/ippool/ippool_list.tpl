{* IP pools  List
   $ippool_infos: array of associative arrays containing ippool infos

*}

{include file="admin_header.tpl" title="IP Pools List"}
{include file="err_head.tpl"}

<center>
    <table>
	<tr>	
	    <th bgcolor=gray colspan=7>
		<h2>IPPools</2> 
	<tr>
	    <th>
		ID
	    <th>
		IP Pool Name
	    <th>
		Comment
	    <th>
		IPs(Truncated)
		
	{foreach from=$ippool_infos item=ippool_info}
	    <tr>
		<td>
		    {$ippool_info.ippool_id}
		<td>
		    {$ippool_info.ippool_name}
		<td>
		    {$ippool_info.comment}
		<td>
		    {$ippool_info.ips_text|truncate:80:"...":false}
		<td>
		    <a href="/IBSng/admin/ippool/ippool_info.php?ippool_name={$ippool_info.ippool_name|escape:"url"}">
			info
		    </a>
	{/foreach}
    </table>
    <a href="add_new_ippool.php"> 
	Add New IP Pool 
    </a>
</center>

{include file="footer.tpl"}