{include file="admin_header.tpl" title="Add New Admin" selected="Add Admin"}
{include file="err_head.tpl"}

{editTemplate target="group" target_id=$group_name update_method="groupInfo" edit_tpl_name="group_info.tpl"}
<input type="hidden" name="group_id" value="{$group_id}">
{addEditTable title="Group Information"}
    {addEditTD type="left"}
	Group ID
    {/addEditTD}

    {addEditTD type="right"}
	{$group_id}
    {/addEditTD}

    {addEditTD type="left"}
	Group Name
    {/addEditTD}

    {addEditTD type="right"}
	<input class=text type=text name="group_name" value="{$group_name}">
    {/addEditTD}

    {addEditTD type="left"}
	Owner Name
    {/addEditTD}

    {addEditTD type="right"}
	{if canDo("SEE ADMIN INFO")}
	    {admin_names_select name=owner_name default=$owner_name}
	{else}
	    <input type=hidden name="owner_name" value="{$owner_name}">
	    {$owner_name}
	{/if}
	
    {/addEditTD}

    {addEditTD type="left" comment=TRUE}
	Comment
    {/addEditTD}

    {addEditTD type="right" comment=TRUE}
	<textarea name=comment class=text>{$comment|strip}</textarea>
    {/addEditTD}
{/addEditTable}
{/editTemplate}

{include file="admin_footer.tpl"}