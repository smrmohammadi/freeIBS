<?php
function smarty_function_relative_units($params,&$smarty)
{/* parameter name(string,required): html select name
    parameter default(string,optional): String that will be drop down default if set
    parameter id(string,optional): set optional dom ID
    
    parameter default_var(string,optional): see attrDefault comments
    parameter default_request(string,optional):
    parameter target(string,optional):
    
    return string of html select code for relative units.
*/

    require_once $smarty->_get_plugin_filepath('function', 'html_options');
    $rel_units=array("Hours","Days","Months","Years");
    $select_arr=array("selected"=>$default,"output"=>$rel_units,"values"=>$rel_units,"name"=>$params["name"]);
    if(isset($params["id"]))
	$select_arr["id"]=$params["id"];
    
    $selected="";
    if(isset($params["default"]))
	$selected=$params["default"];

    if(isset($params["default_var"]) and isset($params["default_request"]) and isset($params["target"]))
	$selected=attrDefault(getTargetAttrsFromSmarty($smarty,$params["target"]),
			      $params["default_var"],
			      $params["default_request"],
			      $selected);


    $select_arr["selected"]=$selected;
    return smarty_function_html_options($select_arr,$smarty);
}
?>