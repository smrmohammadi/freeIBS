{* Group Info


    Group Properties:
	$group_name
	$group_id
	$comment
	$owner_id
	$owner_name
	$attrs





*}
{include file="admin_header.tpl" title="Group Information" selected="Group List"} 
{include file="err_head.tpl"}
<form method=POST action="/IBSng/admin/plugins/edit.php">
    <input type=hidden name="group_name" value="{$group_name}">
    <input type=hidden name="edit_group" value="1">

{include file="plugins/group/view/group_info.tpl"}
{include file="plugins/group/view/exp_date.tpl"}
{include file="plugins/group/view/multi_login.tpl"}
{include file="plugins/group/view/normal_charge.tpl"}


{attrTableFoot action_icon="edit" table_width="280"}
{/attrTableFoot}

</form>

{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group List
    </a>
{/addRelatedLink}

{setAboutPage title="Group Info"}
You can see which attributes this group have. You can edit attribute values if you have relevant permission
{/setAboutPage}


{include file="admin_footer.tpl"}
