<?php
require_once("init.php");

class AddNewIPpool extends Request
{
    function AddNewIPpool($ippool_name,$comment)
    {
	parent::Request("ippool.addNewIPpool",array("ippool_name"=>$ippool_name,
					    	    "comment"=>$comment));
    }
}

class UpdateIPpool extends Request
{
    function UpdateIPpool($ippool_id,$ippool_name,$comment)
    {
	parent::Request("ippool.updateIPpool",array("ippool_id"=>$ippool_id,
					    	    "ippool_name"=>$ippool_comment,
					    	    "comment"=>$comment));
    }
}

class GetIPpoolNames extends Request
{
    function GetIPpoolNames()
    {
	parent::Request("ippool.getIPpoolNames",array());
    }
}

class GetIPpoolInfo extends Request
{
    function GetIPpoolInfo($ippool_name)
    {
	parent::Request("ippool.getIPpoolNames",array("ippool_name"=>$ippool_name));
    }
}

class DeleteIPpool extends Request
{
    function DeleteIPpool($ippool_name)
    {
	parent::Request("ippool.deleteIPpool",array("ippool_name"=>$ippool_name));
    }
}

class DelIPfromPool extends Request
{
    function DelIPfromPool($ippool_name,$ip)
    {
	parent::Request("ippool.delIPfromPool",array("ippool_name"=>$ippool_name,
						     "ip"=>$ip));
    }
}

class AddIPtoPool extends Request
{
    function AddIPtoPool($ippool_name,$ip)
    {
	parent::Request("ippool.addIPtoPool",array("ippool_name"=>$ippool_name,
						   "ip"=>$ip));
    }
}


?>