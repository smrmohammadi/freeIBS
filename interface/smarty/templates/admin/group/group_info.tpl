{* Group Info


    Group Properties:
	$group_name
	$group_id
	$comment
	$owner_id
	$owner_name
	$attrs





*}
{include file="admin_header.tpl" title="Group Information"}
{include file="err_head.tpl"}

{include file="plugins/group/view/group_info.tpl"}
<br>
{include file="plugins/group/view/exp_date.tpl"}
<br>
{include file="plugins/group/view/multi_login.tpl"}
<br>


{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group List
    </a>
{/addRelatedLink}

{setAboutPage title="Group Info"}
You can see which attributes this group have. You can edit attribute values if you have relevant permission
{/setAboutPage}


{include file="admin_footer.tpl"}
