<?php
function smarty_function_relative_units($params,&$smarty)
{/* parameter name(string,required): html select name
    parameter default(string,optional): variable string that if exists in smarty object it will be set as 
					drop down default
    return string of html select code for relative units.
*/
    
    if(isset($params["default"]) and $smarty->is_assigned($params["default"]))
	$default=$smarty->get_assigned_value($params["default"]);
    else
	$default="";

    require_once $smarty->_get_plugin_filepath('function', 'html_options');
	
    $rel_units=array("Hours","Days","Months","Years");
    return smarty_function_html_options(array("selected"=>$default,"output"=>$rel_units,"values"=>$rel_units,"name"=>$params["name"]),$smarty);
}
?>