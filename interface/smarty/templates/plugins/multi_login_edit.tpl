<table>
    <tr>
	<td align=center>
	    Multi Login

    <tr>
	<td>
	    <input type=checkbox name=has_attr {if isset($has_attr) or (!isset($update) and array_key_exists("multi_login",$attrs))} checked {/if} > Have Multi Login
	    <input type=hidden name=attr__1 value="multi_login">
    <tr>
        <td>
	    Multi Login: <input type=text name=multi_login value="{$attrs.multi_login|default:""}">
    <tr>
	<td>
	    <input type=submit value=update>
</table>
