<?php
require_once("voip_tariff.php");

function redirectToTariffList($msg="")
{
    $url="/IBSng/admin/charge/voip_tariff/tariff_list.php";
    if($msg)
	$url.="?msg={$msg}";
    redirect($url);
}

function redirectToTariffInfo($tariff_name)
{
    redirect("/IBSng/admin/charge/voip_tariff/tariff_info.php?tariff_name={$tariff_name}");
}


function intSetTariffInfo(&$smarty,$tariff_name,$include_prefixes=True)
{
    $req=new GetTariffInfo($tariff_name,$include_prefixes);
    $resp=$req->sendAndRecv();
    if($resp->isSuccessful())
	$smarty->assign_array($resp->getResult());
    else
	$resp->setErrorInSmarty($smarty);
}

?>