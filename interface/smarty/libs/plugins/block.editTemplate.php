<?php

function smarty_block_editTemplate($params,$content,&$smarty,&$repeat)
{
/*
    return html codes that are necassary for attribute edit template starts and ends
    parameter target(string,required): target of template should be "group" or "user"
    parameter target_id(string,required): target unique id, should be group_name for group and user_id(s) for user
    parameter update_method(string,required): update method that will be called for updating the attribute
    parameter edit_tpl_name(string,required): name of edit template should be in plugins/group/edit for group
					      and plugins/user/edit for users
*/
    if(!is_null($content))
    {
	$header=<<<END
<script language="javascript" src="/IBSng/js/dom_container.js"></script>
<form method=POST action="/IBSng/admin/plugins/edit.php">
    <input type=hidden name="target" value="{$params["target"]}">
    <input type=hidden name="target_id" value="{$params["target_id"]}">
    <input type=hidden name="update_method" value="{$params["update_method"]}">
    <input type=hidden name="edit_tpl_name" value="{$params["edit_tpl_name"]}">
    <input type=hidden name="update" value="1">
END;

	$footer=<<<END
</form>
END;
    return $header.$content.$footer;
    }    
}