{viewTable title="Basic User Informations"} 
    {addEditTD type="left"}
	User ID:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.user_id}
    {/addEditTD}

    {addEditTD type="left"}
	Credit:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.credit|price}
    {/addEditTD}

    {addEditTD type="left"}
	{if $can_change} {editCheckBox edit_tpl_name="group_name"} {/if}
	Group Name:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_info.basic_info.group_name}
    {/addEditTD}

    {addEditTD type="left"}
	{if $can_change and canDo("CHANGE USERS OWNER")} {editCheckBox edit_tpl_name="owner_name"} {/if}
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

{/viewTable}
