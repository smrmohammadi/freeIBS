<?php

function smarty_block_reportDetailLayer($params,$content,&$smarty,&$repeat)
{
/*
*/
    if(!is_null($content))
    {
	$ret=<<<END
	<div id="{$params["name"]}" style="position:absolute;width:250px;left:100;top:100;visibility:hidden">
	<table border="0" width="250" bgcolor="#424242" cellspacing="0" cellpadding="5">
	    <tr>
		<td width="100%">
		     <table border="0" width="100%" cellspacing="0" cellpadding="0" height="36">
    			 <tr>
			     <td width="100%">
				     <ilayer width="100%" onSelectStart="return false">
					 <layer width="100%">
					     <font face="Arial" color="#FFFFFF">{$params["title"]}</font>
					 </layer>
				     </ilayer>
			    </td>
			    <td style="cursor:hand" valign="top">
				<a href="#" onClick="document.getElementById('{$params["name"]}').style.visibility='hidden';return false">
				    <font color=#ffffff size=2 face=arial  style="text-decoration:none">
					X
				    </font>
				</a>
			     </td>
		     </tr>
		     <tr>
			 <td width="100%" bgcolor="#FFFFFF" style="padding:4px" colspan="2">
			    {$content}
			 </td>
		     </tr>
	    	    </table> 
		</td>
	    </tr>
	</table>
	</div>


END;
	return $ret;

    }
}

?>