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

class UpdateUserAttrs extends Request
{
    function UpdateUserAttrs($user_id,$attrs,$to_del_attrs)
    {
	parent::Request("user.updateUserAttrs",array("user_id"=>$user_id,
						       "attrs"=>$attrs,
						       "to_del_attrs"=>$to_del_attrs));
    }
}

class CheckNormalUsernameForAdd extends Request
{
    function CheckNormalUsernameForAdd($username,$current_username)
    {
	parent::Request("user.checkNormalUsernameForAdd",array("normal_username"=>$username,
							       "current_username"=>$current_username));
    }
}

class ChangeUserCredit extends Request
{
    function ChangeUserCredit($user_id,$credit,$credit_comment)
    {
	parent::Request("user.changeCredit",array("user_id"=>$user_id,
						  "credit"=>$credit,
						  "credit_comment"=>$credit_comment));
    }
}


function getUsersInfoByUserID(&$smarty,$user_ids)
{/*return a list of user_infos of users with id in $user_ids
 */ 
    if(sizeof($user_ids)==0)
	return array();

    $req=new GetUserInfo(join(",",$user_ids));
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
	return $resp->getResult();
    else
    {
	$resp->setErrorInSmarty($smarty);
	return array();
    }
}

?>
