<?php
require_once(IBSINC."charge.php");

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

function relExpDatePluginUpdate(&$update_helper)
{
    if(!isInRequest("has_rel_exp"))
	$update_helper->addToDelAttrs("rel_exp_date");
    else
    {
	$update_helper->addToUpdateAttrs("rel_exp_date",$_REQUEST["rel_exp_date"]);
	$update_helper->addToUpdateAttrs("rel_exp_date_unit",$_REQUEST["rel_exp_date_unit"]);
    }
}


//**************************************************** Multi Login

function multiLoginParser(&$parsed_arr,&$smarty,&$attrs)
{
    assignToParsedIfExists($parsed_arr,$attrs,"multi_login");
}


function multiLoginPluginUpdate(&$update_helper)
{
    if(!isInRequest("has_multi_login"))
	$update_helper->addToDelAttrs("multi_login");
    else
	$update_helper->addToUpdateAttrs("multi_login",$_REQUEST["multi_login"]);
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
    if(isset($attrs["normal_charge"]))
    { //translate charge_id to charge_name
	$charge_info_req=new GetChargeInfo(null,$attrs["normal_charge"]);
	list($success,$info)=$charge_info_req->send();
	if($success)
	    $parsed_arr["normal_charge"]=$info["charge_name"];
	else
	    $smarty->set_page_error($info->getErrorMsgs());
    }
}

function normalChargePluginUpdate(&$update_helper)
{
    if(!isInRequest("has_normal_charge"))
	$update_helper->addToDelAttrs("normal_charge");
    else
	$update_helper->addToUpdateAttrs("normal_charge",$_REQUEST["normal_charge"]);
}


?>
