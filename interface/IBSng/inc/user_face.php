<?php
require_once("init.php");
require_once("attr_parser.php");
require_once(INTERFACE_ROOT."IBSng/admin/user/user_info_funcs.php");

function redirectToUserInfo($user_id)
{
    $redirect_str="/IBSng/admin/user/user_info.php?user_id_multi={$user_id}";
    redirect($redirect_str);
}

function intSetSingleUserInfo(&$smarty,$user_id,$normal_username=null)
{
    $user_info_req=new GetUserInfo($user_id,$normal_username);
    $resp=$user_info_req->sendAndRecv();
    if($resp->isSuccessful())
    {
	$user_info=$resp->getResult();
	$user_info=array_values($user_info);
	intSetSingleUserInfoIntoSmarty($smarty,$user_info[0]);
    }
    else
	$resp->setErrorInSmarty($smarty);
    return $resp;
}

function intSetSingleUserInfoIntoSmarty(&$smarty,$user_info)
{
    $smarty->assign("user_id",$user_info["basic_info"]["user_id"]);
    $smarty->assign("user_info",$user_info);
    $smarty->assign("user_attrs",parseAttrs($smarty,$user_info["attrs"]));
}

function intSetSingleUserGroupAttrs(&$smarty,$user_info)
{
    intSetGroupInfo($smarty,$user_info["basic_info"]["group_name"]);
}

?>
