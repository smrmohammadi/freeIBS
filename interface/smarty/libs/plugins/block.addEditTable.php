<?php

function smarty_block_addEditTable($params,$content,&$smarty,&$repeat)
{
/*
    create header and footer of an Add Edit Style table
    parameter title(string,optional): Title of table that will be printed on top of table
    parameter table_width(string,optional): width of table, if not set, defaults are used
    parameter double(boolean,optional): Set Double table, double tables has two usable areas in 
			each row. Also Double TR s should be used for content

*/
    if(!is_null($content))
    {
	$title=isset($params["title"])?$params["title"]:"";
	if(isset($params["double"]) and $params["double"]=="TRUE")
	{
	    $table_width_default=480;
	    $colspans=9;
	}
	else
	{
	    $table_width_default=280;
	    $colspans=4;
	}

	$table_width=isset($params["table_width"])?$params["table_width"]:$table_width_default;

	$header=<<<END

<table class="Form_Main" width="{$table_width}" border="0" cellspacing="0" bordercolor="#000000" cellpadding="0">
	<tr>
		<td colspan="{$colspans}">
		<!-- Form Title Table -->
		<table border="0" cellspacing="0" cellpadding="0" class="Form_Title">
			<tr>
				<td class="Form_Title_Begin"><img border="0" src="/IBSng/images/begin_form_title_red.gif"></td>
				<td class="Form_Title">	{$title} <img border="0" src="/IBSng/images/arrow_orange.gif"></td>
				<td class="Form_Title_End"><img border="0" src="/IBSng/images/end_of_form_title_red.gif"></td>
			</tr>
			</table>
		<!-- End Form Title Table  -->
		</td>
	</tr>
	<tr>
		<td colspan="{$colspans}" class="Form_Content_Row_Space"></td>
	</tr>

END;
	$footer=<<<END
	
	<tr>
		<td colspan="{$colspans}">
			<table border="0" cellspacing="0" cellpadding="0" class="Form_Foot">
				<tr>
					<td class="Form_Foot_Begin_Line"></td>
					<td rowspan="2" class="Form_Foot_End"><img border="0" src="/IBSng/images/end_of_line_bottom_of_table.gif"></td>
					<td rowspan="2" class="Form_Foot_Buttons"><input type=image src="/IBSng/images/ok.gif"></td>
				</tr>
				<tr>
					<td class="Form_Foot_Below_Line"></td>
				</tr>
			</table>
			<!-- End Form Foot Table -->
		</td>
	</tr>
</table>
END;
    return $header.$content.$footer;    
    }
    
}
?>