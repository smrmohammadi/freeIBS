<?php
require_once("../../inc/init.php");
require_once(IBSINC."ras_face.php");
require_once(IBSINC."ras.php");

needAuthType(ADMIN_AUTH_TYPE);

if(isInRequest("ras_ip","ras_type","radius_secret"))
    intAddRas();
else
    interface();

function intAddRas()
{
    $add_new_ras=new addNewRas($_REQUEST["ras_ip"],$_REQUEST["ras_type"],$_REQUEST["radius_secret"]);
    list($success,$arg)=$add_new_ras->send();
    if($success)
      	redirectToRasInfo($_REQUEST["ras_ip"]);
    else
	interface($arg);
}

function interface($err=NULL)
{
    $smarty=new IBSSmarty();
    intAssignValues($smarty);
    intSetRasTypes($smarty);
    if(!is_null($err))
    {
	intSetErrors($smarty,$err->getErrorKeys());
	$smarty->set_page_error($err->getErrorMsgs());
    }
    $smarty->display("admin/ras/add_new_ras.tpl");    
}

function intAssignValues(&$smarty)
{
    $smarty->assign_array(array("ras_ip"=>requestVal("ras_ip"),
			       "ras_type"=>requestVal("ras_type"),
			       "radius_secret"=>requestVal("radius_secret")
			      ));
}

function intSetErrors(&$smarty,$err_keys)
{
    $smarty->set_field_errs(array("ras_ip_err"=>array("INVALID_RAS_IP",
						      "RAS_IP_ALREADY_EXISTS",
						      "RAS_IS_INACTIVE"),
				     "ras_type_err"=>array("RAS_TYPE_NOT_REGISTERED")
				    ),$err_keys);

}

?>