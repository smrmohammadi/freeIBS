{* Add New Charge
    charge_name: new ras ip
    charge_type: type of new charge
    comment: 
    visible_to_all: Visible to all flag for charge
    
    Success: client will be redirected to the new charge information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Charge"}
{include file="err_head.tpl"}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Charge {helpicon subject="add new charge" category="charge"}
	<tr {ifibserr varname="charge_name_err" add="bgcolor=red"} >
	    <td>
		Charge Name:
	    <td>
		<input type=text name=charge_name value="{$charge_name}">
	    <td>
		{helpicon subject="charge name" category="charge"}
	    
	<tr {ifibserr varname="charge_type_err" add="bgcolor=red"}>
	    <td>
		Charge Type:
	    <td>
		<select name=charge_type>
		    {html_options output=$charge_types values=$charge_types default=$charge_type}
		</select>
	    <td>
		{helpicon subject="charge type" category="charge"}


	<tr {ifibserr varname="comment_err" add="bgcolor=red"}>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    {$comment|strip}
		</textarea>
	    <td>

	<tr {ifibserr varname="visible_to_all_err" add="bgcolor=red"}>
	    <td>
		Visible To All
	    <td>
		<input type=checkbox name=visible_to_all {$visible_to_all}>
	    <td>
		{helpicon subject="visible to all" category="charge"}
	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
{include file="admin_footer.tpl"}
