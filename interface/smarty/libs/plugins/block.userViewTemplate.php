<?php

function smarty_block_userViewTemplate($params,$content,&$smarty,&$repeat)
{
/*
    return html codes that are necassary for SINGLE user view template start and ends
    parameter edit_tpl_name(string,required): tpl file name in plugins/edi/edit template directory.
*/
    if(!is_null($content))
    {
	$user_id=$smarty->get_assigned_value("user_id");
	$header=<<<END
<form method=POST action="/IBSng/admin/plugins/edit.php">
    <input type=hidden name="user_id" value="{$user_id}">
    <input type=hidden name="edit_tpl_name" value="{$params["edit_tpl_name"]}">
    <input type=hidden name="edit_user" value="1">
END;

	$footer=<<<END
</form>
END;
    return $header.$content.$footer;
    }    
}