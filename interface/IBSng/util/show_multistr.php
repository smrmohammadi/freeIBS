<?php
require_once("../inc/init.php");
require_once(IBSINC."util.php");


if(isInRequest("str"))
    showMultiStr($_REQUEST["str"]);
else
{
    print "Invalid inputs";
    exit();
}


function showMultiStr($raw_str)
{
    $smarty=new IBSSmarty();
    intSetAllStrs($smarty,$raw_str);
    $smarty->assign("raw_str",$raw_str);
    $smarty->display("util/show_multistr.tpl");
}

function intSetAllStrs(&$smarty,$raw_str)
{
    $get_all_strs_req=new MultiStrGetAll($raw_str);
    list($success,$strs)=$get_all_strs_req->send();
    if($success)
	$smarty->assign("all_strs",$strs);
    else
    {
	$smarty->set_page_error($strs->getErrorMsgs());
	$smarty->assign("all_strs",array());    
    }
}

?>