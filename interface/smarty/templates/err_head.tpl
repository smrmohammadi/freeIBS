<table align=center border=0>
{if isset($err_msgs) }
    {foreach from=$err_msgs item=err}
	<tr>
	    <td align=left>
		<img border="0" src="/IBSng/images/before_error_message.gif">
	    </td>
	    <td align=left class="error_messages">	    
		{$err|escape:"html"}
	    </td>
	</tr>
    {/foreach}
{/if}
</table>
<br><br>