{userViewTemplate edit_tpl_name="user_info.tpl"}
  {addEditTable title="Basic User Informations" action_icon="edit"} 
    {addEditTD type="left"}
	User ID:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.user_id}
    {/addEditTD}

    {addEditTD type="left"}
	Group Name:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.group_name}
    {/addEditTD}

    {addEditTD type="left"}
	Credit:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.credit|price}
    {/addEditTD}

    {addEditTD type="left"}
	Owner Admin:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.owner_name}
    {/addEditTD}
  
    {addEditTD type="left"}
	Creation Date:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.creation_date}
    {/addEditTD}

  {/addEditTable}
{/userViewTemplate}
