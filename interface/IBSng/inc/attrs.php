<?php
//***************************************************** Relative Exp Date

function relExpParser(&$parsed_arr,&$smarty,&$attrs)
{
    if(!isset($attrs["rel_exp_date"]))
    {
	$parsed_arr["has_rel_exp"]=FALSE;
        $parsed_arr["rel_exp_date_unit"]=null;
	$parsed_arr["rel_exp_date"]=null;
    }
    else
    {
	$parsed_arr["has_rel_exp"]=TRUE;
	$rel_exp=(int)$attrs["rel_exp_date"];
	list($rel_exp,$rel_exp_unit)=calcRelativeDateFromHours($rel_exp);
        $parsed_arr["rel_exp_date_unit"]=$rel_exp_unit;
	$parsed_arr["rel_exp_date"]=$rel_exp;
    }
}

function expDatePluginUpdate(&$update_helper)
{
    $to_del_attrs=array();
    $update_attrs=array();

    if(!isInRequest("has_rel_exp"))
	$to_del_attrs[]="rel_exp_date";
    else
    {
	$update_attrs["rel_exp_date"]=$_REQUEST["rel_exp_date"];	
	$update_attrs["rel_exp_date_unit"]=$_REQUEST["rel_exp_date_unit"];
    }
    $update_helper->updateTargetAttrs($update_attrs,$to_del_attrs,FALSE);
}


//**************************************************** Multi Login

function multiLoginParser(&$parsed_arr,&$smarty,&$attrs)
{
    assignToParsedIfExists($parsed_arr,$attrs,"multi_login");
}


function multiLoginPluginUpdate(&$update_helper)
{
    $to_del_attrs=array();
    $update_attrs=array();

    if(!isInRequest("has_multi_login"))
	$to_del_attrs[]="multi_login";
    else
	$update_attrs["multi_login"]=$_REQUEST["multi_login"];

    $update_helper->updateTargetAttrs($update_attrs,$to_del_attrs,FALSE);
}

//**************************************************** Group Info

function groupInfoPluginUpdate(&$update_helper)
{
    $update_helper->mustBeInRequest("group_id","group_name","owner_name","comment");
    $update_group_req=new UpdateGroup($_REQUEST["group_id"],$_REQUEST["group_name"],$_REQUEST["comment"],$_REQUEST["owner_name"]);
    list($success,$err)=$update_group_req->send();
    if($success)
    {
	$update_helper->target_id=$_REQUEST["group_name"];
	$update_helper->redirectToTargetInfo();
    }
    else
	$update_helper->showEditInterface($err);
}

//**************************************************** Normal Charge

function normalChargeParser(&$parsed_arr,&$smarty,&$attrs)
{
    assignToParsedIfExists($parsed_arr,$attrs,"normal_charge");
}


?>
