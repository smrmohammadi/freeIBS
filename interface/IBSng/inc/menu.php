<?php
$GLOBALS["IBSngMenu"]=Array("user"=>array(),
		"group"=>array("Group List"=>"/IBSng/admin/group/group_list.php",
			       "Add Group"=>"/IBSng/admin/group/add_new_group.php"),
		"report"=>array(),
		"admin"=>array("Admin List"=>"/IBSng/admin/admins/admin_list.php",
			       "Add Admin"=>"/IBSng/admin/admins/add_new_admin.php"),
		"setting"=>array("Charge"=>"/IBSng/admin/charge/charge_list.php",
				"RAS"=>"/IBSng/admin/ras/ras_list.php",
				"IPPool"=>"/IBSng/admin/ippool/ippool_list.php",
				"Advanced Configuration"=>"/IBSng/admin/misc/show_ibs_defs.php"),
		"home"=>array("Admin Home"=>"/IBSng/admin/admin_index.php"),		       
		);

$GLOBALS["IBSngMenuLinks"]=Array("user"=>"/IBSng/admin/user",
		      "group"=>"/IBSng/admin/group",
		      "report"=>"/IBSng/admin/report",
		      "admin"=>"/IBSng/admin/admins",
	    	      "setting"=>"/IBSng/admin/setting",
		      "home"=>"/IBSng/admin/admin_index.php"
		      );


function get1stLvlLink($menu_name)
{/*
    return link of 1st level menu icon for "menu_name";
*/
    global $IBSngMenuLinks;
    return $IBSngMenuLinks[$menu_name];
}

function get1stLvlSelected($second_lvl_selected)
{/*	return 1st level selected tag based on second level selected
*/
    global $menu_selected;
    if(!isset($menu_selected))
	$menu_selected=find1stLvlSelected($second_lvl_selected);
    return $menu_selected;
}

function find1stLvlSelected($second_lvl_selected)
{/*	finds 1st level selected tag based on second level selected
*/
    global $IBSngMenu;
    foreach($IBSngMenu as $first_lvl_name=>$second_lvl_arr)
	foreach($second_lvl_arr as $second_lvl_name=>$link)
	    if ($second_lvl_name == $second_lvl_selected)
		return $first_lvl_name;
}

function get2ndLvlMenu($first_lvl_name)
{/* return second level menu array from first level selected */
    global $IBSngMenu;
    return $IBSngMenu[$first_lvl_name];
}

?>