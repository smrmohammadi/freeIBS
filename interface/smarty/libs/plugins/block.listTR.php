<?php

function smarty_block_listTR($params,$content,&$smarty,&$repeat)
{/*	Create an Add edit style row(TR).
	parameter type(text,required): Can be either of "header" or "body"
				       "header" creates a header style TR and
				       "body" creates a body style TR
	parameter cycle_color(boolean,optional): if set to "TRUE", call getTRColor with true argument so new
						 color is generated, only should be used with "body" type

*/
    
    if(!is_null($content))
	if($params["type"]=="header")
	    return "<tr class=\"List_Head\">".$content."</tr>";
	else if ($params["type"]=="body")
	{
    	    $cycle_color=(isset($params["cycle_color"]) and $params["cycle_color"]=="TRUE")?True:False;
	    $color=getTRColor($cycle_color);
	    return "<tr class=\"List_Row_{$color}Color\">".$content."</tr>";
	}

}

?>