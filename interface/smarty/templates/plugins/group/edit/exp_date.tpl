{include file="admin_header.tpl" title="Group Expiration Date Edit" selected="group list"}
{include file="err_head.tpl"}

{literal}
    <script language="javascript" src="/IBSng/js/dom_container.js"> </script>
    <script language="javascript">
	rel_exp_select=new DomContainer();
        rel_exp_select.setOnSelect("visibility","");
        rel_exp_select.setOnUnSelect("visibility","hidden");
    </script>
{/literal}

{editTemplate target="group" target_id=$group_name update_method="expDate" edit_tpl_name="exp_date.tpl"}


  {addEditTable title="Expiration Dates" table_width=300}
    {addEditTD type="left"}
	Has Relative Expiration Date
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="has_rel_exp" class=checkbox {if $group_attrs.has_rel_exp}checked{/if} onClick='rel_exp_select.toggle("rel_exp_date")'>
    {/addEditTD}

    {addEditTD type="left"}
	Relative Expiration Date
    {/addEditTD}

    {addEditTD type="right"}
	<input id="rel_exp_date" type=text name="rel_exp_date" value="{$group_attrs.rel_exp_date|default:""}" class=small_text > 
	{relative_units default=`$group_attrs.rel_exp_date_unit` name="rel_exp_date_unit" id="rel_exp_date_unit" }
	{$group_attrs.rel_exp_date_unit}
    {/addEditTD}

  {/addEditTable}
{/editTemplate}
<script language="javascript">
	rel_exp_select.addByID("rel_exp_date",Array("rel_exp_date_unit"));
{if $group_attrs.has_rel_exp}
    rel_exp_select.select("rel_exp_date");
{else}
    rel_exp_select.select(null);
{/if}
</script>

{include file="admin_footer.tpl"}