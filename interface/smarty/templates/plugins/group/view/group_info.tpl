{groupViewTemplate edit_tpl_name="/plugins/group/edit/group_info.tpl"}
  {groupInfoTable title="Group Informations"}
    {groupInfoTD type="left"}
		Group ID
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{$group_id}
    {/groupInfoTD}

    {groupInfoTD type="left"}
		Group Name
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{$group_name}
    {/groupInfoTD}

    {groupInfoTD type="left"}
		Owner Name
    {/groupInfoTD}
    {groupInfoTD type="right"}
		{$owner_name}
    {/groupInfoTD}

    {groupInfoTD type="left" comment=TRUE}
		Comment
    {/groupInfoTD}
    {groupInfoTD type="right" comment=TRUE}
		{$comment}
    {/groupInfoTD}
  {/groupInfoTable}
{/groupViewTemplate}
