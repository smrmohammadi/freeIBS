<?php
function smarty_function_group_names_select($params,&$smarty)
{/* parameter name(string,required): html select name
    parameter default(string,optional): variable string that if exists in smarty object it will be set as 
					drop down default
    return string of html select code for group selects.
*/
    
    if(isset($params["default"]) and $smarty->is_assigned($params["default"]))
	$default=$smarty->get_assigned_value($params["default"]);
    else
	$default="";

    require_once($smarty->_get_plugin_filepath('function', 'html_options'));
    require_once(IBSINC."group_face.php");
    $groups=getGroupNames($smarty);
    
    return smarty_function_html_options(array("selected"=>$default,"output"=>$groups,"values"=>$groups,"name"=>$params["name"]),$smarty);
}
?>