{* Add New IPPOOL
    ippool_name: new ippool_name
    comment: comment!
    
    Success: client will be redirected to the new ippool information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New IPPOOL"}
{include file="err_head.tpl"}

<form method=POST>
    {addEditTable title="Add New IPPool"}

	{addEditTD type="left" err="name_err"}
	    IPPool Name
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=ippool_name value="{$ippool_name}" class="text">
	    {helpicon subject='ippool name' category='ippool'}    
	{/addEditTD}
	
	{addEditTD type="left" err="ippool_comment_err" comment=TRUE}
	    Comment
	{/addEditTD}
	{addEditTD type="right" comment=TRUE}
	    <textarea name=comment class=text>{$comment|strip}</textarea>
	{/addEditTD}
	
    {/addEditTable}
</form>
{include file="admin_footer.tpl"}
