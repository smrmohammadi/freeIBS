{include file="admin_header.tpl" title="Edit Attributes"}
{include file="err_head.tpl"}
<form method=POST action="edit_attr.php">
    <input type=hidden name=target value="{$target}">
    <input type=hidden name=target_id value="{$target_id}">
    <input type=hidden name=update value="true">
    {if isset($template_file) and $template_file != ""}
	<input type=hidden name=template_name value="{$template_name}">
	{include file=$template_file}
    {/if}
</form>