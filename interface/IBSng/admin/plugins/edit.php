<?php
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."perm.php");
require_once(IBSINC."attr_parser.php");
require_once(IBSINC."attr_update.php");

needAuthType(ADMIN_AUTH_TYPE);

$smarty=new IBSSmarty();

if(isInRequest("update","edit_tpl_cs","target","target_id"))
    intUpdateAttrs($smarty,$_REQUEST["target"],$_REQUEST["target_id"]);
else if(isInRequest("group_name","edit_group"))
    intEditGroup($smarty,$_REQUEST["group_name"]);
else if(isInRequest("user_id","edit_tpl_name","edit_user"))
    intEditUser($smarty,$_REQUEST["user_id"],$_REQUEST["edit_tpl_name"]);
else
{
    $err=new error("INVALID_INPUT");
    redirectToGroupList($err->getErrorMsg());
}

function intUpdateAttrs(&$smarty,$target,$target_id)
{
    $update_methods=getUpdateMethodsArray();
    $update_helper=new UpdateAttrsHelper($smarty,$target,$target_id);
    runUpdateMethod($update_methods,$update_helper);
    $update_helper->updateTargetAttrs(FALSE);
}


function intEditGroup(&$smarty,$group_name)
{
    $edit_templates=getEditTemplateArray();
    array_map("checkTplFileName",$edit_templates);
    $edit_template_files=array_map(create_function('$tpl_name','return "plugins/group/edit/".$tpl_name.".tpl";'),$edit_templates);
    editGroupAssignValues($smarty,$group_name,$edit_templates,$edit_template_files);
    showEditGroupInterface($smarty);
}


function editGroupAssignValues(&$smarty,$group_name,$edit_tpls,$edit_tpl_files)
{
    intSetGroupInfo($smarty,$group_name);    
    $smarty->assign("edit_tpl_files",$edit_tpl_files);
    $smarty->assign("edit_tpl_cs",join($edit_tpls,","));
    $smarty->assign("target","group");
    $smarty->assign("target_id",$group_name);
}

function showEditGroupInterface(&$smarty)
{
    $smarty->display("plugins/group/edit/skelton.tpl");
}

function intEditUser(&$smarty,$user_id,$edit_tpl_name)
{
    checkTplFileName($edit_tpl_name);
    editUserAssignValues($smarty,$group_name,$edit_tpl_name);
    showEditUserInterface($smarty,$edit_tpl_name);
}

function checkTplFileName($edit_tpl_name)
{
    if (!preg_match("/^[a-zA-Z0-9_]*$/",$edit_tpl_name))
    {
	print "Invalid Template Filename";
	exit();
    }
}

function getEditTemplateArray()
{/* 
    Find edit templates from request, and return template names in an array
*/
    if(isInRequest("edit_tpl_cs")) //we're runned from an update method
	return split("/,/",$_REQUEST["edit_tpl_cs"]);
    else
    {
	$edit_templates=array();    
	foreach($_REQUEST as $key=>$value)
	    if (preg_match("/^attr_edit_checkbox_[0-9]+$/",$key))
		$edit_templates[]=$value;
	return $edit_templates;
    }
}

function getUpdateMethodsArray()
{
    $update_methods=array();    
    foreach($_REQUEST as $key=>$value)
        if (preg_match("/^attr_update_method_[0-9]+$/",$key))
    	    $edit_templates[]=$value;
    return $edit_templates;
}

?>