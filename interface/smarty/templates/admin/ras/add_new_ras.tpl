{* Add New Ras
    ras_ip: new ras ip
    ras_type: type of new ras
    redaius_secret: 
    
    Success: client will be redirected to the new ras information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Ras"}
{include file="err_head.tpl"}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Ras {helpicon subject="add new ras" category="ras"}
	<tr {ifibserr varname="ras_ip_err" add="bgcolor=red"} >
	    <td>
		Ras IP:
	    <td>
		<input type=text name=ras_ip value="{$ras_ip}">
	    <td>
		{helpicon subject="ras ip" category="ras"}
	    
	<tr {ifibserr varname="ras_type_err" add="bgcolor=red"}>
	    <td>
		Ras Type:
	    <td>
		<select name=ras_type>
		    {html_options output=$ras_types values=$ras_types default=$ras_type}
		</select>
	    <td>
		{helpicon subject="ras type" category="ras"}


	<tr {ifibserr varname="radius_secret_err" add="bgcolor=red"}>
	    <td>
		Radius Secret
	    <td>
		<input type=text name=radius_secret value="{$radius_secret}">
	    <td>
		{helpicon subject="radius secret" category="ras"}

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
{include file="footer.tpl"}
