{include file="admin_header.tpl" title="Group Multi Login" selected="group list"}
{include file="err_head.tpl"}

{editTemplate target="group" target_id=$group_name update_method="multiLogin" edit_tpl_name="multi_login.tpl"}

  {addEditTable title="Expiration Dates" table_width=300}
    {addEditTD type="left"}
	Has Multi Login
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="has_multi_login" value="t" class=checkbox {if attrDefault($group_attrs,"multi_login","has_multi_login")!=""}checked{/if} onClick='multi_login_select.toggle("multi_login")'>
    {/addEditTD}

    {addEditTD type="left"}
	Multi Login
    {/addEditTD}

    {addEditTD type="right"}
	<input id="multi_login" type=text name="multi_login" value="{attrDefault target="group" default_var="multi_login" default_request="multi_login"}" class=small_text> 
    {/addEditTD}

  {/addEditTable}
{/editTemplate}
<script language="javascript" src="/IBSng/js/dom_container.js"> </script>
<script language="javascript">
	multi_login_select=new DomContainer();
	multi_login_select.disable_unselected=true;
	multi_login_select.addByID("multi_login");
{if attrDefault($group_attrs,"multi_login","has_multi_login")!=""}
    multi_login_select.select("multi_login");
{else}
    multi_login_select.select(null);
{/if}
</script>


{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group List
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/group/group_info.php?group_name={$group_name}" class="RightSide_links">
	{$group_name} Group Info
    </a>
{/addRelatedLink}

{setAboutPage title="Multi Login Edit"}
You can set multi login, for users who are member of this group.
Multi login limits maximum instances of user that can be online.
{/setAboutPage}


{include file="admin_footer.tpl"}