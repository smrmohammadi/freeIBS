<?php

require_once("../../inc/init.php");
require_once(IBSINC."report.php");


needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();
intShowConnections($smarty);

function intShowConnections(&$smarty)
{
    intSetReport($smarty);
    intAssignVars($smarty);
    $smarty->display("admin/report/connections.tpl");
}

function intAssignVars(&$smarty)
{
    $smarty->assign("services",array("internet","voip","All"));
    $smarty->assign("services_default",requestVal("services","All"));
    $smarty->assign("order_bys",array("user_id"=>"User ID",
				      "credit_used"=>"Credit Used",
				      "login_time"=>"Login Time",
				      "logout_time"=>"Logout Time",
				      "successful"=>"Succesful",
				      "service"=>"Service",
				      "ras_id"=>"Ras ID"));
    $smarty->assign("order_by_default",requestVal("order_by","login_time"));
    $smarty->assign("successful_options",array("Yes","No","All"));
    $smarty->assign("successful_default",requestVal("successful","All"));

}

function intSetReport(&$smarty)
{
    $do_empty=TRUE;
    if(isInRequest("show"))
    {
	$smarty->assign("show_report",TRUE);
	$conds=collectConditions();
	$report_helper=new ReportHelper();
	$req=new GetConnections($conds,
				$report_helper->getFrom(),
				$report_helper->getTo(),
				$report_helper->getOrderBy(),
				$report_helper->getDesc());
	$resp=$req->sendAndRecv();
	if($resp->isSuccessful())
	{
	    $result=$resp->getResult();
	    $report=$result["report"];
	    $total_rows=$result["total_rows"];
	    $total_credit=$result["total_credit"];
	    $total_duration=$result["total_duration"];
	    $do_empty=FALSE;
	}
	else
	    $resp->setErrorInSmarty($smarty);
    }	
    
    if($do_empty)
    {
	$report=array();
	$total_rows=0;
	$total_credit=0;
	$total_duration=0;
    }
    $smarty->assign_by_ref("report",$report);
    $smarty->assign("total_rows",$total_rows);
    $smarty->assign("total_credit",$total_credit);
    $smarty->assign("total_duration",$total_duration);
}

function collectConditions() 
{ 
    $collector=new ReportCollector();
    $collector->addToCondsFromRequest(TRUE,"user_ids");
    $collector->addToCondsIfNotEq("services","All");
    $collector->addToCondsIfNotEq("succesful","All");
    $collector->addToCondsIfNotEq("owner","All");
	
    $collector->addToCondsFromRequest(TRUE,"login_time","login_time_unit");
    $collector->addToCondsFromRequest(TRUE,"logout_time","logout_time_unit");
    $collector->addToCondsFromRequest(TRUE,"credit_used","credit_used_op");

    $collector->addToCondsFromRequest(FALSE,"show_total_credit_used");
    $collector->addToCondsFromRequest(FALSE,"show_total_duration");

    $collector->addToCondsFromCheckBoxRequest("ras_","ras_ip");

    return $collector->getConds();    
}


?>