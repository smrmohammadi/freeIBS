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
	    $from=(int)$_REQUEST["page"]*(int)$_REQUEST["rpp"];
	    $to=(int)$_REQUEST["page"]*((int)$_REQUEST["rpp"]+1);
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


