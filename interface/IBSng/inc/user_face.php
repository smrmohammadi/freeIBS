<?php
require_once("init.php");
require_once("attr_parser.php");


function intSetSingleUserInfo(&$smarty,$user_id,$normal_username=null)
{
    $user_info_req=new GetUserInfo($user_id,$normal_username);
    $resp=$user_info_req->sendAndRecv();
    if($resp->isSuccessful())
    {
	$smarty->assign("user_info",$resp->getResult());
        $smarty->assign("user_attrs",parseAttrs($smarty,$user_info["attrs"]));
    }
    else
	$resp->setErrorInSmarty($smarty);
    return $resp;
}

?>
