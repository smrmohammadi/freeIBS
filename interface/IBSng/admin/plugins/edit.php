<?php
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."attr_parser.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();

if(isInRequest("update","edit_tpl_name","target","target_id"))
    intUpdateAttrs($_REQUEST["group_name"],$_REQUEST["edit_tpl_name"]);

else if(isInRequest("group_name","edit_tpl_name"))
    intEditGroup($_REQUEST["group_name"],$_REQUEST["edit_tpl_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToGroupList($err->getErrorMsg());
}

function intUpdateAttrs(


function intEditGroup(&$smarty,$group_name,$edit_tpl_name)
{
    checkTplFileName($edit_tpl_name);
    editGroupAssignValues($smarty,$group_name,$edit_tpl_name);
    showEditGroupInterface($smarty);
}

function editGroupAssignValues(&$smarty,$group_name,$edit_tpl_name)
{
    intSetGroupInfo($smarty,$group_name);    
    $smarty->assign("edit_tpl_name",$edit_tpl_name);
    $smarty->assign("target","group");
    $smarty->assign("target_id",$group_name);
}

function showEditGroupInterface(&$smarty,$edit_tpl_name)
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

class UpdateAttrsHelper
{	
    function UpdateAttrsHelper(&$smarty,$target,$target_id,$edit_tpl_name)
    {
	$this->smarty=$smarty;
	$this->target=$target;
	$this->target_id=$target_id;
	$this->edit_tpl_name=$edit_tpl_name;
    }



}

?>