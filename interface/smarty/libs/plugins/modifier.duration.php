<?php
function smarty_modifier_duration($seconds)
{	/*
	    make seconds look like durations in format xxxx:xx:xx
	*/
    $hours=(int)($seconds/3600);
    if($hours<10)
	$hours="0{$hours}";
    $rest=$seconds%3600;
    $mins=(int)($rest/60);
    if($mins<10)
	$mins="0{$mins}";
    $secs=$rest%60;
    if($secs<10)
	$secs="0{$secs}";

    return "{$hours}:{$mins}:{$secs}";
}
?>
