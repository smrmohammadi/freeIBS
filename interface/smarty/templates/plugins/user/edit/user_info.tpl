{editTemplate target="group" target_id=$user_id update_method="userInfo" edit_tpl_name="user_info.tpl"}
  {addEditTable title="Basic User Informations" } 
    {addEditTD type="left"}
	User ID:
    {/addEditTD}

    {addEditTD type="right"}
	{$user_id}
    {/addEditTD}

    {addEditTD type="left"}
	Group Name:
    {/addEditTD}

    {addEditTD type="right"}
	{if $is_single}
	    {group_names_select name="group_name" default=`$user_info.basic_info.group_name` default_request="group_name"}
	{else}
	    {group_names_select name="group_name" default_request="group_name"}
	{/if}
    {/addEditTD}

    {addEditTD type="left"}
	Owner Admin:
    {/addEditTD}

    {addEditTD type="right"}
	{if canDo("CHANGE USERS OWNER")}
	    {if $is_single}
    		{admin_names_select name="owner_name" default=`$user_info.basic_info.owner_name` default_request="owner_name"}
	    {else}
		{admin_names_select name="owner_name" default_request="owner_name"}	    
	    {/if}
	{else}
	    <input type=hidden name="owner_name" value="">
    {/addEditTD}

  {/addEditTable}
{/userViewTemplate}
