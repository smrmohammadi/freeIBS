<?php

function smarty_block_userInfoTable($params,$content,&$smarty,&$repeat)
{
/*
    create header and footer of an User info Style table
    parameter title(string,optional): Title of table that will be printed on top of table


*/
    if(!is_null($content))
    {
	$title=isset($params["title"])?$params["title"]:"";
	$header=<<<END
<table class="Form_Main" width="280" border="0"  cellspacing="0" bordercolor="#000000" cellpadding="0">
	<tr>
		<td colspan="7">
		<!-- Title Table User_Info-->
		<table border="0" cellspacing="0" cellpadding="0" class="Form_Title">
			<tr>
				<td class="Form_Title_Begin" rowspan="2"><img border="0" src="begin_form_title_red.gif"></td>
				<td class="Form_Title" rowspan="2">{$title} <img border="0" src="arrow_orange.gif"></td>
				<td class="Form_Title_End" rowspan="2"><img border="0" src="end_of_list_title_red.gif"></td>
				<td class="Form_Title_Top_Line" align="right">Group Info<img border="0" src="arrow_orange_bg_white.gif"></td>
			</tr>
			<tr>
				<td class="Form_Title_End_Line"></td>
			</tr>
		</table>
		<!-- End Title Table  -->
		</td>
	</tr>
	<tr>
		<td colspan="7" class="Form_Content_Row_Space"></td>
	</tr>

END;
	$footer=<<<END
	<tr>
		<td colspan="7">
			<!-- Foot Table -->
			<table border="0" cellspacing="0" cellpadding="0" class="Form_Foot">
				<tr>
					<td class="Form_Foot_Begin_Line"></td>
					<td rowspan="2" class="Form_Foot_End"><img border="0" src="end_of_line_bottom_of_table.gif"></td>
					<td rowspan="2" class="Form_Foot_Buttons">
					<img border="0" src="edit.gif" width="45" height="20"></td>
				</tr>
				<tr>
					<td class="Form_Foot_Below_Line"></td>
				</tr>
			</table>
			<!-- End Foot Table -->
		</td>
	</tr>
</table>
END;
    return $header.$content.$footer;    
    }
    
}
?>