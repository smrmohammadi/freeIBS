{include file="admin_header.tpl" title="Report" selected="Online Users""}

<table border=0 width="100%" height="100%" cellspacing=0 cellpadding=0>
    <tr>
	<td colspan=2 height=30>
	</td>
    </tr>	
    <tr>
	<td valign="center" align="center"> 
		{viewTable title="Internet Report" table_width="200" nofoot="TRUE" color="red" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		{/viewTable}
	</td>
	<td valign="center" align="center">
		{viewTable title="VoIP Report" table_width="200" nofoot="TRUE" color="green" arrow_color="white"}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		{/viewTable}
	</td>
    </tr>
</table>

{addRelatedLink}
    <a href="" class="RightSide_links">
	
    </a>
{/addRelatedLink}
{setAboutPage title="Report"}

{/setAboutPage}

{include file="admin_footer.tpl"}

