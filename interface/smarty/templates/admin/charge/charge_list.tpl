{* Charge List
   $charge_infos: array of associative arrays containing charge infos
*}

{include file="admin_header.tpl" title="Charge List"}
{include file="err_head.tpl"}

<center>
<table>
    <tr>
	<th>
	    Charge Name
	<th>
	    Charge Type
	<th>
	    Visible To All
	<th>
	    Creator
	<th>
	    	
    
    {foreach from=$charge_infos key=charge_name item=charge_info}
	<tr>
	    <td>
		{$charge_name}
	    <td>
		{$charge_info.charge_type}	
    	    <td>
		{$charge_info.visible_to_all}
	    <td>
		{$charge_info.creator}
	    <td>
		<a href="/IBSng/admin/charge/charge_info.php?charge_name={$charge_name|escape:"url"}">info</a>
	
    {/foreach}
</table>
</center>
{include file="footer.tpl"}