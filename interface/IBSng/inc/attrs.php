<?php
require_once(IBSINC."charge.php");

//***************************************************** Relative Exp Date


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


//***************************************************** Absolute Exp Date

function absExpDatePluginUpdate(&$update_helper)
{
    if(!isInRequest("has_abs_exp"))
	$update_helper->addToDelAttrs("abs_exp_date");
    else
    {
	$update_helper->addToUpdateAttrs("abs_exp_date",$_REQUEST["abs_exp_date"]);
	$update_helper->addToUpdateAttrs("abs_exp_date_unit",$_REQUEST["abs_exp_date_unit"]);
    }
}


//**************************************************** Multi Login



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

function normalChargePluginUpdate(&$update_helper)
{
    if(!isInRequest("has_normal_charge"))
	$update_helper->addToDelAttrs("normal_charge");
    else
	$update_helper->addToUpdateAttrs("normal_charge",$_REQUEST["normal_charge"]);
}

//**************************************************** IPpool
function IPpoolPluginUpdate(&$update_helper)
{
    if(!isInRequest("has_ippool"))
	$update_helper->addToDelAttrs("ippool");
    else
	$update_helper->addToUpdateAttrs("ippool",$_REQUEST["ippool"]);
}

//*************************************************** Radius Attrs
function radiusAttrsPluginUpdate(&$update_helper)
{
    if(!isInRequest("has_radius_attrs"))
	$update_helper->addToDelAttrs("radius_attrs");
    else
	$update_helper->addToUpdateAttrs("radius_attrs",$_REQUEST["radius_attrs"]);
}

//************************************* Group Name
function groupNamePluginUpdate(&$update_helper)
{
    if(isInRequest("group_name"))
	$update_helper->addToUpdateAttrs("group_name",$_REQUEST["group_name"]);
}
//************************************* Owner Name

function ownerNamePluginUpdate(&$update_helper)
{
    if(isInRequest("owner_name"))
	$update_helper->addToUpdateAttrs("owner_name",$_REQUEST["owner_name"]);
}
//*************************************
function normalAttrsPluginUpdate(&$update_helper)
{
    if(isInRequest("has_normal_username"))
    {
	$update_helper->addToUpdateAttrs("normal_username",$_REQUEST["normal_username"]);
	$update_helper->addToUpdateAttrs("normal_save_usernames",isInRequest("normal_save_user_add"));
	if(isInRequest("generate_password"))
	{
	    $update_helper->addToUpdateAttrs("normal_password","");
	    $generate_password=0;
	    if(isInRequest("password_character"))
		$generate_password+=1;
	    if(isInRequest("password_digit"))
		$generate_password+=2;
	
	    $update_helper->addToUpdateAttrs("normal_generate_password",$generate_password);
	    $update_helper->addToUpdateAttrs("normal_generate_password_len",$_REQUEST["password_len"]);
	}
	else
	{
	    $update_helper->addToUpdateAttrs("normal_generate_password",0);
	    $update_helper->addToUpdateAttrs("normal_generate_password_len",0);
	    $update_helper->addToUpdateAttrs("normal_password",$_REQUEST["password"]);
	}
    }
    else
	$update_helper->addToDelAttrs("normal_username");
}
//**************************************************
function lockPluginUpdate(&$update_helper)
{
    if(isInRequest("lock"))
	$update_helper->addToUpdateAttrs("lock",removeCR($_REQUEST["lock"]));
    else
	$update_helper->addToDelAttrs("lock");
}

//**************************************************
function persistentLanPluginUpdate(&$update_helper)
{
    if(isInRequest("has_plan"))
    {
	$update_helper->addToUpdateFromRequest("persistent_lan_mac");
	$update_helper->addToUpdateFromRequest("persistent_lan_ip");
	$update_helper->addToUpdateFromRequest("persistent_lan_ras_ip");
    }
    else
	$update_helper->addToDelAttrs("persistent_lan_mac");

}
//***************************************************
function commentPluginUpdate(&$update_helper)
{
    if(isInRequest("comment"))
	$update_helper->addToUpdateAttrs("comment",removeCR($_REQUEST["comment"]));
    else
	$update_helper->addToDelAttrs("comment");
}

//***************************************************
function limitMacPluginUpdate(&$update_helper)
{
    if(isInRequest("limit_mac"))
	$update_helper->addToUpdateFromRequest("limit_mac");
    else
	$update_helper->addToDelAttrs("limit_mac");
}

//************************** UNUSED CODE
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

function multiLoginParser(&$parsed_arr,&$smarty,&$attrs)
{
    assignToParsedIfExists($parsed_arr,$attrs,"multi_login");
}

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

?>
