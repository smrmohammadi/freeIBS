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

{include file="admin_footer.tpl"}
