<?php
require_once("../../inc/init.php");
require_once(IBSINC."bw_face.php");
require_once(IBSINC."bw.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();
if(isInRequest("add","interface_name","leaf_name","parent_id","total_limit_kbits","default_limit_kbits"))
    intAddLeaf($smarty,$_REQUEST["interface_name"],$_REQUEST["leaf_name"],$_REQUEST["parent_id"],$_REQUEST["total_limit_kbits"],$_REQUEST["default_limit_kbits"]);
else if (isInRequest("add","interface_name","parent_id"))
    addInterface($smarty,$_REQUEST["interface_name"],$_REQUEST["parent_id"]);
else
    redirectToInterfaceList();

function intAddLeaf(&$smarty,$interface_name,$leaf_name,$parent_id,$total_kbits,$default_kbits)
{
    $req=new AddLeaf($leaf_name,$parent_id,$default_kbits,$total_kbits);
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
      	redirectToInterfaceInfo($interface_name);
    else
	addInterface($smarty,$interface_name,$parent_id,$resp->getError());
}

function addInterface(&$smarty,$interface_name,$parent_id,$err=NULL)
{
    intAddAssignValues($smarty,$interface_name,$parent_id);
    if(!is_null($err))
    {
	intSetErrors($smarty,$err->getErrorKeys());
	$smarty->set_page_error($err->getErrorMsgs());
    }
    $smarty->display("admin/bw/add_leaf.tpl");
}

function intAddAssignValues(&$smarty,$interface_name,$parent_id)
{
    $smarty->assign("interface_name",$interface_name);
    $smarty->assign("parent_id",$parent_id);
    $smarty->assign("action","add");
    $smarty->assign("action_title","Add");
    $smarty->assign("action_icon","add");
}

function intSetErrors(&$smarty,$err_keys)
{
    $smarty->set_field_errs(array("default_limit_kbits_err"=>array("INVALID_LIMIT_KBITS"),
				  "total_limit_kbits_err"=>array("INVALID_TOTAL_LIMIT_KBITS"),
				  "leaf_name_err"=>array("INVALID_LEAF_NAME","LEAF_NAME_ALREADY_EXISTS")
			    ),$err_keys);
}

?>