<?php
require_once("../../inc/init.php");
require_once("search_user_funcs.php");
require_once("../plugins/edit_funcs.php");

needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();
searchUserEdit($smarty);

function searchUserEdit(&$smarty)
{
    $user_ids=getSelectedUserIDsFromRequest();
    if(sizeof($user_ids)==0)
    {
	$smarty->set_page_error("No users selected!");
	intShowUserSearch($smarty);
    }
    else
	intEditUser($smarty,join(",",$user_ids));
}

function getSelectedUserIDsFromRequest()
{
    $user_ids=array();
    foreach($_REQUEST as $key=>$value)
	if(preg_match("/^edit_user_id_[0-9]+$/",$key))
	    $user_ids[]=$value;
    return $user_ids;
}
?>