<?php
require_once(IBSINC."menu.php");

function smarty_function_menuIcon($params,&$smarty)
{/*
*/
    $menu_selected=get1stLvlSelected($smarty->get_assigned_value("selected"));

}
?>