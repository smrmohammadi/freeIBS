<?php

function smarty_block_attrTableFoot($params,$content,&$smarty,&$repeat)
{
/*
    create a footer table suitable for attribute pages footers
    parameter action_icon(string,required): action icon can be "edit" "delete" "add" or "ok"
    parameter table_width(string,optional): width of table, if not set, defaults are used
    parameter color(string,optional): Set color of table header, default is red

*/
    if(!is_null($content))
    {
	$table_width=380;
	$color="red";
	$action_icon="ok";

	if(isset($params["table_width"]))
	    $table_width=$params["table_width"];

	if(isset($params["color"]))
	    $color=$params["color"];

	if(isset($params["action_icon"]) and in_array($params["action_icon"],array("edit","delete","add","ok")))
	    $action_icon=$params["action_icon"];

	$header=<<<END
<table border="0" cellspacing="0" cellpadding="0" class="Form_Foot" style="width:{$table_width}">
	<tr>
		<td class="Form_Foot_Begin_Line_{$color}"></td>
		<td rowspan="2" class="Form_Foot_End"><img border="0" src="/IBSng/images/list/end_of_line_bottom_of_table.gif"></td>
		<td rowspan="2" class="Form_Foot_Buttons"><input type=image src="/IBSng/images/icon/{$action_icon}.gif"></td>
	</tr>
	<tr>
		<td class="Form_Foot_Below_Line_{$color}">


END;
	$footer=<<<END
</td>
	</tr>
</table>
END;
    return $header.$content.$footer;    
    }
    
}
?>