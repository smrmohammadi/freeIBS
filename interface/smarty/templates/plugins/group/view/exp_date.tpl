{groupViewTemplate edit_tpl_name="exp_date.tpl"}
  {groupInfoTable title="Expiration Date"}
    {groupInfoTD type="left"}
	    Relative Expiration Date 
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{ifHasAttr object="group" var_name="rel_exp_date"}
		    {$group_attrs.rel_exp_date} {$group_attrs.rel_exp_date_unit} 
		{/ifHasAttr}
		{helpicon subject="relative expiration date" category="user"}		
    {/groupInfoTD}

  {/groupInfoTable}
{/groupViewTemplate}

