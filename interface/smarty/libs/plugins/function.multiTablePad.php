<?php
function smarty_function_multiTablePad($params,&$smarty)
{/*
    enter arbitary amount of multiTableTDs, until index%go_until==0
    parameter last_index(integer,required): last index of multiTableTDs
    parameter go_until(integer,required): go until last_index is dividable by this
*/
    require_once($smarty->_get_plugin_filepath('block', 'multiTableTD'));
    $ret="";
    while($params["last_index"]%$params["go_until"]!=$params["go_until"]-1)
    {
	$ret.=smarty_block_multiTableTD(array("type"=>"left"),"&nbsp;",$smarty);
	$ret.=smarty_block_multiTableTD(array("type"=>"right"),"&nbsp;",$smarty);
	$params["last_index"]++;
    }
    return $ret;
}



?>