<?php
require_once("../../inc/init.php");
require_once(IBSINC."ras_face.php");
require_once(IBSINC."charge_face.php");
require_once(IBSINC."charge.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();


if(isInRequest("charge_name","charge_rule_id","rule_start","rule_end","cpm","cpk","assumed_kps","bandwidth_limit_kbytes","ras"))
    intUpdateInternetRule($smarty,$_REQUEST["charge_name"],$_REQUEST["charge_rule_id"],$_REQUEST["rule_start"],$_REQUEST["rule_end"],
		       $_REQUEST["cpm"],$_REQUEST["cpk"],$_REQUEST["assumed_kps"],$_REQUEST["bandwidth_limit_kbytes"],
		       $_REQUEST["ras"]);
else if (isInRequest("charge_name","charge_rule_id"))
    intEditInternetRule($smarty,$_REQUEST["charge_name"],$_REQUEST["charge_rule_id"]);
else
    redirectToChargeList();

function intUpdateInternetRule(&$smarty,$charge_name,$charge_rule_id,$rule_start,$rule_end,$cpm,$cpk,
			    $assumed_kps,$bandwidth_limit_kbytes,$ras_ip)
{
    $dows=intFindDowsInRequest();
    $ports=intGetRasPortsRequest(escapeIP($ras_ip));
    $update_req=new UpdateInternetChargeRule($charge_name,$charge_rule_id,$rule_start,$rule_end,$cpm,$cpk,
			    $assumed_kps,$bandwidth_limit_kbytes,$ras_ip,$ports,$dows);
    list($success,$err)=$update_req->send();
    if($success)
	redirectToChargeInfo($charge_name,"update_charge_rule_success=1");
    else
    {
	$smarty->set_page_error($err->getErrorMsgs());
	intSetFieldErrors($smarty,$err->getErrorKeys());
	intEditInternetRule($smarty,$charge_name,$charge_rule_id);
    }
}


function intEditInternetRule(&$smarty,$charge_name,$charge_rule_id)
{
    list($success,$rule_info)=intGetRuleInfo($charge_name,$charge_rule_id);
    if($success)
	intSetRuleInfo($smarty,$rule_info);
    else
	$smarty->set_page_error($rule_info->getErrorMsgs());

    interface($smarty,$charge_name);
}

function intGetRuleInfo($charge_name,$charge_rule_id)
{
    $list_rules_req=new ListChargeRules($charge_name);
    list($success,$rules)=$list_rules_req->send();
    if(!$success)
	return array(FALSE,$rules);
    foreach($rules as $rule)
	if ($rule["rule_id"]==$charge_rule_id)
	    return array(TRUE,$rule);

    redirectToChargeList("Invalid Rule ID");
}

function intSetRuleInfo(&$smarty,$rule_info)
{
    $smarty->assign_array($rule_info);
    intSetDayOfWeeksParams($smarty,$rule_info);
    intSetRasParams($smarty,$rule_info);
}

function intSetDayOfWeeksParams(&$smarty,$rule_info)
{
    foreach($rule_info["day_of_weeks"] as $dow)
	$smarty->assign($dow,"checked");
}

function intSetRasParams(&$smarty,$rule_info)
{
    $smarty->assign("ras_selected",requestVal("ras",$rule_info["ras"]));
    if($rule_info["ras"]!="_ALL_")
	foreach ($rule_info["ports"] as $port_name)
		$smarty->assign("{$rule_info["ras"]}_{$port_name}","checked");
}

function interface(&$smarty,$charge_name)
{
    intSetDayOfWeeks($smarty);
    intSetRasAndPorts($smarty);
    intAssignValues($smarty,$charge_name);
    $smarty->display("admin/charge/add_internet_charge_rule.tpl");    
}

function intAssignValues(&$smarty,$charge_name)
{
    $smarty->assign("charge_name",$charge_name);
    $smarty->assign("check_all_days",FALSE);
    $smarty->assign("is_editing",TRUE);
}

function intSetFieldErrors(&$smarty,$err_keys)
{
    $smarty->set_field_errs(array("rule_start_err"=>array("INVALID_RULE_START_TIME","RULE_END_LESS_THAN_START"),
				  "rule_end_err"=>array("INVALID_RULE_END_TIME","RULE_END_LESS_THAN_START"),
				  "dow_err"=>array("INVALID_DAY_OF_WEEK"),
				  "cpm_err"=>array("CPM_NOT_NUMERIC","CPM_NOT_POSITIVE"),
				  "cpk_err"=>array("CPK_NOT_NUMERIC","CPK_NOT_POSITIVE"),
				  "assumed_kps_err"=>array("ASSUMED_KPS_NOT_INTEGER","ASSUMED_KPS_NOT_POSITIVE"),
				  "bw_limit_err"=>array("BANDWIDTH_LIMIT_NOT_INTEGER","BANDWIDTH_LIMIT_NOT_POSITIVE")
				  ),$err_keys);

}
