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
    intSetGroupInfo($smarty,$group_name);    
    $smarty->assign("can_change",canDo("CHANGE_GROUP",null,$group_name));
    interface($smarty);
}

function interface(&$smarty)
{
    $smarty->display("admin/group/group_info.tpl");
}

?>