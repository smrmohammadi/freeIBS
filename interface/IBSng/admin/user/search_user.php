<?php
require_once("search_user_funcs.php");


needAuthType(ADMIN_AUTH_TYPE);
$smarty=new IBSSmarty();

if(isInRequest("search"))
    intDoSearch($smarty);
else
    intShowUserSearch($smarty);
    

?>