{* List permissions of an admin
    
*}
{config_load file=admin_perms_list.conf}
{config_load file=perm_category_names.conf}
{include file="admin_header.tpl" title="Admin Permission List"}
{include file="err_head.tpl"}

    

<center>

{if $del_perm_success eq TRUE}
    Permission deleted from admin successfully
{/if}

{if $del_perm_val_success eq TRUE}
    Permission Value updated successfully
{/if}

{if $save_template_success eq TRUE}
    Permissions Saved to template successfully
{/if}

{if $load_template_success eq TRUE}
    Permission Template Loaded into admin successfully
{/if}

{if $del_template_success eq TRUE}
    Permission Template Deleted successfully
{/if}

    <h2> 
	"{$admin_username|capitalize}" Permission List
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
			

	    {foreach from=$cat_perms item=perm}
	    <tr>
		<td>
		    <a href="{eval var=#show_perms_link#}">
		    {$perm.name}
		    </a>
		    {if $can_change eq TRUE}
			<a href="/IBSng/admin/admins/admin_perms_list.php?admin_username={$admin_username}&delete_perm={$perm.name|escape:"url"}"
			{jsconfirm msg="Are you sure you want to delete Permission `$perm.name`"}>
			    del
			</a>
		    {/if}
		<td>
		    {if $perm.value_type eq "NOVALUE"}
			No Value
		    {elseif $perm.value_type eq "SINGLEVALUE"}
			{$perm.value} 
			{if $can_change eq TRUE}
			    <a href="{eval var=#show_perms_link#}">
				Change
			    </a>
			{/if}
		    {elseif $perm.value_type eq "MULTIVALUE"}
			<table>
			{foreach from=$perm.value item=val}
			    <tr>
				<td>
				    {$val} 
				<td>
				    {if $can_change eq TRUE}
					<a href="/IBSng/admin/admins/admin_perms_list.php?admin_username={$admin_username}&delete_perm={$perm.name|escape:"url"}&delete_perm_val={$val|escape:"url"}" 
					 {jsconfirm msg="Are you sure you want to delete value $val from `$perm.name`"}>
					    del
					</a>
				    {/if}
			{/foreach}
			{if $can_change eq TRUE}
			    <tr>
				<td colspan=2>
				    <a href="{eval var=#show_perms_link#}">
					<font size=1>
					    Add Another Value
					</font>
				    </a>
			{/if}
			</table>
			    			
		    {/if}
		<td>
		    {$perm.description|truncate:100}
	    {/foreach}
		    </table>
	
	</table>
    {/foreach}


{if $can_change eq TRUE}
    <a href="/IBSng/admin/admins/show_perm_categories.php?admin_username={$admin_username}">
	Add New Permission
    </a>
    
    {include file="admin/admins/admin_perms_list_templates.tpl"}
{/if}
{include file="admin_footer.tpl"}