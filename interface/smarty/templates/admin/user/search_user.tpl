{* Search User

*}

{include file="admin_header.tpl" title="User Search" selected="User Information"} 
{include file="err_head.tpl"} 
<form method=POST "/IBSng/admin/user/search_user.php" name="search_user">

    {include file="plugins/search/user_id.tpl"} 
	<p>
    {include file="plugins/search/group.tpl"} 
	<p>
    {include file="plugins/search/charge.tpl"}
	<p>
    {include file="plugins/search/owner.tpl"}
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
    <input type=submit value=search>
</form> 

{if $show_results}
<p>
Total Results: <b> {$result_count} </b>
{reportPages total_results=$result_count}
{/if}

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
