<?php
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."attr_parser.php");

needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();

if(isInRequest("group_name","delete_group"))
    intDelGroup($smarty,$_REQUEST["group_name"]);
else if(isInRequest("group_name"))
    intGroupInfo($smarty,$_REQUEST["group_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToGroupList($err->getErrorMsg());
}

function intDelGroup(&$smarty,$group_name)
{
    $req=new DelGroup($group_name);
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
	redirectToGroupList("Group Deleted Successfully");
    else
    {
	$resp->setErrorInSmarty($smarty);
	intGroupInfo($smarty,$group_name);
    }
}

function intGroupInfo(&$smarty,$group_name)
{
    intSetGroupInfo($smarty,$group_name);    
    $smarty->assign("can_change",canDo("CHANGE_GROUP",null,$group_name));
    $smarty->assign("can_del",canDo("ADD_NEW_GROUP"));
    interface($smarty);
}

function interface(&$smarty)
{
    $smarty->display("admin/group/group_info.tpl");
}

?>