<?php
function getClientIPAddress()
{/* return client ip address */
    return $_SERVER["REMOTE_ADDR"];
}

function redirect($url)
{/* redirect user to $url
    NOTE: this must be done before sending headers
 */
    header("Status: 302 moved");
    header("Location: {$url}");
    exit();
}

function isInRequest()
{/* This function has variable length arguments
    It checks if all of arguments is available in REQUEST, if so, return TRUE
    else return FALSE
*/
    $arg_list=func_get_args();
    foreach($arg_list as $arg)
	if(!isset($_REQUEST[$arg]))
	    return FALSE;
    return TRUE;
    
}

function requestVal($key,$default="")
{/* return value of $key in request, if it's not available in request return $default 
 */
    if (isInRequest($key))
	return $_REQUEST[$key];
    else
	return $default;

}

function requestValWithDefaultArr($key,$default_arr,$default="")
{/*
    return value of $key in request, if it's not available in request, it will check $default_arr and return
    if it has key $key, if not, return $default
*/
    if (isInRequest($key))
	return $_REQUEST[$key];
    else if (isset($default_arr[$key]))
	return $default_arr[$key];
    else
	return $default;
    
}


function str_trim($str,$max_size)
{ /*trim $str to $max_size trying to end trimmed string with a complete word 
    Also put ... after str, if it were trimmed    
  */
  if ($max_size>=strlen($str))
    return $str;

  preg_match("/^(.{".$max_size."}[^\s\t\n]{0,100}).*/s",$str,$matches);

  return $matches[1]." ...";
}

function checkPasswordMatch($password1,$password2)
{
    if($password1!=$password2)
	return array(FALSE,new Error("PASSWORDS_NOT_MATCH|Passwords don't match"));
    else
	return array(TRUE,"");
}

function checkBoxValue($name,$default="",$if_not_exists="")
{
/*
    return value for a check box, return string is "" (empty string) or "selected" that can be 
    put into input box
    $name(string): name of check box in request
    $default(string): default value, if check box is not in request, default value is returned
    $if_not_exists(string): if this parameter isn't an empty string, it will checked against the request
	and return "checked" if it isn't in request. This is useful when you want a check box , to be checked
	by default when page is first showed, and relay on $name and $default afterwards

*/
    if(array_key_exists($name,$_REQUEST))
	return "checked";
    if($if_not_exists!=="")
	if(array_key_exists($if_not_exists,$_REQUEST))
	    return "checked";
	else 
	    return "";
    return $default;
}

function escapeIP($ip)
{/*
    escape ip address so it can be used in form names
*/
    return preg_replace("/[.]/","!",$ip);
}

function unEscapeIP($ip)
{/*
    unEscape ip that is used in form names
*/
    return preg_replace("/\!/",".",$ip);
}


function getTRColor($swap=FALSE)
{/*
    get TR color, Used in smarty plugins
    TR colors are either "light" or "dark"
    argument $swap tells if color needs to be swapped and we need a new color, normally this
    is done for new TR
*/
    global $tr_last_color;
    if(!isset($tr_last_color))
	$tr_last_color="light";
    else if($swap)
    {
	if($tr_last_color=="light")
	    $tr_last_color="dark";
	else
	    $tr_last_color="light";
    }
    return $tr_last_color;
}


function attrDefault($target_attrs,$default_var,$default_request,$default="")
{/*
    return attribute default value, see attrDefault smarty plugin function for info about argumentes
*/
    if(isset($_REQUEST[$default_request]))
	return $_REQUEST[$default_request];

    else if (isset($target_attrs[$default_var]) and !is_null($target_attrs[$default_var]))
	return $target_attrs[$default_var];
    else
	return $default;
}

function getTargetAttrsFromSmarty(&$smarty,$target)
{
    if($target=="user")
	$target_attrs=$smarty->get_assigned_value("user_attrs");
    else if ($target=="group")
	$target_attrs=$smarty->get_assigned_value("group_attrs");
    else if ($target=="user_info")
	$target_attrs=$smarty->get_assigned_value("user_info");
    
    return $target_attrs;
}

function getSelectedAttrFromSmartyParams(&$smarty,&$params)
{/* Get selected value of an attr, from smarty object and smarty params.
    This function is useful for smarty plugins that needs to get what is value of selected

    param default_request(string,optional): name of request key, that if has been set, will be returned as
					    default, request is always prefered over other methods

    param target(string,optional): attribute target, should be "user" or "group" that attribute default
				    would be seek in it

    param default_var(string,optional): name of target attribute, that if has been set, will be returned as
					    default, this is preffered after default_request
					    target attributes are searched through target array as set it target parameter


    param default_smarty(string,optional): name of smarty variable that if has been set will be set after above 
					    conditions failed

    param default(string,optional): optional string that will be returned if none of other default values matched
*/
    if(isset($params["default_var"]) and isset($params["default_request"]) and isset($params["target"]))
	$selected=attrDefault(getTargetAttrsFromSmarty($smarty,$params["target"]),
			      $params["default_var"],
			      $params["default_request"],
			      $selected);
    else if (isset($params["default_request"]) and isInRequest($params["default_request"]))
	$selected=$_REQUEST[$params["default_request"]];
    else if(isset($params["default_smarty"]) and $smarty->is_assigned($params["default_smarty"]))
	$selected=$smarty->get_assigned_value($params["default_smarty"]);
    else if(isset($params["default"]))
	$selected=$params["default"];
    else
	$selected="";

    return $selected;
}



################################## NOT USED ###################
function calcRelativeDateFromHours($rel_date)
{/*
    calculate relative date unit from an hour unir relative date, this is useful to show cleaner output
    ex. 1 days is more clear that 24 hours
    return an array of ($rel_date,$rel_date_unit)
*/


    if ($rel_date>=24*30 and $rel_date%(24*30)==0)
    {
	$rel_date=$rel_date/(24*30);
	$rel_date_unit="Months";
    }
    else if($rel_date>=24 and $rel_date%24==0)
    {
	$rel_date=$rel_date/(24);
	$rel_date_unit="Days";
    }
    else
	$rel_date_unit="Hours";
    return array($rel_date,$rel_date_unit);
    
}

?>