{* Admin List
    
*}
{include file="admin_header.tpl" title="Admin List"}
{include file="err_head.tpl"}
{listTable title="Admin List" cols_num=4}
	{listTableHeaderIcon action="view" close_tr=TRUE}
	{listTR type="header"}
	    <td>
		ID
	    </td>
	    <td>
		Username
	    </td>
	    <td>
		Name
	    </td>
	    <td>
		Deposit
	    </td>
	{/listTR}

		
	{section name=index loop=$admin_infos}
	    {listTR type="body"}
		<td>
		    {$admin_infos[index].admin_id}
		</td>
		<td>
		    {$admin_infos[index].username}
		</td>
		<td>
		    {$admin_infos[index].name}
		</td>
		<td>
		    {$admin_infos[index].deposit}
		</td>
		<td>
		    <a href="/IBSng/admin/admins/admin_info.php?admin_username={$admin_infos[index].username|escape:"url"}">
			{listTableBodyIcon action="view"}
		    </a>
		</td>
	    {/listTR}
	{/section}
{/listTable}

{include file="admin_footer.tpl"}