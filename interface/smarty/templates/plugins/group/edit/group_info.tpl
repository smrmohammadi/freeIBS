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
	<input class=text type=text name="group_name" value="{ifisinrequest name="group_name" default_var="group_name"}">
    {/addEditTD}

    {addEditTD type="left"}
	Owner Name
    {/addEditTD}

    {addEditTD type="right"}
	{if canDo("SEE ADMIN INFO")}
	    {admin_names_select name=owner_name default_request="owner_name" default="owner_name" }
	{else}
	    <input type=hidden name="owner_name" value="{$owner_name}">
	    {$owner_name}
	{/if}
	
    {/addEditTD}

    {addEditTD type="left" comment=TRUE}
	Comment
    {/addEditTD}

    {addEditTD type="right" comment=TRUE}
	<textarea name=comment class=text>{strip}{ifisinrequest name="comment" default_var="comment"}{/strip}</textarea>
    {/addEditTD}
{/addEditTable}
{/editTemplate}

{addRelatedLink}
    <a href="/IBSng/admin/group/group_list.php" class="RightSide_links">
	Group List
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/group/group_info.php?group_name={$group_name}" class="RightSide_links">
	{$group_name} Group Info
    </a>
{/addRelatedLink}

{setAboutPage title="Expiration Date Edit"}
Basic group informations can be changed here. Also owner of group is changable if you have relevant permission.
{/setAboutPage}



{include file="admin_footer.tpl"}