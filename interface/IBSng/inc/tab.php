<?php
require_once("init.php");

function fixTabName($name)
{
    return str_replace(" ", "_", $name);
}

function getTabTableID($new)
{
    global $tab_table_id;
    if(!isset($tab_table_id))
	$tab_table_id=0;
    if($new)
	$tab_table_id++;
    return "tab".$tab_table_id;
}
?>