<?php

function smarty_function_requestToUrl($params,&$smarty)
{/*
    Convert Request to url, return the url string
    parameter ignore(str,optional): ignore this key in request
    
*/
    $ignore_arr=array();
    if(isset($params["ignore"]))
	$ignore_arr[]=$params["ignore"];
    return $_SERVER["PHP_SELF"]."?".convertRequestToUrl();
}



?>