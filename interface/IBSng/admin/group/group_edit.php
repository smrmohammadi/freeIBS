<?php
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."attr_parser.php");

needAuthType(ADMIN_AUTH_TYPE);

if(isInRequest("group_name","edit_tpl_name"))
    intEditGroup($_REQUEST["group_name"],$_REQUEST["edit_tpl_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToGroupList($err->getErrorMsg());
}

function intGroupInfo($group_name,$edit_tpl_name)
{
    $smarty=new IBSSmarty();
    checkTplFileName($edit_tpl_name);
    intSetGroupInfo($smarty,$group_name);    
    interface($smarty);
}

function interface(&$smarty,$edit_tpl_name)
{
    $smarty->display($edit_tpl_name);
}

function checkTplFileName($edit_tpl_name)
{
    if (!preg_match("/[a-zA-Z0-9]*\.tpl/",$edit_tpl_name))
    {
	print "Invalid Template Filename";
	exit();
    }
}

?>