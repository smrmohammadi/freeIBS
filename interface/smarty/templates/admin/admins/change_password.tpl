{* 
    Change an Admin password
    username: username of admin to change permission
	      if user don't have permission to change other admin passwords
*}
{include file="admin_header.tpl" title="Change Admin Password"}
{include file="err_head.tpl"}
{if $success eq TRUE}
    Password for {$changed_username} Changed Successfully
{/if}

{if $changed_self_password eq TRUE}
    You must <a href="/IBSng/admin"> Relogin </a> Now!
{/if}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Change Password
	<tr {ifibserr varname="username_err" add="bgcolor=red"} >
	    <td>
		Username:
	    <td>
		{if $can_change_others eq TRUE}
		    <select name=username>
			{html_options values=$usernames selected=$default_username output=$usernames}
		    </select>
		{else}
		    {$self_username}
		{/if}


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

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>
    </table>
</center>
</form>

{include file="admin_footer.tpl"}