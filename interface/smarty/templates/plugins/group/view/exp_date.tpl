{groupViewTemplate edit_tpl_name="/plugins/group/edit/exp_date.tpl"}
  {groupInfoTable title="Expiration Date"}
    {groupInfoTD type="left"}
	    Relative Expiration Date 
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{ifhasattr object="group" var_name="has_rel_exp"}
		    {$rel_exp_date} {$rel_exp_date_unit}
		{/ifhasattr}
    {/groupInfoTD}

  {/groupInfoTable}
{/groupViewTemplate}

