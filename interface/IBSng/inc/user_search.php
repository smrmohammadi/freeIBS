<?php
require_once("init.php");
require_once(IBSINC."user.php");

class UserSearch
{
    function UserSearch()
    {
	$this->conds=array();
    }

    function getConds()
    {
	return $this->conds;
    }

    function addToConds($name,$value)
    {/*
	add $name and $value to internal associative array
    */
	$this->conds[$name]=$value;
    }

    function __addFromRequest($request_key)
    {
	$this->addToConds($request_key,$_REQUEST[$request_key]);
    }

    function addToCondsFromRequest($not_empty=TRUE)
    {/*
	add request arguments to internal dic. request keys are passed as arguments and values are in request
	You can set how many arguments you want
	but arguments will be added to dic only if all of them exists.
	if $not_empty flag is set, they are checked not to be empty and will be added only when
	none of them was empty string
    */
	$arg_list=array_slice(func_get_args(),1);	
	foreach($arg_list as $arg)
	{
	    if (!isInRequest($arg))
		return;
	    if ($_REQUEST[$arg]=="")
		return;
	}
	foreach($arg_list as $arg)
	    $this->__addFromRequest($arg);
    }

    function addToCondsFromCheckBoxRequest($prefix,$cond_name)
    {/*	add check box conditions in internal dic. all checkboxes of same group should have a same prefix
	postfixed by an integer id. We find all values in request and set em in internet dic
    */
	$val_arr=array();
	foreach($_REQUEST as $name=>$val)
	    if(preg_match("/^{$prefix}[0-9]+/",$name))
		$val_arr[]=$val;
	    if (sizeof($val_arr)!=0)
		$this->addToConds($cond_name,$val_arr);
    }
}

class SearchUser extends Request
{
    function SearchUser($conds,$from,$to,$order_by,$desc)
    {
	parent::Request("user.searchUser",array("conds"=>$conds,
						"from"=>$from,
						"to"=>$to,
						"order_by"=>$order_by,
						"desc"=>$desc));
    }
}


function searchUser(&$smarty,&$conds,$from,$to,$order_by,$desc)
{
    $req=new SearchUser($conds,$from,$to,$order_by,$desc);
    $resp=$req->sendAndRecv();
    if(!$resp->isSuccessful())
    {
	$resp->setErrorInSmarty($smarty);
	return array(0,array());
    }
    list($count,$user_ids)=$resp->getResult();
    return array($count,getUsersInfoByUserID($smarty,$user_ids));
}


?>