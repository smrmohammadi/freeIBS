<?php
require_once("../../inc/init.php");

needAuthType(ADMIN_AUTH_TYPE);
interface();
function interface()
{
    $smarty=new IBSSmarty();
    $smarty->display("admin/report/index.tpl");
}
?>