<table align=center border=0>
{if isset($err_msgs) }
    {foreach from=$err_msgs item=err}
	<tr>
	    <td align=left class="error_messages">
		<img border="0" src="/IBSng/images/arrow_error.gif">&nbsp;{$err|escape:"html"}
	    </td>
	</tr>
    {/foreach}
{/if}
</table>
<br><br>