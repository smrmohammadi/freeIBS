{viewTable title="User  Information" table_width="380" nofoot="TRUE"}

    {addEditTD type="left"}
	User ID
    {/addEditTD}
    {addEditTD type="right"}
	{$user_id|replace:",":", "|wordwrap:80:"<br>":true}
    {/addEditTD}

{/viewTable}
