<?php
require_once("init.php");

class AddNewCharge extends Request
{
    function AddNewCharge($name,$charge_type,$visible_to_all,$comment)
    {
	parent::Request("charge.addNewCharge",array("name"=>$name,
					         "comment"=>$comment,
					    	 "charge_type"=>$charge_type,
						 "visible_to_all"=>($visible_to_all==TRUE)?"t":"f"
						 ));
    }
}

class UpdateCharge extends Request
{
    function UpdateCharge($charge_id,$charge_name,$visible_to_all,$comment)
    {
	parent::Request("charge.updateCharge",array("charge_id"=>$charge_id,
						 "charge_name"=>$charge_name,
					         "comment"=>$comment,
						 "visible_to_all"=>($visible_to_all==TRUE)?"t":"f"
						 ));
    }
}


class GetChargeInfo extends Request
{
    function GetChargeInfo($charge_name)
    {
	parent::Request("charge.getChargeInfo",array("charge_name"=>$charge_name));
    }
}


class AddInternetChargeRule extends Request
{
    function AddInternetChargeRule($charge_name,$rule_start,$rule_end,$cpm,$cpk,
			    $assumed_kps,$bandwidth_limit_kbytes,$ras,$ports,$dows)
    {
	parent::Request("charge.addInternetChargeRule",array("charge_name"=>$charge_name,
							     "rule_start"=>$rule_start,
							     "rule_end"=>$rule_end,
							     "cpm"=>$cpm,
							     "cpk"=>$cpk,
							     "assumed_kps"=>$assumed_kps,
							     "bandwidth_limit_kbytes"=>$bandwidth_limit_kbytes,
							     "ras"=>$ras,
							     "ports"=>$ports,
							     "dows"=>$dows
							     ));
    }
}

class ListChargeRules extends Request
{
    function ListChargeRules($charge_name)
    {
	parent::Request("charge.listChargeRules",array("charge_name"=>$charge_name));
    }
}

class ListCharges extends Request
{
    function ListCharges($charge_type=null)
    {
	if(is_null($charge_type))
	    $params=array();
	else
	    $params=array("charge_type"=>$charge_type);

	parent::Request("charge.listCharges",$params);
    }
}

class UpdateInternetChargeRule extends Request
{
    function UpdateInternetChargeRule($charge_name,$charge_rule_id,$rule_start,$rule_end,$cpm,$cpk,
			    $assumed_kps,$bandwidth_limit_kbytes,$ras,$ports,$dows)
    {
	parent::Request("charge.updateInternetChargeRule",array("charge_name"=>$charge_name,
							     "charge_rule_id"=>$charge_rule_id,
							     "rule_start"=>$rule_start,
							     "rule_end"=>$rule_end,
							     "cpm"=>$cpm,
							     "cpk"=>$cpk,
							     "assumed_kps"=>$assumed_kps,
							     "bandwidth_limit_kbytes"=>$bandwidth_limit_kbytes,
							     "ras"=>$ras,
							     "ports"=>$ports,
							     "dows"=>$dows
							     ));
    }
}

class DelChargeRule extends Request
{
    function DelChargeRule($charge_rule_id,$charge_name)
    {
	parent::Request("charge.delChargeRule",array("charge_rule_id"=>$charge_rule_id,
						     "charge_name"=>$charge_name));
    }
}


?>
