{* Add New Interface
    interface_name: new ippool_name
    comment: comment!
    
    Success: client will be redirected to the new interface information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Interface" selected="Bandwidth"}
{include file="err_head.tpl"}

<form method=POST>
    {addEditTable title="Add Interface" action_icon="add"}

	{addEditTD type="left" err="interface_name_err"}
	    Interface 
	{/addEditTD}

	{addEditTD type="right"}
	    <input type=text name=interface_name value="{ifisinrequest name="interface_name"}" class="text">
	    {helpicon subject='interface name' category='bandwidth'}
	{/addEditTD}
	
	{addEditTD type="left" err="comment_err" comment=TRUE}
	    Comment
	{/addEditTD}
	{addEditTD type="right" comment=TRUE}
	    <textarea name=comment class=text>{ifisinrequest name="comment"|strip}</textarea>
	{/addEditTD}
	
    {/addEditTable}
</form>
{addRelatedLink}
    <a href="/IBSng/admin/bw/interface_list.php" class="RightSide_links">
	Interface list
    </a>
{/addRelatedLink}

{setAboutPage title="Add Interface"}

{/setAboutPage}

{include file="admin_footer.tpl"}
