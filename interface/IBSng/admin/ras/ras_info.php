<?php
require_once("../../inc/init.php");
require_once(IBSINC."ras.php");
require_once(IBSINC."ras_face.php");
require_once(IBSINC."perm.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();
$smarty->assign("is_editing",FALSE);
$smarty->assign("attr_editing",FALSE);





if(isInRequest("ras_ip","del_port"))
    intDelPort($smarty,$_REQUEST["ras_ip"],$_REQUEST["del_port"]);
else if(isInRequest("ras_ip","reset_attrs"))
    intResetAttrs($smarty,$_REQUEST["ras_ip"]);
else if (isInRequest("ras_ip","attr_editing_done"))
    intUpdateAttrs($smarty,$_REQUEST["ras_ip"],$_REQUEST);
else if (isInRequest("ras_ip","edit_attrs"))
    intEditAttrs($smarty,$_REQUEST["ras_ip"]);
else if (isInRequest("ras_id","ras_ip","old_ras_ip","edit","radius_secret","ras_type"))
    intUpdateRasInfo($smarty,$_REQUEST["ras_id"],$_REQUEST["ras_ip"],$_REQUEST["old_ras_ip"],$_REQUEST["ras_type"],$_REQUEST["radius_secret"]);
else if (isInRequest("ras_ip","edit"))
    intEditRasInfo($smarty,$_REQUEST["ras_ip"]);
else if(isInRequest("ras_ip"))
    intRasInfo($smarty,$_REQUEST["ras_ip"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToRasList($err->getErrorMsg());
}

function intDelPort(&$smarty,$ras_ip,$port_name)
{
    $del_port_req=new DelRasPort($ras_ip,$port_name);
    list($success,$err)=$del_port_req->send();
    if($success)
	$smarty->assign("del_port_success",TRUE);
    else
	$smarty->set_page_error($err->getErrorMsgs());

    intRasInfo($smarty,$ras_ip);	
}

function intResetAttrs(&$smarty,$ras_ip)
{
    $reset_req=new ResetRasAttributes($ras_ip);
    list($success,$err)=$reset_req->send();
    if($success)

    intRasInfo($smarty,$ras_ip);	
}

function intUpdateAttrs(&$smarty,$ras_ip,$request_arr)
{
    $attrs=catchAttributesInRequest($request_arr);
    $update_attr_req=new UpdateRasAttributes($ras_ip,$attrs);
    list($success,$err)=$update_attr_req->send();
    if($success)
    {
	$smarty->assign("update_ras_attrs_success",TRUE);
	intRasInfo($smarty,$ras_ip);
    }
    else
    {
	$smarty->set_page_error($err->getErrorMsgs());
	intEditAttrs($smarty,$ras_ip);
    }
}

function catchAttributesInRequest($request_arr)
{
    $attrs=array();
    foreach ($request_arr as $key=>$value)
	if (preg_match("/^attr__(.*)/",$key,$matches))
	    $attrs[$matches[1]]=$value;

    return $attrs;    
}

function intEditAttrs(&$smarty,$ras_ip)
{
    $smarty->assign("attr_editing",TRUE);
    intRasInfo($smarty,$ras_ip);
}	


function intUpdateRasInfo(&$smarty,$ras_id,$ras_ip,$old_ras_ip,$ras_type,$radius_secret)
{
    $update_req=new UpdateRasInfo($ras_id,$ras_ip,$ras_type,$radius_secret);
    list($success,$err)=$update_req->send();
    if(!$success)
    {
	intUpdateRasSetErrors($smarty,$err);
	intEditRasInfo($smarty,$old_ras_ip);
    }
    else
    {
	$smarty->assign("update_ras_info_success",TRUE);    
	intRasInfo($smarty,$ras_ip);
    }
}

function intUpdateRasSetErrors(&$smarty,$err)
{
    $smarty->set_page_error($err->getErrorMsgs());
    $smarty->set_field_errs(array("ras_ip_err"=>array("INVALID_RAS_IP",
						      "RAS_IP_ALREADY_EXISTS",
						      "RAS_IS_INACTIVE"),
				     "ras_type_err"=>array("RAS_TYPE_NOT_REGISTERED")
				    ),$err->getErrorKeys());
}

function intEditRasInfo(&$smarty,$ras_ip)
{
    $smarty->assign("is_editing",TRUE);
    intSetRasTypes($smarty);
    intRasInfo($smarty,$ras_ip);
}

function intRasInfo(&$smarty,$ras_ip)
{
    $ras_info_req=new GetRasInfo($ras_ip);
    list($success,$info)=$ras_info_req->send();
    if(!$success)
	redirectToRasList($info->getErrorMsg());
    
    $ras_attrs_req=new GetRasAttributes($ras_ip);
    list($success,$attrs)=$ras_attrs_req->send();
    if(!$success)
	interface($smarty,$info,array(),array(),$attrs);

    $ras_ports_req=new GetRasPorts($ras_ip);
    list($success,$ports)=$ras_ports_req->send();
    if(!$success)
	interface($smarty,$info,$attrs,array(),$ports);
    
    interface($smarty,$info,$attrs,$ports,null);

}

function interface(&$smarty,$info,$attrs,$ports,$err=null,$is_editing=FALSE)
{
    intAssignValues($smarty,$info,$attrs,$ports,$err,$is_editing);
    $smarty->display("admin/ras/ras_info.tpl");
    exit();
}

function intAssignValues(&$smarty,$info,$attrs,$ports,$err)
{
    $smarty->assign_array(array("info"=>$info,"attrs"=>$attrs,"ports"=>$ports,"can_change"=>canDo("CHANGE RAS")));
    if (!is_null($err))
	$smarty->set_page_error($err->getErrorMsgs());
	
}

?>