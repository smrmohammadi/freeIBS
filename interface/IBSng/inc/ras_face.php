<?php
require_once("ras.php");


function redirectToRasInfo($ras_ip)
{
    redirect("/IBSng/admin/ras/ras_info.php?ras_ip={$ras_ip}");
}

function redirectToRasList($msg="")
{
    redirect("/IBSng/admin/ras/ras_list.php?msg={$msg}");
}

function intSetRasTypes(&$smarty)
{
    $ras_types_req=new GetRasTypes();
    list($success,$types)=$ras_types_req->send();
    if($success)
	$smarty->assign("ras_types",$types);
    else
    {
	$smarty->assign("ras_types",array());
	$smarty->set_page_error($types->getErrorMsgs());
    }
}

function intSetPortTypes(&$smarty)
{
    $port_types_req=new GetPortTypes();
    list($success,$types)=$port_types_req->send();
    if($success)
	$smarty->assign("port_types",$types);
    else
    {
	$smarty->assign("port_types",array());
	$smarty->set_page_error($types->getErrorMsgs());
    }
}

function intSetRasAndPorts(&$smarty)
{
    $rases=array();
    $rases_ip_req=new GetActiveRasIPs();
    list($success,$ras_ips)=$rases_ip_req->send();
    if(!$success)
	$smarty->set_page_error($ras_ips->getErrorMsgs());
    else
    {
	$ras_ports_req=new GetRasPorts("");
	foreach ($ras_ips as $ras_ip)
	{
	    $ras_ports_req->changeParam("ras_ip",$ras_ip);
	    list($success,$ports)=$ras_ports_req->send();
	    if(!$success)
	    {
		$smarty->set_page_error($ports->getErrorMsgs());
		break;
	    }
	    $rases[$ras_ip]=$ports;
	}
    }
    $smarty->assign("rases",$rases);
}	

?>