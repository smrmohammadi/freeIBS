<?php
require_once("init.php");
require_once(XMLRPCINC."xmlrpc.inc");
require_once(IBSINC."auth.php");



class Request
{ /* This is class for all requests
     other requests may inherit from this class but don't forget to call parent::Request() in constructor
  */

    function Request($server_method,$params_arr)
    {
	$this->server_method=$server_method;
	$this->__addAuthParams($params_arr);
	$this->params_arr=$params_arr;
	$this->ibs_rpc=new IBSxmlrpc();
    }

    function __addAuthParams(&$params_arr)
    {
	$auth_obj=getAuth();
	list($auth_name,$auth_pass,$auth_type)=$auth_obj->getAuthParams();
	$params_arr["auth_name"]=$auth_name;
	$params_arr["auth_pass"]=$auth_pass;
	$params_arr["auth_type"]=$auth_type;
	$params_arr["auth_remoteaddr"]=getClientIPAddress();
    }

    function changeParam($key,$value)
    {/* change internal kept params array, set $key value to $value,
	useful when using one request object for multiple server calls
     */
	$this->params_arr[$key]=$value;
    }

    function send()
    {/* send request, and return the response in format ($success(bool),$msg(mix))
        it will call $this->check(), this function should be override by children in case 
	of they need some checking before sending request
     */
	list($success,$msg)=$this->__check();
	if(!$success)
	    return array($success,$msg);
	else
	    return $this->ibs_rpc->sendRequest($this->server_method,$this->params_arr);
    }

    
    function __check()
    {/*Children can override this function to check inputs before sending the request
       This should return an array of (FALSE,$failure_msg) on failure or (TRUE,don't care) on success
     */
	return array(TRUE,null);
    }

}


?>