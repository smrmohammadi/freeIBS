<?php

require_once("../../inc/init.php");
require_once(IBSINC."report.php");


needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();
intShowCreditChanges($smarty);

function intShowCreditChanges(&$smarty)
{
    if(isInRequest("show"))
	intSetReport($smarty);
    intAssignVars($smarty);
    $smarty->display("admin/report/credit_change.tpl");
}

function intAssignVars(&$smarty)
{
    $smarty->assign("actions",array("ADD_USER"=>"Add User","CHANGE_CREDIT"=>"Change Credit","DEL_USER"=>"Delete User","All"=>"All"));
    $smarty->assign("actions_default",requestVal("action","All"));
    $smarty->assign("order_bys",array("change_time"=>"Change Time",
				      "per_user_credit"=>"User Credit",
				      "admin_credit"=>"Admin Credit"));
    $smarty->assign("order_by_default",requestVal("order_by","change_time"));
}

function intSetReport(&$smarty)
{
    $do_empty=TRUE;
    $smarty->assign("show_report",TRUE);
    $conds=collectConditions();
    $report_helper=new ReportHelper();
    $req=new GetCreditChanges($conds,
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
	$total_per_user_credit=$result["total_per_user_credit"];
	$total_admin_credit=$result["total_admin_credit"];
	$do_empty=FALSE;
    }
    else
        $resp->setErrorInSmarty($smarty);
    	
    if($do_empty)
    {
	$report=array();
	$total_rows=0;
	$total_per_user_credit=0;
	$total_admin_credit=0;
    }
    $smarty->assign_by_ref("report",$report);
    $smarty->assign("total_rows",$total_rows);
    $smarty->assign("total_per_user_credit",$total_per_user_credit);
    $smarty->assign("total_admin_credit",$total_admin_credit);
}

function collectConditions() 
{ 
    $collector=new ReportCollector();
    $collector->addToCondsFromRequest(TRUE,"user_ids");
    $collector->addToCondsIfNotEq("action","All");
    $collector->addToCondsIfNotEq("admin","All");
	
    $collector->addToCondsFromRequest(TRUE,"change_time_from","change_time_from_unit");
    $collector->addToCondsFromRequest(TRUE,"change_time_to","change_time_to_unit");

    $collector->addToCondsFromRequest(TRUE,"per_user_credit","per_user_credit_op");

    $collector->addToCondsFromRequest(TRUE,"admin_credit","admin_credit_op");

    $collector->addToCondsFromRequest(FALSE,"show_total_per_user_credit");
    $collector->addToCondsFromRequest(FALSE,"show_total_admin_credit");

    $collector->addToCondsFromRequest(TRUE,"remote_addr");


    return $collector->getConds();    
}


?>