<?php
require_once("init.php");

class AddNewUsers extends Request
{
    function AddNewUsers($count,$credit,$owner_name,$group_name,$credit_comment)
    {
	parent::Request("user.addNewUsers",array("count"=>$count,
					         "credit"=>$credit,
						 "owner_name"=>$owner_name,
						 "group_name"=>$group_name,
						 "credit_comment"=>$credit_comment
						 ));
    }
}

class GetUserInfo extends Request
{
    function GetUserInfo($user_id=null,$normal_username=null)
    {
	if (!is_null($user_id))
	    $request=array("user_id"=>$user_id);
	else if (!is_null($normal_username))
	    $request=array("normal_username"=>$normal_username);
	parent::Request("user.getUserInfo",$request);
    }
}



?>
