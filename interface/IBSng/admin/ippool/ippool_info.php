<?php
require_once("../../inc/init.php");
require_once(IBSINC."ippool.php");
require_once(IBSINC."ippool_face.php");
require_once(IBSINC."perm.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();
$smarty->assign("is_editing",FALSE);
if(isInRequest("ippool_name"))
    intIPpoolInfo($smarty,$_REQUEST["ippool_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToIPpoolList($err->getErrorMsg());
}

function intIPpoolInfo(&$smarty,$ippool_name)
{
    $ippool_info_req=new GetIPpoolInfo($ippool_name);
    list($success,$info)=$ippool_info_req->send();
    if(!$success)
//	redirectToIPpoolList($info->getErrorMsg());
	$smarty->set_page_error($info->getErrorMsgs());
    interface($smarty,$info);
}

function interface(&$smarty,$ippool_info)
{
    intAssignValues($smarty,$ippool_info);
    $smarty->display("admin/ippool/ippool_info.tpl");
}

function intAssignValues(&$smarty,$ippool_info)
{
    $smarty->assign_array($ippool_info);
}

?>
