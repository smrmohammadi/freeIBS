<?php
require_once("../inc/init.php");


if (isInRequest("logout"))
    doLogout();
else if (isInRequest("username","password"))
    doLogin($_REQUEST["username"],$_REQUEST["password"]);
else
    interface();

function doLogout()
{
    session_unset();
    auth_init();
    interface();
}

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


function interface($err=NULL)
{
    $smarty=new IBSSmarty();
    if(!is_null($err))
	$smarty->set_page_error($err->getErrorMsgs());
    $smarty->display("admin/index.tpl");    
}


?>
