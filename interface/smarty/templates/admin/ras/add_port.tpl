{* Add New Port
    ras_ip: new ras ip (invisible)
    port name: string representation of port
    phone: phone number
    type: port type
    comment: 
    
    Success: client will be redirected to the ras information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add Port To Ras"}
{include file="err_head.tpl"}

<form method=POST name=add_port>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add Port To Ras {helpicon subject="add ras port" category="ras"}
	<tr>
	    <td>
		Ras IP:
	    <td>
		{$ras_ip}
	    <td>
	    
	<tr {ifibserr varname="port_name_err" add="bgcolor=red"}>
	    <td>
		Port Name:
	    <td>
		<input type=text name=port_name value="{$port_name}">
	    <td>
		{helpicon subject="port name" category="ras"}
		{multistr form_name="add_port" input_name="port_name"}


	<tr {ifibserr varname="port_type_err" add="bgcolor=red"}>
	    <td>
		Port Type:
	    <td>
		<select name=port_type>
		    {html_options output=$port_types values=$port_types default=$port_type}
		</select>
	    <td>
		{helpicon subject="port type" category="ras"}


	<tr {ifibserr varname="phone_err" add="bgcolor=red"}>
	    <td>
		Phone no.:
	    <td>
		<input type=text name=phone value="{$phone}">
	    <td>
		{helpicon subject="phone" category="ras"}
		{multistr form_name="add_port" input_name="phone"}

	<tr {ifibserr varname="comment_err" add="bgcolor=red"}>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    {$comment|strip}
		</textarea>
	    <td>
		{multistr form_name="add_port" input_name="comment"}
	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
{include file="footer.tpl"}
