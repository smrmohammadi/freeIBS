<?php
require_once("../../inc/init.php");
require_once(IBSINC."admin.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."admin_face.php");

needAuthType(ADMIN_AUTH_TYPE);

if (isInRequest("edit","admin_username"))
    intAdminInfo(TRUE);
else if(isInRequest("name","comment","admin_username"))
    intUpdateAdminInfo();
else if(isInRequest("admin_username"))
    intAdminInfo();
else
{
    $err=new error("INVALID_INPUT");
    redirectToAdminList($err->getErrorMsg());
}


function intUpdateAdminInfo()
{
    $update_req=new UpdateAdminInfo($_REQUEST["admin_username"],$_REQUEST["name"],$_REQUEST["comment"]);
    list($success,$err)=$update_req->send();
    if($success)
	intAdminInfo(FALSE,TRUE);
    else
	intAdminInfo(TRUE,FALSE,$err);

}

function interface($info_arr,$is_editing,$update_success,$err)
{
    $smarty=new IBSSmarty();
    intAssignValues($smarty,$info_arr,$is_editing,$update_success,$err);
    $smarty->display("admin/admins/admin_info.tpl");
}

function intAssignValues(&$smarty,$info_arr,$is_editing,$update_success,$err)
{
    $smarty->assign_array($info_arr);
    $smarty->assign("update_success",$update_success);
    $smarty->assign("is_editing",$is_editing);
    if(!is_null($err))
	$smarty->set_page_error($err->getErrorMsgs());
}

function intAdminInfo($is_editing=FALSE,$update_success=FALSE,$err=null)
{
    $admin_info=new GetAdminInfo($_REQUEST["admin_username"]);
    list($success,$info)=$admin_info->send();
    if(!$success)
	redirectToAdminList($info->getErrorMsg());
    else
	interface($info,$is_editing,$update_success,$err);
}

?>