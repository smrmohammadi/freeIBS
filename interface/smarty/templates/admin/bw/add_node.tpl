{* Add Node
    limit_kbits: limit this node bandwidth
    
    interface_name: interface_name we're adding node to
    parent_id: id of parent onde
    
    Success: client will be redirected to the interface information page
    Failure: this page is shown again with error message at top of the page
*}
{include file="admin_header.tpl" title="Add New Node" selected="Bandwidth"}
{include file="err_head.tpl"}

<form method=POST>
    {addEditTable title="Add Node" action_icon="add"}

	{addEditTD type="left" err="interface_name_err"}
	    Interface
	{/addEditTD}

	{addEditTD type="right"}
	    {$interface_name}
	    <input type=hidden name=interface_name value="{$interface_name}">
	    {helpicon subject='interface name' category='bandwidth'}
	{/addEditTD}

	{addEditTD type="left" err="parent_id_err"}
	    Parent Node ID
	{/addEditTD}

	{addEditTD type="right"}
	    {$parent_id}
    	    <input type=hidden name=parent_id value="{$parent_id}">
	    {helpicon subject='Parent Node' category='bandwidth'}
	{/addEditTD}



	{addEditTD type="left" err="limit_kbits_err"}
	    Bandwidth Limit
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=limit_kbits value="{ifisinrequest name="limit_kbits"}" class="text"> kbit/s
	    {helpicon subject='node limit kbits' category='bandwidth'}
	{/addEditTD}
	
    {/addEditTable}
</form>
{addRelatedLink}
    <a href="/IBSng/admin/bw/interface_list.php" class="RightSide_links">
	Interface list
    </a>
{/addRelatedLink}

{setAboutPage title="Add Node"}

{/setAboutPage}

{include file="admin_footer.tpl"}
