<?php
require_once("../../inc/init.php");
require_once(IBSINC."user_search.php");
require_once(IBSINC."report.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."charge_face.php");
require_once(IBSINC."admin_face.php");
require_once(IBSINC."perm.php");

function intDoSearch(&$smarty)
{
    $user_search_helper=new ReportCollector();
    $report_helper=new ReportHelper();
    intSetConditions($smarty,$user_search_helper);
    list($count,$user_ids,$user_infos)=searchUser($smarty,
	       $user_search_helper->getConds(),
	       $report_helper->getFrom(),
	       $report_helper->getTo(),
	       $report_helper->getOrderBy(),
	       $report_helper->getDesc());
    $smarty->assign_by_ref("user_infos",$user_infos);
    $smarty->assign_by_ref("user_ids",$user_ids);
    $smarty->assign("result_count",$count);
    $smarty->assign("show_results",TRUE);
    intShowUserSearch($smarty);
}
    
function intSetConditions(&$smarty,&$helper)
{
    $helper->addToCondsFromCheckBoxRequest("charge_name_","charge_name");
    $helper->addToCondsFromCheckBoxRequest("group_name_","group_name");
    $helper->addToCondsFromRequest(TRUE,"multi_login","multi_login_op");
    $helper->addToCondsFromRequest(TRUE,"normal_username","normal_username_op");
    $helper->addToCondsFromRequest(TRUE,"voip_username","voip_username_op");
    $helper->addToCondsFromCheckBoxRequest("owner_name_","owner_name");
    $helper->addToCondsFromRequest(TRUE,"normal_username","normal_username_op");
    $helper->addToCondsFromRequest(TRUE,"rel_exp_date","rel_exp_date_unit","rel_exp_date_op");
    $helper->addToCondsFromRequest(TRUE,"abs_exp_date","abs_exp_date_unit","abs_exp_date_op");
    $helper->addToCondsFromRequest(TRUE,"user_id");
    $helper->addToCondsFromRequest(TRUE,"credit","credit_op");
    $helper->addToCondsFromRequest(TRUE,"lock");
    $helper->addToCondsFromRequest(TRUE,"lock_reason");
    $helper->addToCondsFromRequest(TRUE,"ippool");
    $helper->addToCondsFromRequest(TRUE,"persistent_lan_mac");
    $helper->addToCondsFromRequest(TRUE,"persistent_lan_ip");
    $helper->addToCondsFromRequest(TRUE,"persistent_lan_ras_ip");
    $helper->addToCondsFromRequest(TRUE,"comment","comment_op");
    $helper->addToCondsFromRequest(TRUE,"limit_mac","limit_mac_op");
}


function intShowUserSearch(&$smarty)
{
    intShowUserSearchSetVars($smarty);
    $smarty->display("admin/user/search_user.tpl");
}


function intShowUserSearchSetVars(&$smarty)
{
    $smarty->assign_by_ref("group_names",getGroupNames($smarty));
    $smarty->assign_by_ref("admin_names",getAdminNames($smarty));
    intSetChargeNames($smarty,null);
    $smarty->assign("can_change",hasPerm("CHANGE USER ATTRIBUTES") or amIGod());
    $smarty->assign("order_by_options",array("user_id"=>"User ID",
						    "normal_username"=>"Normal Username",
						    "creation_date"=>"Creation Date",
						    "owner_id"=>"Owner ID",
						    "group_id"=>"Group ID",
						    "credit"=>"Credit"));
    if(!$smarty->is_assigned("show_results"))	$smarty->assign("show_results",FALSE);
}
?>