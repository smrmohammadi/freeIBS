<table>
    <tr>
	<td align=center bgcolor=blue>
	    Multi Login
    {if array_key_exists("multi_login",$attrs)}
	<tr>
	    <td>
		Can Login Up To <b>{$attrs.multi_login}</b> instances
    {/if}
    <tr>
	<td>
	{edit_attr_link template_name="multi_login_edit"}
</table>
	