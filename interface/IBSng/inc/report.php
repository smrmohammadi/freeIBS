<?php
require_once("init.php");


class ReportHelper
{
    function ReportHelper()
    {
	$this->from=0;
	$this->to=30;
	$this->order_by="";
	$this->desc=True;
	$this->updateToRequest();
    }

    function getFrom()
    {
	return $this->from;
    }

    function getTo()
    {
	return $this->to;
    }

    function getOrderBy()
    {
	return $this->order_by;
    }

    function getDesc()
    {
	return $this->desc;
    }


    function updateToRequest()
    {
	$this->updateFromTo();
	$this->updateOrderBy();
    }
    
    function updateOrderBy()
    {
	if(isInRequest("order_by"))
	{
	    $this->order_by=$_REQUEST["order_by"];
	    $this->desc=isInRequest("desc");
	}
    }

    function updateFromTo()
    {
	if(isInRequest("page","rpp"))
	{
	    $page=(int)$_REQUEST["page"];
	    $rpp=(int)$_REQUEST["rpp"];
	    $from=($page-1)*$rpp;
	    $to=$page*$rpp;
	    if($this->checkFromTo($from,$to))
	    {
		$this->from=$from;
		$this->to=$to;
	    }
	}
    }

    function checkFromTo($from,$to)
    {
	if($from<0 or $from > $to or $to>1024*1024*50)
	{
	    toLog("Invalid Value for From/to: From {$from} To {$to}");
	    return False;    
	}
	return True;
    }
}

class ReportCollector
{
    function ReportCollector()
    {
	$this->conds=array();
    }

    function getConds()
    {
	return $this->conds;
    }

    function addToConds($name,$value)
    {/*
	add $name and $value to internal associative array
    */
	$this->conds[$name]=$value;
    }

    function __addFromRequest($request_key)
    {
	$this->addToConds($request_key,$_REQUEST[$request_key]);
    }

    function addToCondsFromRequest($not_empty=TRUE)
    {/*
	add request arguments to internal dic. request keys are passed as arguments and values are in request
	You can set how many arguments you want
	but arguments will be added to dic only if all of them exists.
	if $not_empty flag is set, they are checked not to be empty and will be added only when
	none of them was empty string
    */
	$arg_list=array_slice(func_get_args(),1);	
	foreach($arg_list as $arg)
	{
	    if (!isInRequest($arg))
		return;
	    if ($_REQUEST[$arg]=="")
		return;
	}
	foreach($arg_list as $arg)
	    $this->__addFromRequest($arg);
    }

    function addToCondsFromCheckBoxRequest($prefix,$cond_name)
    {/*	add check box conditions in internal dic. all checkboxes of same group should have a same prefix
	postfixed by an integer id. We find all values in request and set em in internet dic
    */
	$val_arr=array();
	foreach($_REQUEST as $name=>$val)
	    if(preg_match("/^{$prefix}[0-9]+/",$name))
		$val_arr[]=$val;
	    if (sizeof($val_arr)!=0)
		$this->addToConds($cond_name,$val_arr);
    }
}

class GetOnlineUsers extends Request
{
    function GetOnlineUsers($sort_by,$desc)
    {
	parent::Request("report.getOnlineUsers",array("sort_by"=>$sort_by,
						    "desc"=>$desc));
    }
}


?>