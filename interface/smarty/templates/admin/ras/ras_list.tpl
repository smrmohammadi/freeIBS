{* Ras List
   $ras_infos: array of associative arrays containing active ras infos
   $inactive_ras_infos: array of associative arrays containing inactive ras infos

*}

{include file="admin_header.tpl" title="Ras List"}
{include file="err_head.tpl"}

<center>
{if isset($deactive_success) and $deactive_success}
    <h2>
	Ras DeActivated Successfully
    </h2>
{/if}

{if isset($reactive_success) and $reactive_success}
    <h2>
	Ras ReActivated Successfully
    </h2>
{/if}

    <table>
	<tr>	
	    <th bgcolor=gray colspan=7>
		<h2>Active Rases</2> 
	<tr>
	    <th colspan=7>
	    	{helpicon subject="deactive ras" category="ras" body="Help On Deactive Ras"}
	<tr>
	    <th>
		ID
	    <th>
		Ras IP
	    <th>
		Type
	    <th>
		Radius Secret
		
	{foreach from=$ras_infos item=ras_info}
	    <tr>
		<td>
		    {$ras_info.ras_id}
		<td>
		    {$ras_info.ras_ip}
		<td>
		    {$ras_info.ras_type}
		<td>
		    {$ras_info.radius_secret}
		<td>
		    <a href="/IBSng/admin/ras/ras_info.php?ras_ip={$ras_info.ras_ip|escape:"url"}">
			info
		    </a>
		{if $can_change}
	    	    <td>
			<a href="/IBSng/admin/ras/ras_list.php?deactive={$ras_info.ras_ip|escape:"url"}">
			    DeActive
			</a> 
		    <td>

		{/if}
	{/foreach}

	<tr>	
	    <th bgcolor=gray colspan=7>
		<h2>INActive Rases</2> 
	<tr>
	    <th colspan=7>
	    	{helpicon subject="reactive ras" category="ras" body="Help On Reactive Ras"}
	{foreach from=$inactive_ras_infos item=ras_info}
	    <tr>
		<td>
		    {$ras_info.ras_id}
		<td>
		    {$ras_info.ras_ip}
		<td>
		    {$ras_info.ras_type}
		<td>
		    {$ras_info.radius_secret}
		<td>
		
		{if $can_change}
	    	    <td>
			<a href="/IBSng/admin/ras/ras_list.php?reactive={$ras_info.ras_ip|escape:"url"}">
			    ReActive
			</a>
		    <td>
		{/if}

	{/foreach}
    </table>


</center>

{include file="footer.tpl"}