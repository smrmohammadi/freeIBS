{* Show all string of a multistr
   on success page is shown
   on failure error is shown on top of page
   Variables:
    $raw_str : raw multi string
    $all_strs: decomposed strings of multi str
*}

{include file="header.tpl" title="Show Multiple Strings"}
{include file="err_head.tpl"}
<table border=1 align=center width=100% bgcolor=#FAFFC5>
<tr align=center bgcolor=#3E91EB>
    <td>
	<h2>Show Multiple Strings</h2>
<tr align=left>
    <td>
	Raw Multi String: <b>{$raw_str}</b>
<tr align=left>
    <table width=100% border=1>
    {foreach from=$all_strs key=index item=str}
	{if $index%3==0} <tr align=center>  {/if}
	    <td bgcolor=#3E91EB width=10%>
		{math equation="index+1" index=$index}
	    <td width=20%>
		{$str}
    {/foreach}
    </table>
</table>

{literal}
<script language="javascript">
    window.focus();
</script>
{/literal}

{include file="footer.tpl"}
