<table>
    <tr>
	<td align=center bgcolor=blue>
	    Relative Expiration Date
    {if $has_rel_exp}
	<tr>
	    <td>
		{$rel_exp_date}
	    <td>
		{$rel_exp_date_unit}
    {/if}
    <tr>
	<td>
	{edit_attr_link template_name="rel_exp_date_edit"}
</table>
	