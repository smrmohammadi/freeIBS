{* Search User

*}
{include file="admin_header.tpl" title="User Search" selected="User Information"} 
{include file="err_head.tpl"} 
<script language="javascript" src="/IBSng/js/check_box_container.js"></script>
<form method=POST action="/IBSng/admin/user/search_user.php#show_results" name="search_user">
    {tabTable tabs="Main,Group,Charge,Owner,ExpDates,Lock,Misc" content_height=100 action_icon="search"}

    {tabContent tab_name="Main"}
	{include file="plugins/search/user_id.tpl"} 
	{include file="plugins/search/normal_user.tpl"}
    {/tabContent}
    {tabContent tab_name="Group"}
        {include file="plugins/search/group.tpl"} 
    {/tabContent}
    {tabContent tab_name="Charge"}
	{include file="plugins/search/charge.tpl"}
    {/tabContent}
    {tabContent tab_name="Owner"}
	{include file="plugins/search/owner.tpl"}
    {/tabContent}
    {tabContent tab_name="ExpDates"}
        {include file="plugins/search/abs_exp_date.tpl"}
        {include file="plugins/search/rel_exp_date.tpl"}
    {/tabContent}

    {tabContent tab_name="Lock"}
        {include file="plugins/search/lock.tpl"}
    {/tabContent}

    {tabContent tab_name="Misc"}
	{include file="plugins/search/credit.tpl"}
	{include file="plugins/search/multi_login.tpl"}
	{include file="plugins/search/ippool.tpl"}
    {/tabContent}
    <tr><td colspan=20>	
        {include file="report_foot.tpl"}
    </td></tr>
    <tr><td colspan=20>	
	{include file="admin/user/search_user_select_attrs.tpl"}     
    </td></tr>
    {/tabTable}
    <input type=hidden name=search value=1>
    <input type=hidden name=page value=1>
{if $show_results}
	<p>
	<a name="show_results"></a>
	{include file="admin/user/user_list.tpl"}
	{reportPages total_results=$result_count }
	{if $can_change}
	    {literal}
	    <script>
		function submitEdit(var_name)
		{
		    document.search_user.action="/IBSng/admin/user/search_user_edit.php?"+var_name+"=1";
		    document.search_user.submit();
		}
		
		function checkAnyUserChecked()
		{
		    if( user_ids.allUnChecked() ) 
		    {
			alert('No user(s) selected');
			return false;
		    }
		    return true;
		}
	    </script>
	    {/literal}
	    <input type=image src="/IBSng/images/icon/edit.gif" name=edit value=edit onClick="javascript:  if(checkAnyUserChecked()) submitEdit('edit'); return false;">
	    <input type=image src="/IBSng/images/icon/change_credit.gif" name=changecredit value="Change Credit" onClick="javascript: if(checkAnyUserChecked()) submitEdit('change_credit'); return false;">
	    <input type=image src="/IBSng/images/icon/view_connection_logs.gif" name=connection_log value="View Connection Logs" onClick="javascript: if(checkAnyUserChecked()) submitEdit('connection_log'); return false;">
	    <input type=image src="/IBSng/images/icon/view_credit_changes.gif" name=credit_log value="View Credit Changes" onClick="javascript: if(checkAnyUserChecked()) submitEdit('credit_change'); return false;">
	    <input type=image src="/IBSng/images/icon/delete.gif" name=delete value="Delete" onClick="javascript: if(checkAnyUserChecked()) submitEdit('delete_users'); return false;">

	{/if}
    
{/if}
</form> 


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

{setAboutPage title="Search User"}
You can search through user attributes
{/setAboutPage}

{include file="admin_footer.tpl"}
