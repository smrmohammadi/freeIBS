<?php

function smarty_block_headerMsg($params,$content,&$smarty,&$repeat)
{
/*
    used for messages on header of files, usually when some actions was done, and we want to inform user
    parameter var_name(string,required): smarty variable name that if has been set to True, 
	    the message will be shown

*/
    if(!is_null($content))
    {

	return <<<END
    <span class="message">
	{$content}
    </span>        
	
END;
    }
    else
    {
	$var_name=$params["var_name"];
    	if(!($smarty->is_assigned($var_name) and $smarty->get_assigned_value($var_name)))
	    $repeat=False;
    }
}
?>