<?php
/*
    variable target shows that which of "user" or "group" we're updating.
    variable target_id is either "group_name" or "user_id" based on target value

    each attribute edit template should have a has_attr check box, that shows if we should have this 
    attribute or not. if form submitted with has_attr not ticked, we'll try to delete all of relevant
    attributes from target. If has_attr was ticked then we'll try to update target attributes based
    on what's user input
*/
require_once("../../inc/init.php");
require_once(IBSINC."group.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."attr_parser.php");

$smarty=new IBSSmarty();
needAuthType(ADMIN_AUTH_TYPE);
if(isInRequest("target","target_id","template_name","update"))
    intUpdateAttrs($smarty,$_REQUEST["target"],$_REQUEST["target_id"],$_REQUEST["template_name"],$_REQUEST);
else if(isInRequest("target","target_id","template_name"))
    intEditAttrs($smarty,$_REQUEST["target"],$_REQUEST["target_id"],$_REQUEST["template_name"]);
else
{
    $smarty->set_page_error("Invalid Inputs!");
    interface($smarty);
}    

function intEditAttrs(&$smarty,$target,$target_id,$template_name,$assign_request=FALSE)
{ /*	$assign_request argument is used to assign $_REQUEST members to smarty,
	    this is useful if we have an error occured while updating attrs, and page showed with error message
  */
    if(intCheckTemplateName($smarty,$template_name))
    {
	$smarty->assign("template_file","plugins/{$template_name}.tpl");
	$smarty->assign("template_name",$template_name);
    }
    $smarty->assign("target",$target);
    $smarty->assign("target_id",$target_id);
    intSetTargetAttrs($smarty,$target,$target_id);
    if($assign_request)
	$smarty->assign_array($_REQUEST);
    interface($smarty);
}

function intUpdateAttrs(&$smarty,$target,$target_id,$template_name,&$request)
{
    $has_attr=isset($request["has_attr"]);
    $updated_attrs=intFindUpdatedAttrs($request);
    list($success,$attrs)=intGetTargetAttrs($target,$target_id);
    $to_update_attrs=array();
    $to_del_attrs=array();
    if($success)
    {
	$attrs=callAttrParsers($smarty,$attrs);
        if($has_attr)
	    $to_update_attrs=$updated_attrs;
    	else
	    foreach ($updated_attrs as $name=>$value)
		if (isset($attrs[$name]))
		    $to_del_attrs[$name]=$value;
    }
    else
	$smarty->set_page_error($attrs->getErrorMsgs());

    list($success,$err)=intSendTargetUpdate($target,$target_id,$to_update_attrs,$to_del_attrs);
    if($success)
	redirectToTargetInfo($target,$target_id);
    else
    {
	$smarty->set_page_error($err->getErrorMsgs());
	intEditAttrs($smarty,$target,$target_id,$template_name,TRUE);
    }
}

function intSendTargetUpdate($target,$target_id,&$to_update_attrs,&$to_del_attrs)
{
    if($target=="group")
	$update_attr_req=new UpdateGroupAttrs($target_id,$to_update_attrs,$to_del_attrs);
    else
	$update_attr_req=1;//XXX

    return $update_attr_req->send();
}


function intFindUpdatedAttrs(&$request)
{/*
    find attrs__X in request, and return a associative array of updated attrs
    value of each attr is it's value in request, or empty string if attr is not in request
*/
    $updated=array();
    foreach($request as $name=>$value)
	if(preg_match("/^attr__[0-9]+/",$name))
	    $updated[$value]=isset($request[$value])?$request[$value]:"";
    return $updated;
}



function intSetTargetAttrs(&$smarty,$target,$target_id)
{
    list($success,$attrs)=intGetTargetAttrs($target,$target_id);
    if($success)
    {
        $smarty->assign_array(callAttrParsers($smarty,$attrs));
	$smarty->assign("attrs",$attrs);
    }
    else
        $smarty->set_page_error($attrs->getErrorMsgs());
}


function intGetTargetAttrs($target,$target_id)
{
    if ($target=="group")
    {
	$group_info_req=new GetGroupInfo($target_id);
	list($success,$group_info)=$group_info_req->send();
	if($success)
	    return array(TRUE,$group_info["attrs"]);
	else
	    return array(FALSE,$group_info);
    }
    else if($target=="user")
    {
	//return user attributes here!
    }
    else
    {
	return array(FALSE,error("INVALID_INPUT"));
    }

    
}

function redirectToTargetInfo($target,$target_id)
{
    if ($target=="group")
	redirectToGroupInfo($target_id);
//    else
	
}

function intCheckTemplateName(&$smarty,$template_name)
{
    if(preg_match("/[^a-zA-Z0-9\_]/",$template_name))
    {
	$smarty->set_page_error("Invalid template name!");
	return False;
    }
    return True;
}

function interface(&$smarty)
{
    $smarty->display("admin/user/edit_attr.tpl");
}

?>