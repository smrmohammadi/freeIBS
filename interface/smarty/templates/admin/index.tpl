{* Admin Login Page


*}

{include file="header.tpl" title="Admin Login"}

<center>
    {include file="err_head.tpl"}

    <form method=POST>
    <table>
	<tr>
	    <td colspan=2 align=center>
		Admin Login
	<tr>
	    <td>
		Username:
	    <td>
		<input type=text name=username>
	<tr>
	    <td>
		Password:
	    <td>
		<input type=password name=password>
	<tr>
	    <td colspan=2 align=center>
		<input type=submit name=submit value=submit>

    </table>
    </form>
</center>

{include file="footer.tpl"}