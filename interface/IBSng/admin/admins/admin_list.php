<?php
require_once("../../inc/init.php");
require_once(IBSINC."admin.php");

needAuthType(ADMIN_AUTH_TYPE);
intAdminList();

function intAdminList()
{
    list($success,$admin_infos)=getAllAdminInfos();
    if(!$success)
	interface(array(),$admin_infos);
    else
	interface($admin_infos,null);    
}

function interface($admin_infos,$errs=null)
{
    $smarty=new IBSSmarty();
    intSetErrors($smarty,$errs);
    $smarty->assign("admin_infos",$admin_infos);
    $smarty->display("admin/admins/admin_list.tpl");
}

function intSetErrors(&$smarty,$errs)
{
    if(isInRequest("msg"))
	$smarty->set_page_error(array($_REQUEST["msg"]));
    if($errs!=null)    
    	$smarty->set_page_error($errs->getErrorMsgs());
}

?>