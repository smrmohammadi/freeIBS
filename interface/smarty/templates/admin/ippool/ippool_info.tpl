{* IPpool Info 
    Show IP pool Informations and show IP's of each pool


*}
{include file="admin_header.tpl" title="IPpool Information"}

{include file="err_head.tpl"}

<center>
<table border=1>
    <tr>
	<td>
	    IP Pool ID:
	<td>
	    {$ippool_id}
	<td>
	    IP Pool Name:
	<td>
	    {$ippool_name}
    <tr>
	<td>
	    Comment:
	<td colspan=3>
	    {$comment}
</table>
<table>
    {foreach from=$ip_list item=ip}
	<tr>
	    <td>
		{$ip}
    {/foreach}
</table>

{include file="footer.tpl"}