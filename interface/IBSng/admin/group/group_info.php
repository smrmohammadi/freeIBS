<?php
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."attr_parser.php");

needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();
$smarty->assign("is_editing",FALSE);


if(isInRequest("group_name"))
    intGroupInfo($smarty,$_REQUEST["group_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToGroupList($err->getErrorMsg());
}

function intGroupInfo(&$smarty,$group_name)
{
    $charge_info_req=new GetGroupInfo($group_name);
    list($success,$group_info)=$charge_info_req->send();
    if($success)
    {
	$smarty->assign_array($group_info);
	$smarty->assign_array(callAttrParsers($smarty,$group_info["attrs"]));
	$smarty->assign("target","group");
	$smarty->assign("target_id",$group_info["group_name"]);
    }
    else
	$smarty->set_page_error($group_info->getErrorMsgs());
    interface($smarty);
}

function interface(&$smarty)
{
    $smarty->display("admin/group/group_info.tpl");
}
