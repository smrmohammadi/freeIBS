<?php

class MultiStrGetAll extends Request
{
    function MultiStrGetAll($str)
    {
	parent::Request("util.multiStrGetAll",array("str"=>$str));
    }
}

function getAllMultiStrs($str)
{
    $req=new MultiStrGelAll($str);
    list($success,$str_arr)=$req->send();
    if($success)
	return $str_arr;
    return FALSE;
}
    
function isMultiString($str)
{
    return preg_match("/,|{[0-9]+-[0-9]+}/",$str);
}

function getFirstOfMultiStr($str)
{
    $str_arr=getAllMultiStrs($str);
    if($str_arr===FALSE)
	return FALSE;
    else
	return $str_arr[0];
}

?>