{groupViewTemplate edit_tpl_name="normal_charge.tpl"}
  {groupInfoTable title="Normal Charge"}
    {groupInfoTD type="left"}
	    Normal Charge
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{ifHasAttr object="group" var_name="normal_charge"}
		    {$group_attrs.normal_charge}  
		{/ifHasAttr} 
		{helpicon subject="normal charge" category="user"}
    {/groupInfoTD}

  {/groupInfoTable}
{/groupViewTemplate}

