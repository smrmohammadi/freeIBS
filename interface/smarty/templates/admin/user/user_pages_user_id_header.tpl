{viewTable title="User  Information" table_width="380" nofoot="TRUE"}

    {addEditTD type="left" comment=TRUE}
	User ID
    {/addEditTD}
    {addEditTD type="right" comment=TRUE}
	{$user_id|replace:",":", "|wordwrap:80:"<br>":true}
    {/addEditTD}

{/viewTable}
