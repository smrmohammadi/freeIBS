{* Show Permissions of one category
    
*}
{config_load file=perm_category_names.conf}
{include file="admin_header.tpl" title="Add Permission to admin"}
{include file="err_head.tpl"}
    

<center>
{if $add_success eq TRUE}
    <h3>
	Permission Added Successfully
    </h3>
{/if}
	

    <h2> 
	Adding permission to {$admin_username} <a href="/IBSng/admin/admins/admin_perms_list.php?admin_username={$admin_username}">Permission List</a>
    </h2>
	Category : {eval var=$category_name}
    <table border=1>
	<tr>
	    <th>
		Name
	    <th>
		Description
	    <th>
		Affected Pages
	    <th>
		Dependencies
	{foreach from=$perms item=perm}

	    {if $perm.name eq $selected}
		<a name="selected">
		<tr bgcolor=#0a9ffc>
		    <td>
			<nobr>{$perm.name}</nobr>
		    <td>
			{$perm.description|nl2br}  
		    <td>
			{foreach from=$perm.affected_pages item=affected_page}
			    <nobr>{$affected_page}</nobr><br>
			{/foreach}
		    <td>
			{foreach from=$perm.dependencies item=dependency}
			    <nobr>{$dependency}</nobr><br>
			{/foreach}
		<tr bgcolor=#0a9ffc>
		    <form action=/IBSng/admin/admins/show_perms.php>
    		    <input type=hidden name=admin_username value="{$admin_username}">
		    <input type=hidden name=category value="{$category}">
		    <input type=hidden name=perm_name value="{$selected}">
		    <input type=hidden name=selected value="{$selected}">
		    <td colspan=5>
			<table border=1 width=100%>
			    <tr>
				<td>
				    Admin Has this Permission: 
					{if $has_selected_perm eq TRUE} Yes <br> Current Value: 
					    {if $perm.value_type eq "NOVALUE"}
						Permission doesn't need value
					    {elseif $cur_val eq ""}
						Empty
					    {elseif is_array($cur_val)}
    						<table>
						    <tr>
						{foreach from=$cur_val item=val}
						    <td>	    
							{$val}
						{/foreach}
						</table>
					    {else}
						{$cur_val}
					    {/if}
					{else} 
					    No 
					{/if}

		    {if $can_change eq TRUE && $perm.value_type eq "SINGLEVALUE" || $perm.value_type eq "MULTIVALUE" }
			<td>
			    New Value:
			{if isset($perm.value_candidates)}
			    <select name="value">
				{html_options values=$perm.value_candidates output=$perm.value_candidates selected=$selected_value}
			    </select>
			{else}
			    <input type=text name=value 
			    {if $selected_value ne ""}
				value="{$selected_value}"
			    {elseif $perm.value_type eq "SINGLEVALUE" && $has_selected_perm eq TRUE} 
				value="{$cur_val}" 
			    {/if} 
			    >
			{/if}


		    {/if}
			<td>
			    <input type=submit name="submit" value="Add This Permission">
			    

		    </table>

	    {else}
		<tr>
		    <td>
			<a href="/IBSng/admin/admins/show_perms.php?category={$category}&admin_username={$admin_username}&selected={$perm.name|escape:"url"}#selected">
			    <nobr>{$perm.name}</nobr>
			</a>
		    <td>
			{$perm.description|nl2br|truncate:150:"...":false}
		    <td>
			{foreach from=$perm.affected_pages item=affected_page}
			    <nobr>{$affected_page}</nobr><br>
			{/foreach}
		    <td>
			{foreach from=$perm.dependencies item=dependency}
			    <nobr>{$dependency}</nobr><br>
			{/foreach}
	    {/if}
	{/foreach}

    </table>
</center>
</form>

{include file="footer.tpl"}