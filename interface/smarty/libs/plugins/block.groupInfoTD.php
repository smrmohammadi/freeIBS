<?php

function smarty_block_groupInfoTD($params,$content,&$smarty,&$repeat)
{/*	Create an Group Info style column. Also TR s are created when needed
	parameter comment(boolean,optional): if true, create a td suitable for comments, both
					    "left" and "right" tds should have this flag set
	parameter type("string",required): show td type, for 1 column table can be "left" and "right"
					   
*/
    
    if(!is_null($content))
    {
	if (isset($params["comment"]) and $params["comment"]=="TRUE")
	{
	    if($params["type"]=="left")
	    {
		$color=getTRColor(TRUE);
		$ret=<<<END
<tr>
		<!-- Form Text Area -->
		<td class="Form_Content_Row_Left_Textarea" valign="top" colspan="2">
		<table border="0" width="100%" cellspacing="0" cellpadding="0">
			<tr>
				<td class="Form_Content_Row_Begin"><img border="0" src="/IBSng/images/begin_of_row_{$color}.gif"></td>
				<td class="Form_Content_Row_Left_textarea_td_{$color}"><nobr>{$content}</nobr></td>
				<td class="Form_Content_Row_End"><img border="0" src="/IBSng/images/end_of_row_{$color}.gif"></td>
			</tr>
		</table>
		</td>
END;
	    } 
	    else //type is right
	    {
		$color=getTRColor();
		$ret=<<<END
		<td colspan="2" class="Form_Content_Row_Right_Textarea">
		<table border="0" width="100%" cellspacing="0" cellpadding="0" >
			<tr>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/top_left_of_comment_{$color}.gif"></td>
				<td class="Form_Content_Row_Top_textarea_line_{$color}"></td>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/top_right_of_comment_{$color}.gif"></td>
			</tr>
			<tr>
				<td class="Form_Content_Row_Left_textarea_line_{$color}">&nbsp;</td>
				<td class="Form_Content_Row_Right_textarea_td_{$color}">{$content}</td>
				<td class="Form_Content_Row_Right_textarea_line_{$color}">&nbsp;</td>
			</tr>
			<tr>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/bottom_left_of_comment_{$color}.gif"></td>
				<td class="Form_Content_Row_Bottom_textarea_line_{$color}">&nbsp;</td>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/bottom_right_of_comment_{$color}.gif"></td>
			</tr>
		</table>
		</td>
		<!-- End Form Text Area -->
		<tr>
		<td colspan="4" class="Form_Content_Row_Space"></td>
	</tr>
END;
    	    }
	
	
	}//end comment
	else //normal 1 row table
	{
	    if($params["type"]=="left")
	    {
		$color=getTRColor(TRUE);
		$ret=<<<END
	<tr>
		<td class="Form_Content_Row_Begin"><img border="0" src="/IBSng/images/begin_of_row_{$color}.gif"></td>
		<td class="Form_Content_Row_Left_{$color}"><nobr>{$content}</nobr></td>
END;
	    }
	    else //type is right
	    {
		$color=getTRColor();
		$ret=<<<END
		<td class="Form_Content_Row_Right_{$color}">{$content}</td>
		<td class="Form_Content_Row_End"><img border="0" src="/IBSng/images/end_of_row_{$color}.gif"></td>
	</tr>
	<tr>
		<td colspan="4" class="Form_Content_Row_Space"></td>
	</tr>
END;
    	    }
	}

	return $ret;
    }
    
}

