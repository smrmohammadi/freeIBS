<?php
require_once("../inc/init.php");


if (isset($_REQUEST["username"]) and isset($_REQUEST["password"]))
    doLogin($_REQUEST["username"],$_REQUEST["password"]);    
else
    interface();

function doLogin($username,$password)
{
    list($success,$msg)=adminAuth($username,$password);
    if($success)
	goAdminIndex();
    else
	interface($msg);
}

function goAdminIndex()
{
    redirect("/IBSng/admin/admin_index.php");
}


function interface($msg=NULL)
{
    $smarty=new IBSSmarty();
    if(!is_null($msg))
	$smarty->assign("err_msgs",$msg->getErrorMsgs());
    $smarty->display("admin/index.tpl");    
}


?>
