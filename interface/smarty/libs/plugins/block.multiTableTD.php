<?php

function smarty_block_multiTableTD($params,$content,&$smarty)
{/*	Create an Multi Style Table, TD
	parameter type(string,required): can be either of "left" or "right"
*/
    
    if(!is_null($content))
    {
	global $multi_table_color;
	if($params["type"]=="left")
	{
	    return <<<END

	<td class="Form_Content_Row_Begin"><img border="0" src="/IBSng/images/row/begin_of_row_{$multi_table_color}.gif"></td>
	<td class="Form_Content_multi_left">{$content}</td>
END;
	}
        else
	{
	    return <<<END

	<td class="Form_Content_multi_right">{$content}</td>
	<td class="Form_Content_Row_End"><img border="0" src="/IBSng/images/row/end_of_row_{$multi_table_color}.gif"></td>

END;
	}

    }
}

?>