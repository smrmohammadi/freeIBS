{* Online Users By Type : Show a list of online users, seperated by their type(eg. Internet or VoIP)
*}

{include file="admin_header.tpl" title="Online Users" selected="Online Users"} 
{include file="err_head.tpl"} 
<iframe name=msg id=msg border=0 FRAMEBORDER=0 SCROLLING=NO height=50 valign=top></iframe>
{literal}
    <script language=javascript>
	function killUser(user_id,username,ras_ip,unique_id_val)
	{
	    document.getElementById("msg").src="/IBSng/admin/user/kill_user.php?user_id="+user_id+"&username="+username+"&ras_ip="+ras_ip+"&unique_id_val="+unique_id_val;
	}
    </script>
{/literal}

{include file="refresh_header.tpl" title="Online Users"}

{listTable title="Internet Online Users" cols_num=9}
    {listTableHeaderIcon action="kick"}
    {listTableHeaderIcon action="details" close_tr=TRUE}
    {listTR type="header"}
	{listTD}
	    {sortableHeader name="user_id"} 
		User ID
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="normal_username"} 
		Username
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="login_time_epoch" default=TRUE default_desc=TRUE}
		Login Time
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="current_credit"} 
		Credit
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="ras_ip"} 
		Ras IP
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="unique_id_val"} 
	        Port/ID
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="in_bytes"} 
		In Bytes
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="out_bytes"} 
		Out Bytes
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="owner_name"} 
		Owner
	    {/sortableHeader}
	{/listTD}
    {/listTR}
    {foreach from=$onlines item=info_dic}
	{listTR type="body" hover_location="/IBSng/admin/user/user_info.php?user_id=`$info_dic.user_id`"}
	    {listTD}
		<a href="/IBSng/admin/user/user_info.php?user_id={$info_dic.user_id}">
		    {$info_dic.user_id}
		</a>
	    {/listTD}

	    {listTD}
		{$info_dic.normal_username}
	    {/listTD}

	    {listTD}
		{$info_dic.login_time}
	    {/listTD}

	    {listTD}
		{$info_dic.current_credit|price}
	    {/listTD}


	    {listTD}
		{$info_dic.ras_ip}
	    {/listTD}

	    {listTD}
		{$info_dic.unique_id_val}
	    {/listTD}

	    {listTD}
		{$info_dic.in_bytes}
	    {/listTD}

	    {listTD}
		{$info_dic.out_bytes}
	    {/listTD}

	    {listTD}
		{$info_dic.owner_name}
	    {/listTD}

	    {listTD icon=TRUE extra="onClick='event.cancelBubble=true;'"}
		    <a style="text-decoration:none" href="javascript: killUser('{$info_dic.user_id}','{$info_dic.normal_username}','{$info_dic.ras_ip}','{$info_dic.unique_id_val}');" {jsconfirm}>
			{listTableBodyIcon action="kick" cycle_color="TRUE"}
		    </a>
	    {/listTD}

	    {listTD icon=TRUE extra="onClick='event.cancelBubble=true;'"}
		    
		<a onClick="showReportLayer('{$info_dic.user_id}',this); return false;" href="#">
		    {listTableBodyIcon action="details" cycle_color="TRUE"}
		</a>
		{reportDetailLayer name=`$info_dic.user_id` title="Report Details"}
		    <table>
		    {foreach from=`$info_dic.attrs` key=key item=item}
			<tr>
			    <td>
				{$key}
			    </td>
			    <td>
				{$item}
			    </td>
			</tr>
		    {/foreach}
		    </table>
		{/reportDetailLayer}
	    {/listTD}
	{/listTR}
    {/foreach}

{/listTable}

{addRelatedLink}
    <a href="/IBSng/admin/user/search_user.php" class="RightSide_links">
	Search User
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/user/user_info.php" class="RightSide_links">
	User Information
    </a>
{/addRelatedLink}

{setAboutPage title="Online Users"}
You can see online users, seperated by their service
{/setAboutPage}

{include file="admin_footer.tpl"}
