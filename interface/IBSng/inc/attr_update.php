<?php
require_once("init.php");
require_once(IBSINC."group_face.php");
require_once(IBSINC."attrs.php");

function runUpdateMethod($update_method,&$update_helper)
{/*	All user plugin udpate function should be named "{$update_method}PluginUpdate"
	$update_method is set in smarty template and will be passed to this function.
	All update methods will get an $update_helper instance as their first argument. It must be 
	passed as refrence
	pluginUpdateTest(&$update_helper)
*/
    
    eval("{$update_method}PluginUpdate(\$update_helper);");
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
    

    function updateTargetAttrs($updated_attrs,$to_del_attrs,$return_after_send=TRUE)
    {/*
	
	$return_after_send(boolean): if set to TRUE, function will return after executation of request
					    and return array of ($success,$ret)
				     if set to FALSE, function will redirect client based on reponse 
					    of request.
    */
	if($this->target=="group")
	    list($success,$ret)=$this->updateGroupAttrs($this->target_id,$updated_attrs,$to_del_attrs);
	else if($this->target=="user")
	    {}

	if($return_after_send)
	    return array($success,$ret);
	else
	    $this->redirectBasedOnResponse($success,$ret);
    }
    
    function redirectBasedOnResponse($success,$ret)
    {
	if($success)
	    $this->redirectToTargetInfo();
	else
	    $this->showEditInterface($ret);

    }
    function updateGroupAttrs($group_name,$attrs,$to_del_attrs)
    {
	$update_grp_attrs=new UpdateGroupAttrs($group_name,$attrs,$to_del_attrs);
	list($success,$ret)=$update_grp_attrs->send();
	return array($success,$ret);
    }
    
    function redirectToTargetInfo()
    {/*	redirect to Target info, normally called when update was sucessful
    */
	if($this->target=="group")
	    redirectToGroupInfo($this->target_id);
    }
    
    function setPageError($err)
    {
	if(!is_null($err))
	    $this->smarty->set_page_error($err->getErrorMsgs());
    }
    
    function showEditInterface($err=null)
    {/* show target edit interface, normally called when update failed
	
    */
	$this->setPageError($err);
	if($this->target=="group")
	    intEditGroup($this->smarty,$this->target_id,$this->edit_tpl_name);

	exit();
    }
    
    function mustBeInRequest()
    {/* check if all needed arguments are in $_REQUEST array.
	if one of arguments aren't in $_REQUEST, show the interface again, with "INCOMPLETE REQUEST"
	error on top of page
    */
	$args=func_get_args();
	if(!call_user_func_array("isInRequest",$args))
	    $this->showEditInterface(error("INCOMPLETE_REQUEST"));
    }
    
    function getTargetAttrs()
    {
	if($this->target=="group")
	    return $this->getGroupAttrs($this->target_id);
    }
    
    function getGroupAttrs($group_name)
    {
	$group_info_req=new GetGroupInfo($group_name);
	list($success,$group_info)=$group_info_req->send();
	if($success)
	    return $group_info["attrs"];
	else
	    $this->showEditInterface($group_info);
    }
}


?>