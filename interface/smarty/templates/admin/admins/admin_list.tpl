{* Admin List
    
*}
{include file="admin_header.tpl" title="Admin List" selected="Admin List"}
{include file="err_head.tpl"}
{listTable title="Admin List" cols_num=4}
	{listTableHeaderIcon action="view" close_tr=TRUE}
	{listTR type="header"}
	    {listTD}
		ID
	    {/listTD}
	    {listTD}
		Username
	    {/listTD}
	    {listTD}
		Name
	    {/listTD}
	    {listTD}
		Deposit
	    {/listTD}
	{/listTR}

		
	{section name=index loop=$admin_infos}
	    {listTR type="body"}
		{listTD}
		    {$admin_infos[index].admin_id}
    		{/listTD}
		{listTD}
		    {$admin_infos[index].username}
    		{/listTD}
		{listTD}
		    {$admin_infos[index].name}
    		{/listTD}
		{listTD}
		    {$admin_infos[index].deposit}
    		{/listTD}
		
		{listTD icon=TRUE}
		    <a style="text-decoration:none" href="/IBSng/admin/admins/admin_info.php?admin_username={$admin_infos[index].username|escape:"url"}">{listTableBodyIcon action="view" cycle_color="TRUE"}</a>
    		{/listTD}
		
	    {/listTR}
	{/section}
{/listTable}

{addRelatedLink}
    <a href="/IBSng/admin/admins/admin_list.php" class="RightSide_links">
	Admin List
    </a>
{/addRelatedLink}
{addRelatedLink}
    <a href="/IBSng/admin/admins/add_new_admin.php" class="RightSide_links">
	Add New Admin
    </a>
{/addRelatedLink}
{setAboutPage title="Admin List"}
A list of all admins are shown here.
{/setAboutPage}

{include file="admin_footer.tpl"}