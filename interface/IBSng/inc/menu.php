<?php
$IBSngMenu=Array("user"=>array(),
		"group"=>array(),
		"report"=>array(),
		"admin"=>array("list_admin"=>"/IBSng/admin/admins/admin_list.php"),
		"setting"=>array()
		);


$IBSngMenuLinks=Array("user"=>"/IBSng/admin/user",
		"group"=>"/IBSng/admin/group",
		"report"="/IBSng/admin/report",
		"admin"=>"/IBSng/admin/admin",
		"setting"="/IBSng/admin/setting"
		);


function get1stLvlLink($menu_name)
{/*
    return link of 1st level menu icon for "menu_name";
*/
    global $IBSngMenuLinks;
    return $IBSngMenuLinks[$menu_name];
}

function get1stLvlSelected($second_lvl_selected)
{/*	return 1st lvl selected tag based on second level selected
*/
    global $menu_selected;
    if(!isset($menu_selected))
	$menu_selected=find1stLvlSelected($second_lvl_selected);
    return $menu_selected;
}

function find1stLvlSelected($second_lvl_selected)
{/*	finds 1st lvl selected tag based on second level selected
*/
    global $IBSngMenu;
    foreach($IBSngMenu as $1st_lvl_name=>$2nd_lvl_arr)
	foreach($2nd_lvl_arr as $2nd_lvl_name=>$link)
	    if ($2nd_lvl_name == $second_lvl_selected)
		return $1st_lvl_name;
}

?>