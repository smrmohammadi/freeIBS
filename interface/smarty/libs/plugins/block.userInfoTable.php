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
<table class="Form_Main" width="370" border="0"  cellspacing="0" bordercolor="#000000" cellpadding="0">
	<tr>
		<td colspan="7">
		<!-- Title Table User_Info-->
		<table border="0" cellspacing="0" cellpadding="0" class="Form_Title">
			<tr>
				<td class="Form_Title_Begin" rowspan="2"><img border="0" src="/IBSng/images/begin_form_title_red.gif"></td>
				<td class="Form_Title_red" rowspan="2" style="width:175">{$title} <img border="0" src="/IBSng/images/arrow_orange.gif"></td>
				<td class="Form_Title_End" rowspan="2"><img border="0" src="/IBSng/images/end_of_list_title_red.gif"></td>
				<td class="Form_Title_Top_Line" align="right">Group Value <img border="0" src="/IBSng/images/arrow_orange_bg_white.gif"></td>
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
	<tr class="List_Foot_Line_red">
		<td colspan=25></td>
	</tr>
</table>
<br>
END;
    return $header.$content.$footer;    
    }
    
}
?>