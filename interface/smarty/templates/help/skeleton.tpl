{include file="help_header.tpl"}
<table border=1 align=center width=100% bgcolor=#FAFFC5 id="help_table">
<tr align=center bgcolor=#3E91EB>
    <td>
	<h2>Help!</h2>
<tr align=left>
    <td>
	Subject: <b>{$subject|capitalize}</b>
<tr align=left>
    <td>
	Category: <b>{$category|capitalize}</b>
<tr>
    <td>
	{include file=$tpl_file}

</table>

{literal}
<script language="javascript">

    window.focus();
    element=document.getElementById("help_table");
    height=0;
    while (element)
    {    
	height+=element.offsetHeight;
	if(element.offsetTop)
	    height+=element.offsetTop;
	if(element.offsetParent)
	    element=element.offsetParent;
	else
	    element=null;
    }
//    alert(height);
    window.resizeTo(window.outerWidth,height-100);
</script>
{/literal}

{include file="help_footer.tpl"}