<?php
function smarty_function_listTableHeaderIcon($params,&$smarty)
{/*     return a string, an image that will show the action text
	parameter action(string,required): action that will be showed in header
					   options: "add","delete","edit","view"
	parameter close_tr(boolean,optional): optionally add an </tr> at the end. Useful when 
					      it's the last icon in row

*/
    
    $action=$params["action"];
    $close_tr=(isset($params["close_tr"]) and $params["close_tr"]=="TRUE")?"</tr>":"";
    $link="/IBSng/images/list_header_";
    if($action=="add")
	$link.="add.gif";
    else if ($action=="delete")
	$link.="delete.gif";
    else if ($action=="edit")
	$link.="edit.gif";
    else if ($action=="view")
	$link.="view.gif";
    	
    return <<<EOF
                <td Rowspan=2 class="List_Title_Icon" >
		    <img border="0" src="{$link}">
		</td>	
	    {$close_tr}
EOF;
}
?>