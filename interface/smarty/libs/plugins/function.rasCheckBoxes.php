<?php
function smarty_function_rasCheckBoxes($params,&$smarty)
{/*
*/
    require_once(IBSINC."ras.php");
    $ras_table=createRasTable($params["prefix"]);
    return createShowHideTable($params["prefix"],$ras_table);
}

function createRasTable($prefix)
{
    $req=new GetActiveRasIPs();
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
    {
	$content="<table><tr>";
	$i=0;
	foreach($resp->getResult() as $ras_ip)
	{
	    if($i!=0 and $i%3==0)
		$content.="</tr><tr>";
	    $checked=checkBoxValue("{$prefix}_{$i}");
	    $content.="<td><input type=checkbox name='{$prefix}_{$i}' value='{$ras_ip}' {$checked}> {$ras_ip}</td>";
	    $i++;
	}
	$content.="</table>";
    }
    else
	$content=$resp->getError();
    return $content;    
}

function createShowHideTable($prefix,$rases_content)
{
    return <<<END
<table>
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
}

?>