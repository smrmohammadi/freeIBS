<?php
require_once("../../inc/init.php");
require_once(IBSINC."user.php");


needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();

if(isInRequest("user_id","username","ras_ip","unique_id_val"))
    intKillUser($smarty,$_REQUEST["user_id"],$_REQUEST["username"],$_REQUEST["ras_ip"],$_REQUEST["unique_id_val"]);
else
    interface($smarty,"Invalid Input");

function interface(&$smarty,$err="")
{
    if($err!="")
	$smarty->set_page_error($err);
    $smarty->display("admin/user/kill_user.tpl");
}

function intKillUser(&$smarty,$user_id,$username,$ras_ip,$unique_id_val)
{
    $req=new KillUser($user_id,$ras_ip,$unique_id_val);
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
	$smarty->assign("success",TRUE);
    else
	$resp->setErrorInSmarty($smarty);
    $smarty->assign("username",$username);
    interface($smarty);
}
?>