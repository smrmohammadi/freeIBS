<?php
function smarty_function_multistr($params,&$smarty)
{/* 
    parameter form_name(string,required): name of form, multi string input text exists in
    parameter input_name(string,required): name of input text field

    return string, a linked image that will show dicomposed multi string
*/
    return <<<EOF
<a href="javascript:showMultiStr('{$params["form_name"]}','{$params["input_name"]}')" title="Show All Strings" style="text-decoration: none">
    <img src="/IBSng/images/icon/multistr_icon.gif" border=0>
</a>
EOF;
}
?>