<?php

function smarty_block_listTD($params,$content,&$smarty,&$repeat)
{/*	Create an Add edit style column (TD).
	icon(boolean,optional): set style suitable for icon TDs
*/
    
    if(!is_null($content))
    {
	if(isset($params["icon"]) and $params["icon"]=="TRUE")
	    $style="List_col_Body_Icon";
	else
	    $style="list_col";
    

	return <<<END
    <td class="{$style}">{$content}</td>
END;

    }


}

?>