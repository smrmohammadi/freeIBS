<?php

require_once("../../inc/init.php");
require_once(IBSINC."report.php");


needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();
intShowOnlineUsers($smarty);

function intShowOnlineUsers(&$smarty)
{
    $report_helper=new ReportHelper();
    $req=new GetOnlineUsers($report_helper->getOrderBy(),$report_helper->getDesc());
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
	$onlines=$resp->getResult();
    else
    {
	$resp->setErrorInSmarty($smarty);
	$onlines=array();
    }
    intShowOnlinesByType($smarty,$onlines);
}


function intShowOnlinesByType(&$smarty,$onlines)
{
    $smarty->assign_by_ref("onlines",$onlines);
    $smarty->assign("refresh_times",array(5,10,20,30,60));
    $smarty->assign("refresh_default",requestVal("refresh",10));
    $smarty->display("admin/report/online_users_by_type.tpl");
}



?>