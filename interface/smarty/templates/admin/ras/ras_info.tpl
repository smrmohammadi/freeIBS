{* Ras Info
    Shows one ras information, including ports and attributes
    on fatal errors that no info can be shown, client is redirected to admin_list
    else error is shown on top of page
    
    Variables:
    
*}
{include file="admin_header.tpl" title="Ras Information"}

{include file="err_head.tpl"}

<center>

{if isset($update_ras_info_success) and $update_ras_info_success}
    <h2>
	Ras Info Updated Successfully
    </h2>
{/if}

{if isset($update_ras_attrs_success) and $update_ras_attrs_success}
    <h2>
	Ras Attributes Updated Successfully
    </h2>
{/if}


{if isset($reset_ras_attrs_success) and $reset_ras_attrs_success}
    <h2>
	Ras Attributes Reset Successfully
    </h2>
{/if}

{if isset($del_port_success) and $del_port_success}
    <h2>
	Port(s) Deleted Successfully
    </h2>
{/if}

{if isset($add_ippool_success) and $add_ippool_success}
    <h2>
	IP Pool Added To Ras Successfully
    </h2>
{/if}

{if isset($del_ippool_success) and $del_ippool_success}
    <h2>
	IP Deleted From Ras Successfully
    </h2>
{/if}

</center>


{if $is_editing or $attr_editing}
    <form method=POST action="/IBSng/admin/ras/ras_info.php">
{/if}
{if $is_editing}
    <input type=hidden name=edit value=1>
    <input type=hidden name=old_ras_ip value="{$info.ras_ip}">
    <input type=hidden name=ras_id value="{$info.ras_id}">
{/if}

{if $attr_editing}
    <input type=hidden name=attr_editing_done value=1>
    <input type=hidden name=ras_ip value="{$info.ras_ip}">
{/if}
    
<center>
    <table border=1>
	<tr>	
	    <td>

		Ras IP:
	    <td {ifibserr varname="ras_ip_err" add="bgcolor=red"}>
		{if $is_editing}
		    <input type=text name=ras_ip value="{$info.ras_ip}">
		    
		    
		{else}		
		    {$info.ras_ip}
		{/if}
	    <td>
		Ras ID:
	    <td>
		{$info.ras_id}
	<tr>
	    <td>
		Type:
	    <td {ifibserr varname="ras_type_err" add="bgcolor=red"}>
		{if $is_editing}
		    <select name=ras_type>
			{html_options output=$ras_types values=$ras_types default=$info.ras_type}
		    </select>
		{else}		
		    {$info.ras_type}
		{/if}
	    <td>
		Radius Secret:
	    <td {ifibserr varname="ras_radius_secret_err" add="bgcolor=red"}>
		{if $is_editing}
		    <input type=text name=radius_secret value="{$info.radius_secret}">
		{else}		
		    {$info.radius_secret}
		{/if}
    </table>
</center>
<table width=100% border=1>
    <tr valign=top>
	<td>
	    <table border=1>
		<tr>
		    <td colspan=2 align=center>
			Attributes
		<tr>
		    <td align=center>
			Name
		    <td align=center>
			Value
	    
		{foreach from=$attrs key=attr_name item=attr_value}
		    <tr>
			<td>
			    {$attr_name}
			<td>
			    {if $attr_editing}
				<input type=text name="attr__{$attr_name}" value="{$attr_value}">
			    {else}
				{$attr_value}
			    {/if}
		{/foreach}
	    </table>
	<td>
	    <table border=1>
		<tr>
		    <td colspan=4 align=center>
			Ports
		<tr>
		    <td align=center>
			Port Name
		    <td align=center>
			Type
		    <td align=center>
			Phone
		    <td align=center>
			Comment

		{foreach from=$ports item=port_info}
		    <tr>
			<td>
			    {$port_info.port_name}
			<td>
			    {$port_info.type}
			<td>
			    {$port_info.phone}
			<td>
			    {$port_info.comment}
			{if not $is_editing and not $attr_editing and $can_change}
			    <td>
				<a href="/IBSng/admin/ras/ras_info.php?ras_ip={$info.ras_ip|escape:"url"}&del_port={$port_info.port_name|escape:"url"}" {jsconfirm msg="Are you sure you want to delete port `$port_info.port_name`"}>
				    del
				</a>

			    <td>
				<a href="/IBSng/admin/ras/edit_port.php?ras_ip={$info.ras_ip|escape:"url"}&port_name={$port_info.port_name|escape:"url"}">
				    edit
				</a>
			{/if}
		{/foreach}

	    </table>
    <tr>
	<td>

	    <table border=1>
		<tr>
		    <td colspan=2 align=center>
			Ras IP Pools
		<tr>
		    <td align=center>
			IP Pool Name
	    
		{foreach from=$ras_ippools item=ras_ippool_name}
		    <tr>
			<td>
			    {$ras_ippool_name}
			<td>
			    {if not $is_editing and not $attr_editing and $can_change}
				<a href="/IBSng/admin/ras/ras_info.php?ras_ip={$info.ras_ip|escape:"url"}&del_ip_pool={$ras_ippool_name|escape:"url"}">
				    del
				</a>
			    {/if}
		{/foreach}
	    </table>
	    
</table>


<table>
{if not $is_editing and not $attr_editing and $can_change}
    <table>
	<tr>
	    <td>
		<a href="/IBSng/admin/ras/ras_info.php?ras_ip={$info.ras_ip}&edit=1">
		    Edit Ras Informations
		</a>
	<tr>
	    <td>
		<a href="/IBSng/admin/ras/ras_info.php?ras_ip={$info.ras_ip}&edit_attrs=1">
		    Edit Ras Attributes
		</a>

	<tr>
	    <td>
		<a href="/IBSng/admin/ras/ras_info.php?ras_ip={$info.ras_ip}&reset_attrs=1" {jsconfirm msg="Reset attributes of ras `$info.ras_ip` to default?"}>
		    Reset Ras Attributes To Default
		</a>

	<tr>
	    <td>
		<a href="/IBSng/admin/ras/add_port.php?ras_ip={$info.ras_ip}">
		    Add Port(s)
		</a>
	<tr>
	    <td>
			<form method=POST action="/IBSng/admin/ras/ras_info.php" name=del_port>
				<input type=hidden name=ras_ip value="{$info.ras_ip}">
		    Del Port(s): <input type=text name=del_port> {multistr form_name="del_port" input_name="del_port"}
				<input type=submit value=del {jsconfirm msg="Are you sure?"}>
			</form>

	<tr>
	    <td>
				<form method=POST action="/IBSng/admin/ras/edit_port.php" name=edit_port>
				<input type=hidden name=ras_ip value="{$info.ras_ip}">
		    Edit Port(s): <input type=text name=port_name> {multistr form_name="edit_port" input_name="port_name"}
				<input type=submit value=edit>
				</form>

	<tr>
	    <td>

		    <form method=POST action="/IBSng/admin/ras/ras_info.php">
			<input type=hidden name=ras_ip value="{$info.ras_ip}">
			Add IP pool To Ras: <select name="add_ip_pool">
						{html_options values=$ippool_names output=$ippool_names}
					    </select>
				<input type=submit value=add>					    
		    </form>

    </table>
{else}
    <input type=submit name=submit>
    </form>
{/if}

{include file="footer.tpl"}
