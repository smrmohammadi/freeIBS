{include file="admin_header.tpl" title="Setting" selected="Charge"}

<a href="charge">Charge</a>
<a href="misc">Misc</a>
<a href="ras">Ras</a>
<a href="ippool">IPpool</a>


{addRelatedLink}
    <a href="/IBSng/admin/charge/add_new_charge.php" class="RightSide_links">
	Add New Charge
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/ras/add_new_ras.php" class="RightSide_links">
	Add New RAS
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/ippool/add_new_ippool.php" class="RightSide_links">
	Add New IPpool
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/misc/show_ibs_defs.php" class="RightSide_links">
	Advanced Configuration	
    </a>
{/addRelatedLink}


{setAboutPage title="setting"}

{/setAboutPage}
{include file="admin_footer.tpl"}

