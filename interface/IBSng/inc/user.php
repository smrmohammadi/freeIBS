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

?>
