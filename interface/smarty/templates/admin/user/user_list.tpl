Total Results: <b> {$result_count} </b>
{listTable title="List of Users" cols_num=20}
    {listTR type="header" }
	{listTD}
	    User ID
	{/listTD}
    {if isInRequest("show__normal_username")}
	{listTD}
	    Normal Username
	{/listTD}
    {/if}
    
    {if isInRequest("show__credit")}
	{listTD}
	    Credit
	{/listTD}
    {/if}

    {if isInRequest("show__group")}
	{listTD}
	    Group
	{/listTD}
    {/if}

    {if isInRequest("show__owner")}
	{listTD}
	    Owner
	{/listTD}
    {/if}

    {if isInRequest("show__creation_date")}
	{listTD}
	    Creation Date
	{/listTD}
    {/if}

    {if isInRequest("show__rel_exp_date")}
	{listTD}
	    Rel Exp Date
	{/listTD}
    {/if}

    {if isInRequest("show__multi_login")}
	{listTD}
	    Multi Login
	{/listTD}
    {/if}

    {if isInRequest("show__normal_charge")}
	{listTD}
	    Normal Charge
	{/listTD}
    {/if}

    {/listTR}

    {foreach from=$user_infos item=user_info key=user_id}
	{listTR type="body"}
	    {listTD}
		{$user_id}
	    {/listTD}	
	
	    {if isInRequest("show__normal_username")}
	    	{searchUserTD attr_name="normal_username" user_id=$user_id attr_type="attrs"}{/searchUserTD}
	    {/if}
    
	    {if isInRequest("show__credit")}
		{searchUserTD attr_name="credit" user_id=$user_id attr_type="basic"}{$search_value|price}{/searchUserTD}
	    {/if}

	    {if isInRequest("show__group")}
		{searchUserTD attr_name="group_name" user_id=$user_id attr_type="basic"}{/searchUserTD}
	    {/if}

	    {if isInRequest("show__owner")}
		{searchUserTD attr_name="owner_name" user_id=$user_id attr_type="basic"}{/searchUserTD}
	    {/if}

	    {if isInRequest("show__creation_date")}
		{searchUserTD attr_name="creation_date" user_id=$user_id attr_type="basic"}{/searchUserTD}
	    {/if}

	    {if isInRequest("show__rel_exp_date")}
	    	{searchUserTD attr_name="rel_exp_date" user_id=$user_id attr_type="attrs"}{/searchUserTD}
	    {/if}

	    {if isInRequest("show__multi_login")}
	    	{searchUserTD attr_name="multi_login" user_id=$user_id attr_type="attrs"}{/searchUserTD}
	    {/if}

	    {if isInRequest("show__normal_charge")}
	    	{searchUserTD attr_name="normal_charge" user_id=$user_id attr_type="attrs"}{/searchUserTD}
	    {/if}
	    
	{/listTR}	
    {/foreach}
{/listTable}
