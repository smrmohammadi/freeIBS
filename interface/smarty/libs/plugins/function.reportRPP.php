<?php
function smarty_function_reportRPP($params,&$smarty)
{/*return html select of Result Per Page selection
*/

    require_once $smarty->_get_plugin_filepath('function', 'html_options');
    $rpps=array(20,30,50,100,500,1000,2000);
    $select_arr=array("output"=>$rpps,"values"=>$rpps,"name"=>"rpp","selected"=>requestVal("rpp"));
    return smarty_function_html_options($select_arr,$smarty);
}
?>