{* Search User

*}
{include file="admin_header.tpl" title="User Search" selected="User Information"} 
{include file="err_head.tpl"} 
<script language="javascript" src="/IBSng/js/check_box_container.js"></script>
<form method=POST action="/IBSng/admin/user/search_user.php#show_results" name="search_user">

    {include file="plugins/search/user_id.tpl"} 
	<p>
    {include file="plugins/search/group.tpl"} 
	<p>
    {include file="plugins/search/charge.tpl"}
	<p>
    {include file="plugins/search/owner.tpl"}
	<p>
    {include file="plugins/search/credit.tpl"}
	<p>
    {include file="plugins/search/multi_login.tpl"}
	<p>
    {include file="plugins/search/normal_user.tpl"}
	<p>
    {include file="plugins/search/rel_exp_date.tpl"}
	<p>
    {include file="report_foot.tpl"}

    {include file="admin/user/search_user_select_attrs.tpl"}     
    <input type=hidden name=search value=1>
    <input type=hidden name=page value=1>
    <input type=submit value=search>
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
		    document.search_user.action="/IBSng/admin/user/search_user_edit.php";
		    document.search_user.elements["var_name"]=1;
		    document.search_user.submit();
		}
	    </script>
	    {/literal}
	    <input type=submit name=edit value=edit {literal} onClick="javascript: if( user_ids.allUnChecked() ) {alert('No user(s) selected');} else {submitEdit('edit')} return false;  " {/literal}>
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
