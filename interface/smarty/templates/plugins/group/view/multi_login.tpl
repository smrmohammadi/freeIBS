{groupViewTemplate edit_tpl_name="/plugins/group/edit/multi_login.tpl"}
  {groupInfoTable title="Multi Login"}
    {groupInfoTD type="left"}
	    Multi Login
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{ifHasAttr object="group" var_name="multi_login"}
		    {$multi_login} instances 
		{/ifHasAttr} 
		{helpicon subject="multi login" category="user"}
    {/groupInfoTD}

  {/groupInfoTable}
{/groupViewTemplate}

