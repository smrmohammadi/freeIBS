<?php

function smarty_block_sortableHeader($params,$content,&$smarty,&$repeat)
{
/*
    Create a Sortable header, used for reports. this is done by making a new request link, with order_by and desc attribute 
    values changed.
    
    parameter name(string,required): name that will be present in order_by if our link clicked
    parameter default(string,optional): if set to TRUE and order_by is not present in request, we assume we're the default
					order by
    parameter default_desc(string,optional): defaultly! are we desc?
					

*/
    if(!is_null($content))
    {
	$request_url=$_SERVER["PHP_SELF"]."?".convertRequestToUrl(array("order_by","desc"));
	$ret="";
	$desc="&desc=1";
	if( isInRequest("order_by") and $_REQUEST["order_by"]==$params["name"] )
	{
	    $ret.=currentSortImage(isInRequest("desc"));
	    if(isInRequest("desc"))
		$desc="";
	}
	else if( !isInRequest("order_by") and isset($params["default"]) and $params["default"]=="TRUE" )
	{
	    $ret.=currentSortImage($params["default_desc"]=="TRUE");
	    if($params["default_desc"]=="TRUE")
		$desc="";
	}
	
	$ret.=<<<END
    <a class="Header_Top_links" href="{$request_url}&order_by={$params["name"]}{$desc}">
	{$content}
    </a>
END;
	return $ret;

    }
}

function currentSortImage($is_desc)
{
    if($is_desc)
	return "\/";
    else
	return "/\\";
}

?>