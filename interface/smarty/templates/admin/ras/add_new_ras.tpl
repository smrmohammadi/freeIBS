{* Add New Ras
    ras_ip: new ras ip
    ras_type: type of new ras
    redaius_secret: 
    
    Success: client will be redirected to the new ras information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Ras" selected="RAS"}
{include file="err_head.tpl"}

<form method=POST>
    {addEditTable title="Add New RAS"}

	{addEditTD type="left" err="ras_ip_err"}
	    RAS IP
	{/addEditTD}
	{addEditTD type="right"}
	    	<input class="text" type=text name=ras_ip value="{$ras_ip}">
	    	{helpicon subject="ras ip" category="ras"}
	{/addEditTD}

	{addEditTD type="left" err="ras_type_err"}
	    RAS Type
	{/addEditTD}
	{addEditTD type="right"}
		<select name=ras_type>
		    {html_options output=$ras_types values=$ras_types default=$ras_type}
		</select>
		{helpicon subject="ras type" category="ras"}
	{/addEditTD}

	{addEditTD type="left" err="radius_secret_err"}
	    Radius Secret
	{/addEditTD}
	{addEditTD type="right"}
	    	<input class="text" type=text name=radius_secret value="{$radius_secret}">
		{helpicon subject="radius secret" category="ras"}

	{/addEditTD}
	
    {/addEditTable}

</form>
{addRelatedLink}
    <a href="/IBSng/admin/ras/ras_list.php" class="RightSide_links">
	RAS List
     </a>
{/addRelatedLink}

{setAboutPage title="Add New RAS"}

{/setAboutPage}

{include file="admin_footer.tpl"}
