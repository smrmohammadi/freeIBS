{include file="admin_header.tpl" title="Normal Charge Edit" selected="Group List"}
{include file="err_head.tpl"}

{editTemplate target="group" target_id=$group_name update_method="normalCharge" edit_tpl_name="normal_charge.tpl"}

  {addEditTable title="Internet Charge" table_width=300}
    {addEditTD type="left"}
	Has Internet Charge
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="has_normal_charge" value="t" class=checkbox {if attrDefault($group_attrs,"normal_charge","has_normal_charge")!=""}checked{/if} onClick='normal_charge_select.toggle("normal_charge")'>
    {/addEditTD}

    {addEditTD type="left"}
	Normal Charge
    {/addEditTD}

    {addEditTD type="right"}
	{charge_names_select name="normal_charge" type="Internet" target="group" default_var="normal_charge" default_request="normal_charge" id="normal_charge"}
    {/addEditTD}

  {/addEditTable}
{/editTemplate}
<script language="javascript">
	normal_charge_select=new DomContainer();
	normal_charge_select.disable_unselected=true;
	normal_charge_select.addByID("normal_charge");
{if attrDefault($group_attrs,"normal_charge","has_normal_charge")!=""}
    normal_charge_select.select("normal_charge");
{else}
    normal_charge_select.select(null);
{/if}
</script>


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

{setAboutPage title="Internet Charge Edit"}
You can set internet charge, for users who are member of this group.
Internet charge is used for dialup and lan users.
{/setAboutPage}

{include file="admin_footer.tpl"}
