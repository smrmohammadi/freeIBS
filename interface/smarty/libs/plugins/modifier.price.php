<?php
function smarty_modifier_price($string)
{	/*
	    put , between each 3 digits, take care of 2 digits of floating point
	*/
	$price=(float)$string;
	$sign=$price<0?-1:1;
	$price*=$sign;
	$int_price=(int)$price;
	$float_part=round(($price-$int_price)*100);
	$str="";
	while($int_price>1000)
	{
	    $part=$int_price%1000;
	    $int_price=(int)($int_price/1000);
	    $str=",{$part}{$str}";
	}
	$str="{$int_price}{$str}";
	if($float_part>0)
	    $str.=".{$float_part}";
	if($sign==-1)
	    $str="-{$str}";
	return $str;
}
?>
