{include file="admin_header.tpl" title="IBS Definitions"}

<center>
    <h2>
	IBS Definitions 
    </h2>
{include file="err_head.tpl"}

{if $save_success}
    Definitions updated successfully
{/if}

    <p>
	Warning: Changing these value may result IBS not working properly. Don't change any value until you know
	what are you doing.
    </p>

<table align=center border=1>
    <form method=POST>
    {foreach from=$defs_arr item=def_arr}
    <tr valign=top>
	<td>
	    {$def_arr.name}
	<td>
	    {if is_array($def_arr.value)}
		<table>
		{foreach from=$def_arr.value key=index item=member }
		    <tr>
			<td>
			    <input type=text name="def_{$def_arr.name}__{$index}__" value="{$member}">
		{/foreach}
		    <font size=1>(new value)</font><input type=text name="def_{$def_arr.name}__new__" value="">
		</table>
	    {else}
		<input type=text name="def_{$def_arr.name}" value="{$def_arr.value}">
	    {/if}
    
    
    {/foreach}

</table>
    <input type=hidden name=action value=save>
    <input type=submit name=submit value="save">
</center>
</form>

{include file="footer.tpl"}
