<?php
require_once("init.php");
require_once("attrs.php");

/*
    Add your attribute parser function name here
*/
$ATTR_PARSER_FUNCTIONS=array("relExpParser");

function callAttrParsers(&$smarty,&$attrs)
{/*
    this function parse attributes that fetched from core and assign them to the parsed_array.
    Functions that are in ATTR_PARSER_FUNCTIONS array are called within the parser
    each of functions called by parsed_array,smarty object and attributes as arguments, and should change parsed_array
    by assigning name value pairs of parsed attributes. function may call smarty object methods
    (ex. for setting page error) 
    
    proto: function func_name(&$parsed_array,&$smarty,&$attrs);

*/
	$parsed_array=array();
	global $ATTR_PARSER_FUNCTIONS;
	foreach($ATTR_PARSER_FUNCTIONS as $parser_name)
//	    call_user_func($parser_name,$smarty,$attrs);
	    eval("{$parser_name}(\$parsed_array,\$smarty,\$attrs);"); //call_user_func always pass arguments with value!
        return $parsed_array;
}


?>
