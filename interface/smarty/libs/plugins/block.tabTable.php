<?php

function smarty_block_tabTable($params,$content,&$smarty,&$repeat)
{
    require_once(IBSINC."tab.php");
/*
    create header and footer of an tab constructs
    parameter tabs(string,required): "," seperated list of tab ids. tab ids are used for labling tabs and also used for
				     dom ids, so they must be unique. They can contain white spaces 
    parameter content_height(integer,optional): set height of contents, if this value is small, you'll see tab goes
						up n down

    parameter action_icon(boolean,optional): Tells which icon to use for form submit
					     Can be on of "edit" "delete" "add" "load" "save" or "ok"
					     default is "ok"


*/
    if(!is_null($content))
    {
	$table_id=getTabTableID(FALSE);
	$buttons=createButtons($params["tabs"],$table_id);
	$height=isset($params["content_height"])?$params["content_height"]:200;
	return createTabTable($buttons,$content,$table_id,$height,$params["action_icon"]);
    }
    else
	$table_id=getTabTableID(TRUE);
	
}

function createButtons($tab_names,$table_id)
{
    $tab_arr=split(",",$tab_names);
    $tab_id=fixTabName($tab_arr[0]);
    $ret=<<<END
		<!-- Begin Button -->
		<td rowspan="2" class="Tab_Title_begin">
			<img border="0" src="/IBSng/images/tab/begin_of_tab_red.gif" width="8" height="20" id="{$table_id}_{$tab_id}_begin"></td>
		<td rowspan="2" class="Tab_Title_red" id="{$table_id}_{$tab_id}_td">{$tab_arr[0]}</td>
		<td rowspan="2" class="Tab_Title_end">
			<img border="0" src="/IBSng/images/tab/end_of_tab_red.gif" width="5" height="20" id="{$table_id}_{$tab_id}_end"></td>
	
		<!-- End Begin Button -->
		<script>
		    {$table_id}.addTab("{$table_id}_{$tab_id}");
		</script>
END;
    foreach (array_slice($tab_arr,1) as $tab_name)
    {
        $tab_id=fixTabName($tab_name);
	$ret.=<<<END
		<!-- mid button -->
		<td rowspan="2" class="Tab_Title_begin">
			<img border="0" src="/IBSng/images/tab/begin_of_tab_gray.gif" width="8" height="20" id="{$table_id}_{$tab_id}_begin"></td>
		<td  rowspan="2" class="Tab_Title_gray" id="{$table_id}_{$tab_id}_td">{$tab_name}</td>
		<td rowspan="2" class="Tab_Title_end">
			<img border="0" src="/IBSng/images/tab/end_of_tab_gray.gif" width="5" height="20" id="{$table_id}_{$tab_id}_end"></td>
		<!--end mid button -->
		<script>
		    {$table_id}.addTab("{$table_id}_{$tab_id}");
		</script>

END;
    }
    return $ret;
}

function createTabTable($buttons,$content,$table_id,$height,$action_icon)
{
	return <<<END
<script>
    {$table_id}=new Tab();
</script>

<table border="0" cellspacing="0" cellpadding="0" width="430" valign="top">
	<tr><td>
	    <table border="0" cellspacing="0" cellpadding="0" width="100%" valign="top">
		{$buttons}
		<td class="Tab_Title_Top_Line"></td></tr>	
		<tr>
		<td class="Tab_Title_End_Line"></td></tr>
		</table>
	</td></tr>
	<tr>
		<td  height=1></td>
	</tr>
	<tr>
		<td  height={$height} valign=top bgcolor="#efefef" width="100%">
		    {$content}
		</td>
	</tr>

	<tr>
		<td>
			<table border="0" cellspacing="0" cellpadding="0" class="Form_Foot">
				<tr>
					<td class="Form_Foot_Begin_Line_red"></td>
					<td rowspan="2" class="Form_Foot_End"><img border="0" src="/IBSng/images/list/end_of_line_bottom_of_table.gif"></td>
					<td rowspan="2" class="Form_Foot_Buttons"><input type=image src="/IBSng/images/icon/{$action_icon}.gif"></td>
				</tr>
				<tr>
					<td class="Form_Foot_Below_Line_red"></td>
				</tr>
			</table>
			<!-- End Form Foot Table -->
		</td>
	</tr>
</table>
END;
}

?>