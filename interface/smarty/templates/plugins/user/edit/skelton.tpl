{*

*}
{include file="admin_header.tpl" title="Edit User Attributes" selected="User Information"}
{include file="err_head.tpl"}

User ID: {$user_id}
<form method=POST action="/IBSng/admin/plugins/edit.php">

    <input type=hidden name="target" value="user">
    <input type=hidden name="target_id" value="{$user_id}">
    <input type=hidden name="update" value="1">
    <input type=hidden name="edit_tpl_cs" value="{$edit_tpl_cs}">

{foreach from=$edit_tpl_files item="tpl_file"}
    {include file=$tpl_file}    
{/foreach}
<input type=submit value=update>
</form>
{addRelatedLink}
    <a href="/IBSng/admin/user/user_info.php?user_id_multi={$user_id|escape:"url"}" class="RightSide_links">
	User Info
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group List
    </a>
{/addRelatedLink}

{setAboutPage title="Group Info"}
    You can edit attributes of users that you have selected.
{/setAboutPage}

{include file="admin_footer.tpl"}