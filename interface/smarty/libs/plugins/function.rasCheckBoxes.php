<?php

function smarty_function_rasCheckBoxes($params,&$smarty)
{/*
*/
    require_once(IBSINC."ras.php");
    require_once($smarty->_get_plugin_filepath('block','multiTable'));
    require_once($smarty->_get_plugin_filepath('block','multiTableTD'));
    require_once($smarty->_get_plugin_filepath('function','multiTableTR'));
    require_once($smarty->_get_plugin_filepath('function','multiTablePad'));



    $ras_table=createRasTable($smarty,$params["prefix"]);
    return createShowHideTable($smarty,$params["prefix"],$ras_table);
}

function createRasTable(&$smarty,$prefix)
{
    $req=new GetActiveRasIPs();
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
    {
	$content="";
	$i=0;
	foreach($resp->getResult() as $ras_ip)
	{
	    if($i%4==0)
		$content.=smarty_function_multiTableTR(array(),$smarty);
	    $checked=checkBoxValue("{$prefix}_{$i}");
	    $content.=smarty_block_multiTableTD(array("type"=>"left","width"=>"25%"),"<input type=checkbox name='{$prefix}_{$i}' value='{$ras_ip}' {$checked}>",$smarty);
	    $content.=smarty_block_multiTableTD(array("type"=>"right","width"=>"25%"),"{$ras_ip}",$smarty);
	    $i++;
	}
	$content.=smarty_function_multiTablePad(array("last_index"=>$i-1,"go_until"=>4,"width"=>"25%"),$smarty);
	$content=smarty_block_multiTable(array(),$content,$smarty);
    }
    else
    {
	$err=$resp->getError();
	$content=$err->getErrorMsg();
    }
    return $content;    
}

function createShowHideTable(&$smarty,$prefix,$rases_content)
{
    $content= <<<END
<table width=100%>
    <tr>
      <td>
	<a href="#" onClick="{$prefix}_container.toggle('{$prefix}_select_ras'); return false;"><font size=1>Show/Hide Rases</font></a>
      </td>
    </tr>
    <tr id="{$prefix}_select_ras">
	<td>
	    {$rases_content}
	</td>
    </tr>
</table>
<script>
    {$prefix}_container=new DomContainer();
    {$prefix}_container.setOnSelect("display","");
    {$prefix}_container.setOnUnSelect("display","none");

    {$prefix}_container.addByID("{$prefix}_select_ras");

    {$prefix}_container.select(null);
</script>

END;
    return $content;
}

?>