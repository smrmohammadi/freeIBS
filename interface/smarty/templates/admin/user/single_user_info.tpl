{* User Info
    User Properties:
	$user_info: dic of user infos containing basic_info and attrs
	$user_attrs: parsed attributes of user
	$group_attrs: parsed attributes of group

*}

{include file="admin_header.tpl" title="User Information" selected="User Information"} 
{include file="err_head.tpl"} 
<form method=POST action="/IBSng/admin/plugins/edit.php">
    <input type=hidden name="user_id" value="{$user_id}">
    <input type=hidden name="edit_user" value="1">


    {include file="plugins/user/view/single_user_info.tpl"}
    <br>
    {include file="plugins/user/view/normal_username.tpl"}
    <br>
    {include file="plugins/user/view/exp_date.tpl"}
    <br>
    {include file="plugins/user/view/multi_login.tpl"}
    <br>
    {include file="plugins/user/view/normal_charge.tpl"}
    <br>

{attrTableFoot action_icon="edit"}
{/attrTableFoot}
</form> 



{addRelatedLink}
    <a href="/IBSng/admin/user/user_list.php" class="RightSide_links">
	User List
    </a>
{/addRelatedLink}

{setAboutPage title="User Info"}
User Informations and Attributes are shown here. If user doesn't have any attribute, it's value is empty.
{/setAboutPage}


{include file="admin_footer.tpl"}
