<?php

function relExpParser(&$parsed_arr,&$smarty,&$attrs)
{
    if(!isset($attrs["rel_exp_date"]))
	$parsed_arr["has_rel_exp"]=FALSE;
    else
    {
	$parsed_arr["has_rel_exp"]=TRUE;
	$rel_exp=(int)$attrs["rel_exp_date"];
	list($rel_exp,$rel_exp_unit)=calcRelativeDateFromHours($rel_exp);
        $parsed_arr["rel_exp_date_unit"]=$rel_exp_unit;
	$parsed_arr["rel_exp_date"]=$rel_exp;
    }
}


?>
