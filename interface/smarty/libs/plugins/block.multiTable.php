<?php

function smarty_block_multiTable($params,$content,&$smarty,&$repeat)
{/*	Create an Multi Style Table
*/
    
    if(!is_null($content))
    {
    return <<<END
<table cellpadding=0 cellspacing=0 border=0 width=100%>
    {$content}
    </tr>
</table>

END;

    }


}

?>