<?php
require_once("../../inc/init.php");
require_once(IBSINC."user.php");
require_once(IBSINC."user_face.php");
require_once(IBSINC."group_face.php");


$smarty=new IBSSmarty();

if(isInRequest("user_id"))
    intShowSingleUserInfo($smarty,$_REQUEST["user_id"]);
else if (isInRequest("normal_username"))
    intShowSingleUserInfo($smarty,null,$_REQUEST["normal_username"]);
else if (isInRequest("user_id_multi")){}
else if (isInRequest("normal_username_multi")){}
else
    intShowSingleUserInfoInput($smarty);


//********************************************
function intShowSingleUserInfo(&$smarty,$user_id,$normal_username=null)
{
    $resp=intSetSingleUserInfo(&$smarty,$user_id,$normal_username);
    if($resp->isSuccessful())
    {
        intShowSingleUserInfoAssignValues($smarty,$resp->getResult());
	intShowSingleUserInfoInterface($smarty);
    }
    else
	intShowSingleUserInfoInput($smarty);
}

function intShowSingleUserInfoAssignValues(&$smarty)
{
    intSetGroupInfo($smarty,$user_info["basic_info"]["group_name"]);
}

function intShowSingleUserInfoInterface(&$smarty)
{
    $smarty->display("admin/user/user_info.tpl");
}
//*********************************************

function intShowSingleUserInfoInput(&$smarty)
{
    $smarty->display("admin/user/single_user_info_input.tpl");
}


?>