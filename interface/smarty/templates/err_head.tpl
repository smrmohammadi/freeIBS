<table align=center border=1>
{if isset($err_msgs) }
    {foreach from=$err_msgs item=err}
	<tr>
	    <td align=center>
		{$err|escape:"html"}
	    </td>
	</tr>
    {/foreach}
{/if}
</table>