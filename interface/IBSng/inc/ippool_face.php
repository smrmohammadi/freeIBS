<?php
require_once("ippool.php");

function redirectToIPpoolInfo($ippool_name)
{
    redirect("/IBSng/admin/ippool/ippool_info.php?ippool_name={$ippool_name}");
}

function redirectToIPpoolList($msg)
{
    redirect("/IBSng/admin/ippool/ippool_list.php?msg={$msg}");
}


?>