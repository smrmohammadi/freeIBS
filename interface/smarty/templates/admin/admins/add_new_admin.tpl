{* Admin Add New Admin
    username: new admin username
    password: new admin password
    name: new admin name
    comment: comments about new admin
    
    Success: client will be redirected to the new admin information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Admin"}
{include file="err_head.tpl"}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Admin
	<tr {ifibserr varname="username_err" add="bgcolor=red"} >
	    <td>
		Username:
	    <td>
		<input type=text name=username value="{$username}">
	    <td>
		{helpicon subject="username" category="admin"}
	    
	<tr {ifibserr varname="password_err" add="bgcolor=red"}>
	    <td>
		Password:
	    <td>
		<input type=password name=password1>

	<tr {ifibserr varname="password_err" add="bgcolor=red"}>
	    <td>
		Confirm Password:
	    <td>
		<input type=password name=password2>

	<tr {ifibserr varname="name_err" add="bgcolor=red"}>
	    <td>
		Name:
	    <td>
		<input type=text name=name value="{$name}">
	
	<tr {ifibserr varname="comment_err" add="bgcolor=red"}>
	    <td>
		Comment:
	    <td>
		<textarea name=comment> 
		    {$comment} 
		</textarea>
	<tr>
	    <td colspan=2>
		<input type=submit name=submit>
    </table>
</center>
</form>


{include file="footer.tpl"}