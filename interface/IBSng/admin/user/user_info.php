<?php
require_once("user_info_funcs.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();

if(isInRequest("user_id"))
    intShowSingleUserInfo($smarty,$_REQUEST["user_id"]);
else if (isInRequest("normal_username"))
    intShowSingleUserInfo($smarty,null,$_REQUEST["normal_username"]);
else if (isInRequest("user_id_multi"))
    intShowMultiUserInfo($smarty,$_REQUEST["user_id_multi"]);
else if (isInRequest("normal_username_multi"))
    intShowMultiNormalUserInfo($smarty,$_REQUEST["normal_username_multi"]);
else
    intShowSingleUserInfoInput($smarty);



?>