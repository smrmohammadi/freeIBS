<?php
require_once("../../inc/init.php");
require_once(IBSINC."user.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."charge_face.php");
require_once(IBSINC."admin_face.php");



needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();

if(isInRequest("search"))
    intDoSearch($smarty);
else
    intShowUserSearch($smarty);
    
    
function intShowUserSearch(&$smarty)
{
    intShowUserSearchSetVars($smarty);
    $smarty->display("admin/user/search_user.tpl");
}


function intShowUserSearchSetVars(&$smarty)
{
    $smarty->assign_by_ref("group_names",getGroupNames($smarty));
    $smarty->assign_by_ref("admin_names",getAdminNames($smarty));
    intSetChargeNames($smarty,null);
}

?>