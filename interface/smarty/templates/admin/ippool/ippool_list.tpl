{* IP pools  List
   $ippool_infos: array of associative arrays containing ippool infos

*}

{include file="admin_header.tpl" title="IP Pools List"}
{include file="err_head.tpl"}

{listTable title="IP Pool List" cols_num=4}
	{listTableHeaderIcon action="view" close_tr=TRUE}
	{listTR type="header"}
	    <td>
		ID
	    </td>
	    <td>
		IP Pool Name
	    </td>
	    <td>
		Comment
	    </td>
	    <td>
		IPs(Truncated)
	    </td>
	{/listTR}
		
	{foreach from=$ippool_infos item=ippool_info}
	    {listTR type="body" cycle_color=FALSE}
		<td>
		    {$ippool_info.ippool_id}
		</td>
		<td>
		    {$ippool_info.ippool_name}
		</td>
		<td>
		    {$ippool_info.comment}
		</td>
		<td>
		    {$ippool_info.ips_text|truncate:80:"...":false}
		</td>
		<td>
		    <a href="/IBSng/admin/ippool/ippool_info.php?ippool_name={$ippool_info.ippool_name|escape:"url"}">
			{listTableBodyIcon action="view" cycle_color=TRUE}
		    </a>
		</td>
	    {/listTR}
	{/foreach}

{/listTable}
<a href="add_new_ippool.php"> 
    Add New IP Pool 
</a>

{include file="admin_footer.tpl"}