{* Online Users By Type : Show a list of online users, seperated by their type(eg. Internet or VoIP)
*}

{include file="admin_header.tpl" title="Online Users" selected="Online Users"} 
{include file="err_head.tpl"} 

<form method=get action="{requestToUrl ignore="refresh"}" name="refresh_form">
{addEditTable title="Online Users" action_icon="ok" action_onclick="updateRefresh()"}
    {addEditTD type="left"}
	Refresh Every 
    {/addEditTD}
    {addEditTD type="right"}
	{html_options name="refresh" values=$refresh_times output=$refresh_times selected=$refresh_default}
	Seconds <font size=1>(<span id="timer">&nbsp;</span> seconds remaining)</font>
    {/addEditTD}
{/addEditTable}
</form>

<script language=javascript>
{if isInRequest("refresh")}
    refresh={$smarty.request.refresh};
{else}
    refresh=10;
{/if}
    url_without_refresh='{requestToUrl ignore="refresh"}';
{literal}
    updateTimer();
    function updateTimer()
    {
	refresh-=1;
	span_obj=document.getElementById("timer");
	span_obj.childNodes[0].nodeValue=refresh;
	if(refresh==0)
	    window.location.reload();
	else	    
	    setTimeout("updateTimer()",1000);
    }

    function updateRefresh()
    {
	window.location=url_without_refresh+"&refresh="+document.refresh_form.refresh.value;
	return false;
    }
{/literal}

</script>

{listTable title="Internet Online Users" cols_num=9}
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

	    {listTD extra="onClick='event.cancelBubble=true;'"}
		    
		<a onClick="toggleVisibility('{$info_dic.user_id}'); return false;" href="#">
		    Details
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
