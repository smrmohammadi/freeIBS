<?php
define("FLOAT_PRECISION",2);
function smarty_modifier_price($string)
{	/*
	    put , between each 3 digits, take care of 2 digits of floating point
	*/
	$price=(float)$string;
	$sign=$price<0?-1:1;
	$price*=$sign;
	$int_price=floor($price);
	$int_part="{$int_price}";
	$float_part=round(($price-$int_price)*pow(10,FLOAT_PRECISION));
	$str="";
	while(strlen($int_part)>3)
	{
	    $part=substr($int_part,strlen($int_part)-3,3);
	    $int_part=substr($int_part,0,strlen($int_part)-3);
	    $str=",{$part}{$str}";
	}
	$str="{$int_part}{$str}";
	if($float_part>0)
	    $str.=".".leftPadZero($float_part,FLOAT_PRECISION);
	if($sign==-1)
	    $str="-{$str}";
	return $str;
}

function leftPadZero($str,$len)
{
    $str="{$str}";
    while (strlen($str)<$len)
	$str="0".$str;
    return $str;
}

?>
