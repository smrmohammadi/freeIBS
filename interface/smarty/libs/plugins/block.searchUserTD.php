<?php
function smarty_block_searchUserTD($params,$content,&$smarty,&$repeat)
{/*
    parameter attr_name
    parameter user_id
    parameter attr_type(string,required): can be "attrs" or "basic"
*/

    if(is_null($content))
    {
	$user_attrs=getUserAttrs($smarty,$params["user_id"]);
	$val=getUserAttrValue($user_attrs,$params["attr_name"],$params["attr_type"]);
	$class="";
	if(is_null($val) and $params["attr_type"]=="attrs")
	{
	    $group_val=getGroupAttrValue($user_attrs,$params["attr_name"]);
	    if(!is_null($group_val))
	    {
		$class="Form_Content_Row_groupinfo_dark";
	        $val=$group_val;
	    }
	}
    
        if(is_null($val))
	{
	    $repeat=FALSE;
	    print "<td align=center>-------</td>";
	}
	else
	{
	    $smarty->assign("search_value",$val);
	    $smarty->assign("search_class",$class);
	}
    }
    else
    {
	$class=$smarty->get_assigned_value("search_class");
	if(trim($content)=="")
	    $content=$smarty->get_assigned_value("search_value");
	return <<<END
    	    <td class="{$class}" >{$content}</td>
END;
    }
}

function getUserAttrs(&$smarty,$user_id)
{
    $user_attrs=$smarty->get_assigned_value("user_infos");
    return $user_attrs[$user_id];
}

function getUserAttrValue(&$user_attrs,$attr_name,$attr_type)
{
    
    if($attr_type=="basic" and isset($user_attrs["basic_info"][$attr_name]))
	return $user_attrs["basic_info"][$attr_name];
    else if ($attr_type=="attrs" and isset($user_attrs["attrs"][$attr_name]))
	return $user_attrs["attrs"][$attr_name];
    else
	return null;
}

function getGroupAttrValue(&$user_attrs,$attr_name)
{
    $group_name=$user_attrs["basic_info"]["group_name"];
    list($success,$group_info)=getGroupInfoWithCache($group_name);
    if(!$success or !isset($group_info["attrs"][$attr_name]))
	return null;
    else
	return $group_info["attrs"][$attr_name];
}

?>