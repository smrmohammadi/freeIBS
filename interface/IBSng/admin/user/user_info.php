<?php
require_once("../../inc/init.php");
require_once(IBSINC."user.php");
require_once(IBSINC."user_face.php");
require_once(IBSINC."group_face.php");

if(isInRequest("user_id"))
    intShowSingleUserInfoByUserID($_REQUEST["user_id"]);
else if (isInRequest("normal_username"))
    intShowSingleUserInfoByNormalUsername($_REQUEST["normal_username"]);
else if (isInRequest("user_id_multi")){}
else if (isInRequest("normal_username_multi")){}  
else
    intShowUserInfoInput();

function intShowSingleUserInfoByUserID($user_id)
{
    $user_info_req=new GetUserInfo($user_id);
    list($success,$info)=$user_info_req->send();
    if($success)
	intShowSingleUserInfo($info);
    else
	intShowUserInfoInput($info);
}

function intShowSingleUserInfoByNormalUsername($normal_username)
{
    $user_info_req=new GetUserInfo(null,$normal_username);
    list($success,$info)=$user_info_req->send();
    if($success)
	intShowSingleUserInfo($info);
    else
	intShowUserInfoInput($info);
    
}

function intShowSingleUserInfo($user_info)
{
    $smarty=new IBSSmarty();
    intShowSingleUserInfoAssignValues($smarty,$user_info)
    intShowSingleUserInfoInterface($smarty)
}

function intShowSingleUserInfoAssignValues(&$smarty,$user_info)
{
    $smarty->assign_array($user_info);
    $smarty->assign_array(callAttrParsers($smarty,$user_info["attrs"]));
    intSetGroupFace($smarty,$user_info["basic_info"]["group_name"]);
}

function intShowSingleUserInfoInterface(&$smarty)
{
    $smarty->display("admin/user/user_info.tpl");
}

?>