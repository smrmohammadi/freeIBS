<?php

function smarty_block_addEditTD($params,$content,&$smarty,&$repeat)
{/*	Create an Add edit style column. Also TR s are created when needed
	parameter double(boolean,optional): if true, create a td suitable for double column tables
					    all of "left1" "left2" "right1" "right2" td s should have
					    this flag set
	parameter comment(boolean,optional): if true, create a td suitable for comments, both
					    "left" and "right" tds should have this flag set
	parameter type("string",required): show td type, for 1 column table can be "left" and "right"
					   and for 2 column tables can be "left1" "right1" "left2" "right2"
*/
    
    if(!is_null($content))
    {
	$err_star_img_link="<img src='/IBSng/images/error.gif'> ";
	if (isset($params["err"]) and $smarty->is_assigned($params["err"]) and $smarty->get_assigned_value($params["err"])==TRUE)
        {
	    $err_star=$err_star_img_link;
	    $err=True;
	}
        else
	{
	    $err_star="";
	    $err=False;
        }

	if(isset($params["double"])and $params["double"]=="TRUE")
	{
	    if($params["type"]=="left1")
	    {
	    	$color=getTRColor(TRUE);
		$ret=<<<END
	<tr>
		<td class="Form_Content_Row_Begin">	<img border="0" src="/IBSng/images/begin_of_row_{$color}.gif"></td>
		<td class="Form_Content_Row_Left_2col_{$color}" >{$content}</td>
END;
	    }
	    else if ($params["type"]=="right1")
	    {
	    	$color=getTRColor();
		$ret=<<<END
		<td class="Form_Content_Row_Right_2col_{$color}">{$content}</td>
		<td class="Form_Content_Row_End"><img border="0" src="/IBSng/images/end_of_row_{$color}.gif"></td>
END;
	    }
	    else if($params["type"]=="left2")
	    {
	    	$color=getTRColor();
		$ret=<<<END
		<td class="Form_Content_Col_Space">&nbsp;</td>
		
		<td class="Form_Content_Row_Begin"><img border="0" src="/IBSng/images/begin_of_row_{$color}.gif"></td>
		<td class="Form_Content_Row_Left_2col_{$color}" >{$content}</td>
END;
	    }
	    else if ($params["type"]=="right2")
	    {
	    	$color=getTRColor();
		$ret=<<<END
		<td class="Form_Content_Row_Right_2col_{$color}">{$content}</td>
		<td class="Form_Content_Row_End"><img border="0" src="/IBSng/images/end_of_row_{$color}.gif"></td>
		
	</tr>
END;
	    }
	    
	} //end double
	else if (isset($params["comment"]) and $params["comment"]=="TRUE")
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
		<td class="Form_Content_Row_Left_{$color}">{$err_star}<nobr>{$content}</nobr></td>
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

