<?php
require_once("init.php");

class CSVGenerator
{
    function CSVGenerator($separator=",",$buffer=False)
    {/*
	$seperator can be ",", ";","\t","TAB", or else it will be set as ","
	if $buffer is true, all lines are buffered instead of print
    */
	$this->separator=$this->getSeparator($separator);
	$this->do_buffer=$buffer;
	if($buffer)
	    $this->buffer=array();
    }

    function getSeparator($separator)
    {
	if (in_array($separator,array(",",";","\t")))
	    return $separator;
	else if ($separator=="TAB")
	    return "\t";
	else
	    return ",";
    }

    function doLine()
    {/*
	convert arguments to csv format
	if do_buffer is true , it will add the line to buffer
	else it will print the line
    */
	$arg_list=func_get_args();
	$this->doArray($arg_list);
    }

    function doArray($arr)
    {
	$line=join($this->separator,$arr)."\r\n";
	if($this->do_buffer)
	    $this->buffer[]=$line;
	else
	    print $line;
    }
    
    function sendHeader($filename)
    {

	header("Content-Type: Text/Text");
	header("Content-Disposition: attachment; filename=".$filename);
    }
    
}

?>