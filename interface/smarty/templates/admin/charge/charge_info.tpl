{* Charge Info
    Shows one charge information, including charge rules
    on fatal errors that no info can be shown, client is redirected to admin_list
    else error is shown on top of page
    
    Variables:
    $is_editing
    
    $charge_name
    $charge_id
    $charge_types
    $charge_type
    $visible_to_all_checked
    $visible_to_all
    $creator
    $comment
    
*}
{include file="admin_header.tpl" title="Charge Information"}
{include file="err_head.tpl"}

<center>
{if isset($update_success) and $update_success}
    <span class="message">
	Charge Updated Successfully.
    </span>        
{/if}

{if isset($del_charge_rule_success) and $del_charge_rule_success}
    <span class="message">
	Charge Rule Deleted Successfully.
    </span>        
{/if}


{if isInRequest("update_charge_rule_success") }
    <span class="message">
	Charge Rule Updated Successfully.
    </span>        
{/if}



{if $is_editing}
    <form action="/IBSng/admin/charge/charge_info.php" method=POST>
    <input name=charge_id value="{$charge_id}" type=hidden>
    <input name=old_charge_name value="{$charge_name}" type=hidden>
{/if}

<table>
    <tr>
	<td>
	    Charge Name:
	<td>
	    {if $is_editing}
		<input type=text name=charge_name value="{$charge_name}">
	    {else}
        	{$charge_name}
	    {/if}
	<td>
	    Charge ID:
	<td>
	    {$charge_id}
    <tr>
	<td>
	    Charge Type:
	<td>
		{$charge_type}
	<td>
	    Visible To All:
	<td>
	    {if $is_editing}
		<input type=checkbox name=visible_to_all {$visible_to_all_checked}>
	    {else}
		{$visible_to_all}
	    {/if}

    <tr>
	<td>
	    Comment:
	<td>
	    {if $is_editing}
		<textarea name=comment>{$comment|strip}</textarea>
	    {else}
		{$comment}
	    {/if}
	<td>
	    Creator Admin:
	<td>
	    {$creator}
	    
</table>

{if $is_editing}
    <input type=submit value=change>
    </form>
{/if}

{if not $is_editing}
    {if $charge_type eq "Internet"}
	{include file="admin/charge/internet_charge_rule_list.tpl"}
    {else}
    
    {/if}

{/if}

{if not $is_editing and $can_change}
    {addRelatedLink}
        <a href="/IBSng/admin/charge/charge_info.php?charge_name={$charge_name|escape:"url"}&edit=1" class="RightSide_links">
        	Edit Charge Information
        </a>
    {/addRelatedLink}
    {addRelatedLink}
        <a href="/IBSng/admin/charge/{if $charge_type eq "Internet"}add_internet_charge_rule{else}add_voip_charge_rule{/if}.php?charge_name={$charge_name|escape:"url"}" class="RightSide_links">
        	Add Charge Rule
        </a>
    {/addRelatedLink}

{/if}
{include file="admin_footer.tpl"}
