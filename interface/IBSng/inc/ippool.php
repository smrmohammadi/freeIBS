<?php
require_once("init.php");

class AddNewIPpool extends Request
{
    function AddNewIPpool($ippool_name,$comment)
    {
	parent::Request("ippool.addNewIPpool",array("ippool_name"=>$ippool_comment,
					    	    "comment":$comment));
    }
}

class UpdateIPpool extends Request
{
    function AddNewIPpool($ippool_id,$ippool_name,$comment)
    {
	parent::Request("ippool.updateIPpool",array("ippool_id"=>$ippool_id,
					    	    "ippool_name"=>$ippool_comment,
					    	    "comment":$comment));
    }
}

class getIPpoolNames extends Request
{
    function getIPpoolNames()
    {
	parent::Request("ippool.getIPpoolNames",array());
    }
}

class getIPpoolInfo extends Request
{
    function getIPpoolNames($ippool_name)
    {
	parent::Request("ippool.getIPpoolNames",array("ippool_name"=>$ippool_name));
    }
}

class deleteIPpool extends Request
{
    function deleteIPpool($ippool_name)
    {
	parent::Request("ippool.deleteIPpool",array("ippool_name"=>$ippool_name));
    }
}

class delIPfromPool extends Request
{
    function delIPfromPool($ippool_name,$ip)
    {
	parent::Request("ippool.delIPfromPool",array("ippool_name"=>$ippool_name
						     "ip"=>$ip));
    }
}

class addIPtoPool extends Request
{
    function addIPtoPool($ippool_name,$ip)
    {
	parent::Request("ippool.addIPtoPool",array("ippool_name"=>$ippool_name
						   "ip"=>$ip));
    }
}


?>