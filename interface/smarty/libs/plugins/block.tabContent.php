<?php

function smarty_block_tabContent($params,$content,&$smarty,&$repeat)
{
    require_once(IBSINC."tab.php");
/*
    create content of tabs
    parameter tab_name(string,required): name of tab title, that when it's selected, this content would be shown

*/
    if(!is_null($content))
    {
	$table_id=getTabTableID(FALSE);
	$tab_id=fixTabName($params["tab_name"]);
	return <<<END
	<div id="{$table_id}_{$tab_id}_content">
	    <table border="0" cellspacing="0" cellpadding="0" width="100%">
	    {$content}
	    </table>
	</div>
	<script>
		{$table_id}.initContent("{$table_id}_{$tab_id}");
	</script>
END;
    }
	
}


?>