<?php
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."attr_parser.php");
require_once(IBSINC."attr_update.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();

if(isInRequest("update","edit_tpl_name","target","target_id","update_method"))
    intUpdateAttrs($smarty,$_REQUEST["edit_tpl_name"],$_REQUEST["target"],$_REQUEST["target_id"],$_REQUEST["update_method"]);
else if(isInRequest("group_name","edit_tpl_name","edit_group"))
    intEditGroup($smarty,$_REQUEST["group_name"],$_REQUEST["edit_tpl_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToGroupList($err->getErrorMsg());
}

function intUpdateAttrs(&$smarty,$edit_tpl_name,$target,$target_id,$update_method)
{
    $update_helper=new UpdateAttrsHelper($smarty,$target,$target_id,$edit_tpl_name);
    runUpdateMethod($update_method,$update_helper);
    $update_helper->updateTargetAttrs(FALSE);
}


function intEditGroup(&$smarty,$group_name,$edit_tpl_name)
{
    checkTplFileName($edit_tpl_name);
    editGroupAssignValues($smarty,$group_name,$edit_tpl_name);
    showEditGroupInterface($smarty,$edit_tpl_name);
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
    $smarty->display("plugins/group/edit/{$edit_tpl_name}");
}

function checkTplFileName($edit_tpl_name)
{
    if (!preg_match("/^[a-zA-Z0-9_]*\.tpl$/",$edit_tpl_name))
    {
	print "Invalid Template Filename";
	exit();
    }
}


?>