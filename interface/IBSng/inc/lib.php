<?php
require_once("attr_lib.php");

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

function convertRequestToUrl($ignore_list=array())
{/*
    convert request key/values to url parameters.
    keys that are in $ignore_list array are ignored
*/
    $name_vals=array();
    foreach($_REQUEST as $key=>$value)
    {
	if(in_array($key,$ignore_list))
	    continue;

        if(is_array($value))
            foreach($value as $x)
               $name_vals[]=urlencode("{$key}[]")."=".urlencode($x);
	else
	    $name_vals[]="{$key}=".urlencode($value);
    }
    return join("&",$name_vals);
}

?>