{include file="admin_header.tpl" title="Expiration Dates Edit" selected="Group List"}
{include file="err_head.tpl"}

{editTemplate target="group" target_id=$group_name update_method="expDate" edit_tpl_name="exp_date.tpl"}


  {addEditTable title="Expiration Dates" table_width=300}
    {addEditTD type="left"}
	Has Relative Expiration Date
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="has_rel_exp" value="t" class=checkbox {if attrDefault($group_attrs,"rel_exp_date","has_rel_exp")!=""}checked{/if} onClick='rel_exp_select.toggle("rel_exp_date")'>
    {/addEditTD}

    {addEditTD type="left"}
	Relative Expiration Date
    {/addEditTD}

    {addEditTD type="right"}
	<input id="rel_exp_date" type=text name="rel_exp_date" value="{attrDefault target="group" default_var="rel_exp_date" default_request="rel_exp_date"}" class=small_text > 
	{relative_units name="rel_exp_date_unit" id="rel_exp_date_unit" default_var="rel_exp_date_unit" default_request="rel_exp_date_unit" target="group"}
    {/addEditTD}

  {/addEditTable}
{/editTemplate}

<script language="javascript">
	rel_exp_select=new DomContainer();
	rel_exp_select.disable_unselected=true;
	rel_exp_select.addByID("rel_exp_date",Array("rel_exp_date_unit"));
{if attrDefault($group_attrs,"rel_exp_date","has_rel_exp")!=""}
    rel_exp_select.select("rel_exp_date");
{else}
    rel_exp_select.select(null);
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

{setAboutPage title="Expiration Date Edit"}
You can set expiration date, for users who are member of this group.
{/setAboutPage}

{include file="admin_footer.tpl"}
