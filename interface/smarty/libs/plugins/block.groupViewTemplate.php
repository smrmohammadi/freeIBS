<?php

function smarty_block_groupViewTemplate($params,$content,&$smarty,&$repeat)
{
/*
    return html codes that are necassary for group view template start and ends
    parameter edit_tpl_name(string,required): tpl file name in plugins/group/edit template directory.
*/
    if(!is_null($content))
    {
	$group_name=$smarty->get_assigned_value("group_name");
	$header=<<<END
<form method=POST action="/IBSng/admin/group/group_edit.php">
    <input type=hidden name="group_name" value="{$group_name}">
    <input type=hidden name="edit" value="{$params["edit_tpl_name"]}">
END;

	$footer=<<<END
</form>
END;
    return $header.$content.$footer;
    }    
}