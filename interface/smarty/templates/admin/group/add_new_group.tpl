{* Add New Group
    group_name: new group
    comment: 
    
    Success: client will be redirected to the new group information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Group"}
{include file="err_head.tpl"}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Group {helpicon subject="add new group" category="group"}
	<tr {ifibserr varname="group_name_err" add="bgcolor=red"} >
	    <td>
		Group Name:
	    <td>
		<input type=text name=group_name value="{$group_name}">
	    <td>
		{helpicon subject="group name" category="group"}
	    
	<tr {ifibserr varname="comment_err" add="bgcolor=red"}>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    {$comment|strip}
		</textarea>
	    <td>

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
{include file="footer.tpl"}
