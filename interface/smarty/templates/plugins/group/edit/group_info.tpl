{include file="admin_header.tpl" title="Add New Admin" selected="Add Admin"}
{include file="err_head.tpl"}

<form method=POST action="/IBSng/admin/plugins/edit/group_info.php">
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
	<input type=text name="group_name" value="{$group_name}">
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
	<textarea name=comment>{$comment}</textarea>
    {/addEditTD}

    

{include file="admin_footer.tpl"}