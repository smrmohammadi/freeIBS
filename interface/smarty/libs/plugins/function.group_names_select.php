<?php
function smarty_function_group_names_select($params,&$smarty)
{/* parameter name(string,required): html select name

    parameter default_var(string,optional): see getSelectedAttrFromSmartyParams comments
    parameter default_request(string,optional):
    parameter default_smarty(string,optional):
    parameter default(string,optional)
    parameter target(string,optional):

    return string of html select code for group selects.
*/
    
    $selected=getSelectedAttrFromSmartyParams($smarty,$params);

    require_once($smarty->_get_plugin_filepath('function', 'html_options'));
    require_once(IBSINC."group_face.php");
    $groups=getGroupNames($smarty);
    
    return smarty_function_html_options(array("selected"=>$selected,"output"=>$groups,"values"=>$groups,"name"=>$params["name"]),$smarty);
}
?>