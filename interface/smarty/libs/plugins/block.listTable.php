<?php

function smarty_block_listTable($params,$content,&$smarty,&$repeat)
{
/*
    create header and footer of an List Style table
    parameter title(string,optional): Title of table that will be printed on top of table
    parameter cols_num(integer,required): number of table columns

*/
    if(!is_null($content))
    {
	$title=isset($params["title"])?$params["title"]:"";
	$header=<<<END
<table border="0"  class="List_Main" cellspacing="1" bordercolor="#FFFFFF" cellpadding="0">
	<tr>
		<td colspan="{$params["cols_num"]}" valign="bottom">
		<!-- List Title Table -->
		<table border="0" cellspacing="0" cellpadding="0" class="List_Title">
			<tr>
				<td class="List_Title_Begin" rowspan="2"><img border="0" src="/IBSng/images/begin_form_title_red.gif"></td>
				<td class="List_Title" rowspan="2"><nobr>{$title} <img border="0" src="/IBSng/images/arrow_orange.gif" width="10" height="10"></td>
				<td class="List_Title_End" rowspan="2"><img border="0" src="/IBSng/images/end_of_list_title_red.gif" width="5" height="20"></td>
				<td class="List_Title_Top_Line">&nbsp;</td>
			</tr>
			<tr>
				<td class="List_Title_End_Line"></td>
			</tr>
		</table>
		<!-- End List Title Table -->
		</td>
END;
	$footer=<<<END
	<!-- List Foot -->
	<tr class="List_Foot_Line">
		<td colspan=25></td>
	</tr>
	<!-- End List Foot-->
</table>
END;
    return $header.$content.$footer;    
    }
    
}
?>