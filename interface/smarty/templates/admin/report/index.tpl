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
			<a href="/IBSng/admin/report/online_users.php" class="page_menu">Online Users</a>
		    {/menuTR}
		    {menuTR}
			<a href="/IBSng/admin/report/connections.php" class="page_menu">Connetion Logs</a>
		    {/menuTR}

		    {menuTR}
			<a href="/IBSng/admin/report/credit_change.php" class="page_menu">Credit Changes</a>
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
		    {menuTR}
			<a href="/IBSng/admin/" class="page_menu"></a>
		    {/menuTR}
		{/viewTable}
	</td>
    </tr>
</table>

{addRelatedLink}
    <a href="/IBSng/admin/report/online_users.php" class="RightSide_links">
	Online Users
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/report/connections.php" class="RightSide_links">
	Connetion Logs
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/report/credit_change.php" class="RightSide_links">
	Credit Changes
    </a>
{/addRelatedLink}

{setAboutPage title="Report"}

{/setAboutPage}

{include file="admin_footer.tpl"}

