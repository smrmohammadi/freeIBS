<table>
    <tr>
	<td align=center>
	    Relative Expiration Date

    <tr>
	<td>
	    <input type=checkbox name=has_attr {if isset($has_attr) or (!isset($update) and $has_rel_exp)} checked {/if} > Have Relative Expiration Date
	    <input type=hidden name=attr__1 value="rel_exp_date">
	    <input type=hidden name=attr__2 value="rel_exp_date_unit">
    <tr>
        <td>
	    Relative Expiration Date: <input type=text name=rel_exp_date value="{$rel_exp_date|default:""}">
	<td>
	    {relative_units default="rel_exp_date_unit" name="rel_exp_date_unit"}
    <tr>
	<td>
	    <input type=submit value=update>
</table>
	