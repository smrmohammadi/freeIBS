<?php
require_once("../../inc/init.php");
require_once(IBSINC."bw_face.php");
require_once(IBSINC."bw.php");

needAuthType(ADMIN_AUTH_TYPE);

if(isInRequest("interface_name","parent_id","limit_kbits"))
    intAddNode($_REQUEST["interface_name"],$_REQUEST["parent_id"],$_REQUEST["limit_kbits"]);
else if (isInRequest("interface_name","parent_id"))
    interface($_REQUEST["interface_name"],$_REQUEST["parent_id"]);
else
    redirectToInterfaceList();

function intAddNode($interface_name,$parent_id,$limit_kbits)
{
    $req=new AddNode($interface_name,$parent_id,$limit_kbits);
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
      	redirectToInterfaceInfo($interface_name);
    else
	interface($interface_name,$parent_id,$resp->getError());
}

function interface($interface_name,$parent_id,$err=NULL)
{
    $smarty=new IBSSmarty();
    intAssignValues($smarty,$interface_name,$parent_id);
    if(!is_null($err))
    {
	intSetErrors($smarty,$err->getErrorKeys());
	$smarty->set_page_error($err->getErrorMsgs());
    }
    $smarty->display("admin/bw/add_node.tpl");
}

function intAssignValues(&$smarty,$interface_name,$parent_id)
{
    $smarty->assign("interface_name",$interface_name);
    $smarty->assign("parent_id",$parent_id);
}

function intSetErrors(&$smarty,$err_keys)
{
    $smarty->set_field_errs(array("limit_kbits_err"=>array("INVALID_LIMIT_KBITS")),$err_keys);
}

?>