<?php
require_once("init.php");
require_once("group.php");


function redirectToGroupList($msg="")
{
    redirect("/IBSng/admin/group/group_list.php?msg={$msg}");
}

function redirectToGroupInfo($group_name,$extra_param="")
{
    $redirect_str="/IBSng/admin/group/group_info.php?group_name={$group_name}";
    if($extra_param!="")
	$redirect_str.="&{$extra_param}";
    redirect($redirect_str);
}

function getGroupNames(&$smarty)
{ /* return number indexed(starting from 0... not group_id) array of group_names 
    on error an empty array is returned and a message is set in smart object
  */
    $group_names_req=new ListGroups();
    list($success,$groups)=$group_names_req->send();
    if($success)
	return $groups;
    else
    {
	$smarty->set_page_error($admins->getErrorMsgs());
	return array();
    }
}



?>