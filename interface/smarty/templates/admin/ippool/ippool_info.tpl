{* IPpool Info 
    Show IP pool Informations and show IP's of each pool


*}
{include file="admin_header.tpl" title="IPpool Information"}

<table border=0 width=100%>
<tr><td width=50% align=center valign=top>
{include file="err_head.tpl"}
        {if $is_editing}
		<form method=POST action="ippool_info.php">
		<input type=hidden name=update value=1>
		<input type=hidden name=ippool_id value="{$ippool_id}">
		<input type=hidden name=old_ippool_name value="{$ippool_name}">
	{/if}
	    {viewTable title="IPPool Information" table_width="220"}
	    {addEditTD type="left" err="IPPool_ID_err"}
		    IP Pool ID
	    {/addEditTD}
	    {addEditTD type="right"}
		{$ippool_id}
	    {/addEditTD}
	    {addEditTD type="left" err="IPPool_ID_err"}
	        IP Pool Name
	    {/addEditTD}
	    {addEditTD type="right"}
		{if $is_editing}
		    <input type=text name="new_ippool_name" value="{$ippool_name}">
    		{else}
		    {$ippool_name}
		{/if}	
	    {/addEditTD}
	    {addEditTD type="left" err="name_err" comment=TRUE}
	        Comment
		{/addEditTD}

	{addEditTD type="right" comment=TRUE}
	    {if $is_editing}
		<textarea name="comment">{$comment|strip}</textarea>
	    {else}
	        {$comment}
	    {/if}
	{/addEditTD}
	{/viewTable}
<br>
    {if $can_change and !$is_editing}
    	<form method=POST action="ippool_info.php" name="add_ip_form">
	    {addEditTable title="Add IP(s) To Pool" table_width="220"}
		{addEditTD type="left" err="add_ip_err"}
		    IP(s)
	    {/addEditTD}
	    {addEditTD type="right"}
		<nobr><input type=text name=add_ip value="{ifisinrequest name="add_ip"}" class=text>{multistr form_name="add_ip_form" input_name="add_ip"}    
	    {/addEditTD}
	    {/addEditTable}
	<input type=hidden name=ippool_name value="{$ippool_name}">
	<input type=hidden name=add_submit>
	</form>

	<form method=POST action="ippool_info.php" name="del_ip_form">
	    {addEditTable title="Del IP(s) From Pool" table_width="220"}
		{addEditTD type="left" err="del_ip__err"}
		    IP(s)
	    {/addEditTD}
	    {addEditTD type="right"}
		<nobr><input type=text name=del_ip value="{ifisinrequest name="del_ip"}" class=text>{multistr form_name="del_ip_form" input_name="del_ip"}    
	    {/addEditTD}
	    {/addEditTable}
	<input type=hidden name=ippool_name value="{$ippool_name}">
	<input type=hidden name=del_submit>
	</form>
    {/if}
</td>
<td width=50% align=center valign=top>
<br>
<br>
{if isset($update_successfull)}
    IP pool Updated Successfully
{/if}

{if isset($ip_added_successfull)}
    IP Added To IP Pool Successfully
{/if}

{if isset($ip_deleted_successfull)}
    IP Deleted from IP Pool Successfully
{/if}
{if !$is_editing}
    {listTable title="IP List" cols_num=2}
	{if $can_change}
	    {listTableHeaderIcon action="delete" close_tr=TRUE}
	{/if}    
	    {listTR type="header"}
		{listTD}
			IP Address
	        {/listTD}
	        {listTD}
			Status
	        {/listTD}
	    {/listTR}
	{foreach from=$ip_list item=ip}
	    {listTR type="body"}
		{listTD}    
		    {$ip}
	        {/listTD}
		{listTD}
		    {if in_array($ip,$used)}
			Used
		    {else}
			Free
		    {/if}
		{/listTD}    
		{if $can_change}
			{listTD icon="TRUE"}
		        	<a href="ippool_info.php?del_submit=1&del_ip={$ip|escape:"url"}&ippool_name={$ippool_name|escape:"url"}" {jsconfirm msg="Are you sure you want to delete $ip?"}>
				    {listTableBodyIcon action="delete" cycle_color="TRUE"}
				</a>
			{/listTD}
		{/if}    
	    {/listTR}
	{/foreach}
    {/listTable}
{/if}
{if $is_editing}
    <input type=submit value=change>
    </form>
{/if}

</td></tr></table>
{if $can_change and !$is_editing}	
{addRelatedLink}
    <a href="ippool_info.php?edit=1&ippool_name={$ippool_name|escape:"url"}" class="RightSide_links">
	Edit IPPool ({$ippool_name})
    </a>
{/addRelatedLink}
{addRelatedLink}
        <a href="ippool_info.php?delete=1&ippool_name={$ippool_name|escape:"url"}" 
		{jsconfirm msg="Are you sure you want to delete IP Pool? Warning: You should remove ippool from ras and users"}
		 class="RightSide_links">
	Delete Ippool ({$ippool_name})
    </a>
{/addRelatedLink}
{/if}
{include file="admin_footer.tpl"}