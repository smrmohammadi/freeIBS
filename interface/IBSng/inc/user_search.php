<?php
require_once("init.php");
require_once(IBSINC."user.php");
require_once(INTERFACE_ROOT."IBSng/admin/user/search_user_funcs.php");

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
    return array($count,$user_ids,getUsersInfoByUserID($smarty,$user_ids));
}

function redirectToUserSearch($url_conds)
{
    redirect("/IBSng/admin/user/search_user.php?search=1&show__normal_username=1&show__group=1&show__credit=1&show__owner=1&{$url_conds}");
}

function redirectToUserSearchInc($conds)
{
    if(!isInRequest("search"))
    {
	$_REQUEST["search"]=1;
	$_REQUEST["show__normal_username"]=1;
	$_REQUEST["show__group"]=1;
	$_REQUEST["show__credit"]=1;
	$_REQUEST["show__owner"]=1;
    }
    foreach($cond as $key=>$value)
	$_REQUEST[$key]=$value;
    intDoSearch(new IBSSmarty());
}

?>