<?php
function smarty_function_admin_names_select($params,&$smarty)
{/* parameter name(string,required): html select name
    parameter default(string,optional): variable string that if exists in smarty object it will be set as 
					drop down default
    parameter default_request(string,optional): variable string that if exists in request it will be set as 
					drop down default
    return string of html select code for admin names select.
*/
    
    if (isset($params["default_request"]) and isset($_REQUEST[$params["default_request"]]))
	$default=$_REQUEST[$params["default_request"]];
    else if(isset($params["default"]) and $smarty->is_assigned($params["default"]))
	$default=$smarty->get_assigned_value($params["default"]);
    else
	$default="";

    require_once($smarty->_get_plugin_filepath('function', 'html_options'));
    require_once(IBSINC."admin_face.php");
    $admins=getAdminNames($smarty);
    
    return smarty_function_html_options(array("selected"=>$default,"output"=>$admins,"values"=>$admins,"name"=>$params["name"]),$smarty);
}
?>