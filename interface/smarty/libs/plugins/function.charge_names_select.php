<?php
function smarty_function_charge_names_select($params,&$smarty)
{/* return string of html select code for charge selects.

    parameter name(string,required): html select name
    parameter default(string,optional): variable string that if exists in smarty object it will be set as 
					drop down default
    parameter type(string,optional): if set, only set this type of charge, should be either of "Internet" or "VoIP"

    parameter default_var(string,optional): see attrDefault comments
    parameter default_request(string,optional):
    parameter target(string,optional):
    
*/
    

    require_once($smarty->_get_plugin_filepath('function', 'html_options'));
    require_once(IBSINC."charge.php");
    $type=isset($params["type"])?$params["type"]:null;
    
    $charge_names=new ListCharges($type);
    list($success,$charge_names)=$charge_names->send();
    if(!$success)
	$charge_names=array();

    $selected=getSelectedAttrFromSmartyParams(&$smarty,&$params);
    
    return smarty_function_html_options(array("selected"=>$selected,"output"=>$charge_names,"values"=>$$charge_names,"name"=>$params["name"]),$smarty);
}
?>