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
{/*
    Set Ras Types into smarty object variable name "ras_types"
*/
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
{/*
    Set port types into smarty object variable name "port_types"
*/
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
{/*
    Get Ras IPs and Ports from core, and assign them to smarty object variable name "rases"
    rases is and associative array with key as ras ip addess and values as ports arrays
    rases=array(ras_ip=>ports_array,...)
    ports_array=array(port1_name,port2_name,...)
*/
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