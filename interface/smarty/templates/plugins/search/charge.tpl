{counter name="charge_search_id" start=0 print=false}

    {foreach from=$charge_names item=charge_name key=index}

        {if $index%4==0}
	    {multiTableTR}
        {/if}

	{counter name="charge_search_id" assign="charge_search_id"}
	{multiTableTD type="left"}
    	    <input name="charge_name_{$charge_search_id}" value="{$charge_name}" type=checkbox {ifisinrequest name="charge_name_`$charge_search_id`" value="checked"}> 
	{/multiTableTD}
	{multiTableTD type="right" width="25%"}
	    {$charge_name}
	{/multiTableTD}
    {/foreach}
    {multiTablePad last_index=$index go_until=4 width="25%"}
</tr><tr><td colspan=30 height=1 bgcolor="#FFFFFF"></td></tr>
