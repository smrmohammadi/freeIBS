<?php
require_once("ippool.php");

function redirectToIPpoolInfo($ippool_name)
{
    redirect("/IBSng/admin/ippool/ippool_info.php?ippool_name={$ippool_name}");
}

function redirectToIPpoolList($msg)
{
    redirect("/IBSng/admin/ippool/ippool_list.php?msg={$msg}");
}

function intSetAllIPpoolNames(&$smarty)
{/*	set all available ippool names in "ippool_names" variable into smarty object
*/
    $ippool_list_req=new GetIPpoolNames();
    list($success,$ippool_names)=$ippool_list_req->send();
    if($success)
	$smarty->assign("ippool_names",$ippool_names);
    else
    {
	$smarty->assign("ippool_names",array());
	$smarty->set_page_error($ippool_names->gerErrorMsgs());
    }
}

?>