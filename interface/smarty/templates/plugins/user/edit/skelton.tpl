{*

*}
{include file="admin_header.tpl" title="Edit User Attributes" selected="User Information"}
{include file="err_head.tpl"}

{if not $single_user}
{headerMsg}
    Warning: When editing multiple users, user default values and group values are empty and ambigious
{/headerMsg}    
{/if}

{viewTable title="User  Information" table_width="370"}

    {addEditTD type="left"}
	User ID
    {/addEditTD}
    {addEditTD type="right"}
	{$user_id}
    {/addEditTD}

{/viewTable}

<form method=POST action="/IBSng/admin/plugins/edit.php" name="user_edit">

    <input type=hidden name="target" value="user">
    <input type=hidden name="target_id" value="{$user_id}">
    <input type=hidden name="update" value="1">
    <input type=hidden name="edit_tpl_cs" value="{$edit_tpl_cs}">

{foreach from=$edit_tpl_files item="tpl_file"}
    {include file=$tpl_file}    
{/foreach}

{attrTableFoot action_icon="ok"}
{/attrTableFoot}
</form>

{addRelatedLink}
    <a href="/IBSng/admin/user/user_info.php?user_id_multi={$user_id|escape:"url"}" class="RightSide_links">
	User <b>{$user_id}</b> Info
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group List
    </a>
{/addRelatedLink}

{setAboutPage title="User Info"}
    You can edit attributes of users that you have selected.
{/setAboutPage}

{include file="admin_footer.tpl"}