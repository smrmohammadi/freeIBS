<?php
function smarty_function_reportToShowCheckBox($params,&$smarty)
{/*
    create and return html code for checkboxes used in report forms, to tell which attribute should be shown in
	retport
    param name(string,required): name of checkbox that will be set
    param output(string,required): string that will be shown aside of checkbox
    param default_checked(string,optional): default to false, see function.checkBoxValue
    param always_in_request(string,optional): see function.checkBoxValue

*/
    require_once($smarty->_get_plugin_filepath('function', 'checkBoxValue'));
    $checked=smarty_function_checkBoxValue($params,$smarty);
    return <<<END
    <input type=checkbox name={$params["name"]} {$checked}}> 
    {$params["output"]}
END;
}

?>