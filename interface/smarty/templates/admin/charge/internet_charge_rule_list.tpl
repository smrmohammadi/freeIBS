<table border=1>
    <tr>
	<th>
	    Rule ID
	<th>
	    Start Time
	<th>
	    End Time
	<th>
	    CPM
	<th>
	    CPK
	<th>
	    Assumed KPS
	<th>
	    bandwidth_limit(kbytes)

	<th>
	    Ras
	<th>
	    Ports
	<th>
	    Day Of Weeks

{foreach from=$rules item=rule}
<tr>
    <td>
	{$rule.rule_id}
    <td>
	{$rule.start_time}
    <td>
	{$rule.end_time}
    <td>
	{$rule.cpm}
    <td>
	{$rule.cpk}
    <td>
	{$rule.assumed_kps}
    <td>
	{$rule.bandwidth_limit}
    <td>
	{$rule.ras}
    <td>
        <table>
    	    <tr>
	    {foreach from=`$rule.ports` item=port}
		<td>
		    {$port}
	    {/foreach}
	</table}

    <td>
        <table>
    	    <tr>
	    {foreach from=`$rule.day_of_weeks` item=day_name}
		<td>
		    {$day_name}
	    {/foreach}
	</table}
    <td>
    {if $can_change}
	<a href="/IBSng/admin/charge/edit_internet_charge_rule.php?charge_rule_id={$rule.rule_id}&charge_name={$charge_name|escape:"url"}">Edit</a>
    {/if}
    <td>
    {if $can_change}
        <a {jsconfirm msg="Are you sure you want to delete charge rule with id `$rule.rule_id`"} href="/IBSng/admin/charge/charge_info.php?charge_rule_id={$rule.rule_id}&charge_name={$charge_name|escape:"url"}&delete_charge_rule=1">Delete</a>
    {/if}
		
{/foreach}
</table>