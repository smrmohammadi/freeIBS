<?php
require_once("init.php");

class AddInterface extends Request
{
    function AddInterface($interface_name,$comment)
    {
	parent::Request("bw.addInterface",array("interface_name"=>$interface_name,
					    	    "comment"=>$comment));
    }
}

class AddNode extends Request
{
    function AddNode($interface_name,$parent_id,$limit_kbits)
    {
	parent::Request("bw.addNode",array("interface_name"=>$interface_name,
					   "parent_id"=>$parent_id,
					   "limit_kbits"=>$limit_kbits));
    }
}

class AddLeaf extends Request
{
    function AddLeaf($leaf_name,$parent_id,$default_limit_kbits,$total_limit_kbits)
    {
	parent::Request("bw.addLeaf",array("leaf_name"=>$leaf_name,
					   "parent_id"=>$parent_id,
					   "default_limit_kbits"=>$default_limit_kbits,
					   "total_limit_kbits"=>$total_limit_kbits));
    }
}

class AddLeafService extends Request
{
    function AddLeafService($leaf_name,$protocol,$filter,$limit_kbits)
    {
	parent::Request("bw.addLeafService",array("leaf_name"=>$leaf_name,
						  "protocol"=>$protocol,
						  "filter"=>$filter,
					          "limit_kbits"=>$limit_kbits));
    }
}

class GetInterfaces extends Request
{
    function getInterfaces()
    {
	parent::Request("bw.getInterfaces",array());
    }
}

class GetNodeInfo extends Request
{
    function getNodeInfo($node_id)
    {
	parent::Request("bw.getNodeInfo",array("node_id"=>$node_id));
    }
}

class GetLeafInfo extends Request
{
    function getLeafInfo($leaf_name)
    {
	parent::Request("bw.getLeafInfo",array("leaf_name"=>$leaf_name));
    }
}

class GetTree extends Request
{
    function getTree($interface_name)
    {
	parent::Request("bw.getTree",array("interface_name"=>$interface_name));
    }
}

class DelLeafService extends Request
{
    function DelLeafService($leaf_name,$leaf_service_id)
    {
	parent::Request("bw.delLeafService",array("leaf_name"=>$leaf_name,
						  "leaf_service_id"=>$leaf_service_id));
    }
}

class GetAllLeafNames extends Request
{
    function GetAllLeafNames()
    {
	parent::Request("bw.getAllLeafNames",array());
    }
}

class DelNode extends Request
{
    function DelNode($node_id)
    {
	parent::Request("bw.delNode",array("node_id"=>$node_id));
    }
}

class DelLeaf extends Request
{
    function DelLeaf($leaf_name)
    {
	parent::Request("bw.delLeaf",array("leaf_name"=>$leaf_name));
    }
}


class DelInterface extends Request
{
    function DelInterface($interface_name)
    {
	parent::Request("bw.delInterface",array("interface_name"=>$interface_name));
    }
}


?>