{* List permissions of an admin
    
*}
{config_load file=perm_category_names.conf}
{include file="header.tpl" title="Template Permission List"}
{include file="err_head.tpl"}

    

<center>

    <h2> 
	Template "{$template_name|capitalize}" Permission List
    </h2>
    {foreach from=$perms key=category item=cat_perms}
	<table>
	    <tr>
		<td>
		    Category: {$category_names.$category}
	    <tr>
		<td>
		    <table border=1>
			<tr>
			    <th>
				Name
			    <th>
				Value
			    <th>
				Description
			

	    {section loop=$cat_perms name=index}
	    <tr>
		<td>

		    {$cat_perms[index].name}
		<td>
		    {if $cat_perms[index].value_type eq "NOVALUE"}
			No Value
		    {elseif $cat_perms[index].value_type eq "SINGLEVALUE"}
			{$cat_perms[index].value} 
		    {elseif $cat_perms[index].value_type eq "MULTIVALUE"}
			<table>
			{foreach from=$cat_perms[index].value item=val}
			    <tr>
				<td>
				    {$val} 
			{/foreach}
			</table>
			    			
		    {/if}
		<td>
		    {$cat_perms[index].description|truncate:50}
	    {/section}
		    </table>
	
	</table>
    {/foreach}
{literal}
<script language="javascript">
    window.focus();
</script>
{/literal}

{include file="footer.tpl"}