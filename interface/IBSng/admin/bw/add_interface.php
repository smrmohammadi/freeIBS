<?php
require_once("../../inc/init.php");
require_once(IBSINC."bw_face.php");
require_once(IBSINC."bw.php");

needAuthType(ADMIN_AUTH_TYPE);

if(isInRequest("interface_name","comment"))
    intAddInterface($_REQUEST["interface_name"],$_REQUEST["comment"]);
else
    interface();

function intAddInterface($interface_name,$comment)
{
    $req=new AddInterface($interface_name,$comment);
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
      	redirectToInterfaceInfo($interface_name);
    else
	interface($resp->getError());
}

function interface($err=NULL)
{
    $smarty=new IBSSmarty();
    if(!is_null($err))
    {
	intSetErrors($smarty,$err->getErrorKeys());
	$smarty->set_page_error($err->getErrorMsgs());
    }
    $smarty->display("admin/bw/add_interface.tpl");    
}

function intSetErrors(&$smarty,$err_keys)
{
    $smarty->set_field_errs(array("interface_name_err"=>array("INVALID_INTERFACE_NAME",
							   "INTERFACE_NAME_ALREADY_EXISTS")
							   ),$err_keys);
}

?>