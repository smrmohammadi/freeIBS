{* Add New or edit Internet Charge Rule
    
    Success: client will be redirected to the charge information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Internet Charge Rule"}
{include file="err_head.tpl"}

<center>
<form method=POST name=add_internet_rule>
<table border=1>
    <tr>
	<td>
	    Charge Name:
	<td>
	    {$charge_name}
	    <input type=hidden name=charge_name value="{$charge_name}">
	<td>
	    {if $is_editing}
		Charge Rule ID:
	    {/if}
	<td>
	    {if $is_editing}
		{$rule_id}
		<input type=hidden name=charge_rule_id value="{$rule_id}">
	    {/if}


    <tr>
	<td colspan=4 {ifibserr varname="dow_err" add="bgcolor=red"}>
	    {include file="admin/charge/day_of_week_select.tpl" form_name="add_internet_rule"}
    <tr>
	<td {ifibserr varname="rule_start_err" add="bgcolor=red"}>
	    Rule Start Time:
	<td {ifibserr varname="rule_start_err" add="bgcolor=red"}>
	    <input type=text name=rule_start value="{ifisinrequest name="rule_start" default_var="start_time"}" >

	<td {ifibserr varname="rule_end_err" add="bgcolor=red"}>
	    Rule End Time:
	<td {ifibserr varname="rule_end_err" add="bgcolor=red"}>
	    <input type=text name=rule_end value="{ifisinrequest name="rule_end" default_var="end_time"}">

    <tr>
	<td {ifibserr varname="cpm_err" add="bgcolor=red"}>
	    Charge Per Minute:
	<td {ifibserr varname="cpm_err" add="bgcolor=red"}>
	    <input type=text name=cpm value="{ifisinrequest name="cpm" default_var="cpm" }"> {$MONEY_UNIT}
	    
	<td {ifibserr varname="cpk_err" add="bgcolor=red"}>
	    Charge Per KiloByte:
	<td {ifibserr varname="cpk_err" add="bgcolor=red"}>
	    <input type=text name=cpk value="{ifisinrequest name="cpk" default_var="cpk" }"> {$MONEY_UNIT}

    <tr>
	<td {ifibserr varname="assumed_kps_err" add="bgcolor=red"}>
	    Assumed Kilo Byte Per Second:
	<td {ifibserr varname="assumed_kps_err" add="bgcolor=red"}>
	    <input type=text name=assumed_kps value="{ifisinrequest name="assumed_kps" default_var="assumed_kps" }"> Kilo Bytes
	    
	<td {ifibserr varname="bw_limit_err" add="bgcolor=red"}>
	    Bandwidth Limit:
	<td {ifibserr varname="bw_limit_err" add="bgcolor=red"}>
	    <input type=text name=bandwidth_limit_kbytes value="{ifisinrequest name="bandwidth_limit_kbytes" default_var="bandwidth_limit" }"> KB/s

    <tr>
	<td colspan=4>
	    {include file="admin/charge/ras_select.tpl"}
    <tr>
	<td colspan=4>
	    <input type=submit value=add>
</table>
{include file="admin_footer.tpl"}
