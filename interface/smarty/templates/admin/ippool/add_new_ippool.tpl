{* Add New IPPOOL
    ippool_name: new ippool_name
    comment: comment!
    
    Success: client will be redirected to the new ippool information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New IPPOOL"}
{include file="err_head.tpl"}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New IPPOOL {helpicon subject="add new ippool" category="ippool"}
	<tr {ifibserr varname="ippool_name_err" add="bgcolor=red"} >
	    <td>
		Ras IP:
	    <td>
		<input type=text name=ippool_name value="{$ippool_name}">
	    <td>
		{helpicon subject="ippool name" category="ippool"}
	    
	<tr {ifibserr varname="ippool_comment_err" add="bgcolor=red"}>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    {$comment}
		</textarea>
	    <td>

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
{include file="footer.tpl"}
