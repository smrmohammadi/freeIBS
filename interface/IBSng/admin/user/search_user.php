<?php
require_once("../../inc/init.php");
require_once(IBSINC."user.php");

needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();

if(isInRequest("search"))
    intDoSearch($smarty);
else
    intShowUserSearch($smarty);
    
    
function intShowUserSearch(&$smarty)
{
    intShowUserSearchSetVars($smarty);
    $smarty->display("admin/user/user_search.tpl");
}


function intShowUserSearchSetVars(&$smarty)
{
    $smarty->assign_by_ref("group_names",getGroupNames($smarty));
    $smarty->assign_by_ref("admin_names",getAdminNames($smarty));
    intSetChargeNames($smarty,null);

}

?>