<?php
function smarty_modifier_price($string)
{
	$price=(int)$string;
	$neg = false;
	if($price < 0){
	    $price = -$price;
	    $neg = true;
	}
	$str="{$price}";
	$len=strlen($str);
	$priceString="";
	for($i=$len;$i>0;$i-=3)
	{
		$temp=$priceString;
		if($i-3>0)
		{
			$start=$i-3;
			$len=3;
		}
		else
		{
			$start=0;
			$len=$i;
		}
		
		$priceString=substr($str,$start,$len);
		$priceString.=",{$temp}";
	}
	$priceString=substr($priceString,0,strlen($priceString)-1);
	if($neg)
	    $priceString = "-" . $priceString;
	return $priceString;
}
?>
