{listTable title="Internet Online Users" cols_num=10}
    {listTableHeaderIcon action="kick"}
    {listTableHeaderIcon action="clear"}
    {listTableHeaderIcon action="details" close_tr=TRUE}
    {listTR type="header"}
	{listTD}
	    {sortableHeader name="user_id"} 
		User ID
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="normal_username"} 
		Username
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="login_time_epoch" default=TRUE default_desc=TRUE}
		Login Time
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="duration_secs"}
		Duration
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="current_credit"} 
		Credit
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="ras_ip"} 
		Ras IP
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="unique_id_val"} 
	        Port/ID
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="in_bytes"} 
		In Bytes
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="out_bytes"} 
		Out Bytes
	    {/sortableHeader}
	{/listTD}

	{listTD}
	    {sortableHeader name="owner_name"} 
		Owner
	    {/sortableHeader}
	{/listTD}
    {/listTR}
    {foreach from=$onlines item=info_dic}
	{if $info_dic.service eq "Normal"}
	
	{listTR type="body" hover_location="/IBSng/admin/user/user_info.php?user_id=`$info_dic.user_id`"}
	    {listTD}
		<a href="/IBSng/admin/user/user_info.php?user_id={$info_dic.user_id}">
		    {$info_dic.user_id}
		</a>
	    {/listTD}

	    {listTD}
		{$info_dic.normal_username}
	    {/listTD}

	    {listTD}
		{$info_dic.login_time}
	    {/listTD}

	    {listTD}
		{$info_dic.duration_secs|duration}
	    {/listTD}

	    {listTD}
		{$info_dic.current_credit|price}
	    {/listTD}


	    {listTD}
		{$info_dic.ras_ip}
	    {/listTD}

	    {listTD}
		{$info_dic.unique_id_val}
	    {/listTD}

	    {listTD}
		{$info_dic.in_bytes}
	    {/listTD}

	    {listTD}
		{$info_dic.out_bytes}
	    {/listTD}

	    {listTD}
		{$info_dic.owner_name}
	    {/listTD}

	    {listTD icon=TRUE extra="onClick='event.cancelBubble=true;'"}
		    <a style="text-decoration:none" href="javascript: killUser('{$info_dic.user_id}','{$info_dic.normal_username}','{$info_dic.ras_ip}','{$info_dic.unique_id_val}',true);" {jsconfirm}>
			{listTableBodyIcon action="kick" cycle_color="TRUE"}
		    </a>
	    {/listTD}

	    {listTD icon=TRUE extra="onClick='event.cancelBubble=true;'"}
		    <a style="text-decoration:none" href="javascript: killUser('{$info_dic.user_id}','{$info_dic.normal_username}','{$info_dic.ras_ip}','{$info_dic.unique_id_val}',false);" {jsconfirm}>
			{listTableBodyIcon action="clear" cycle_color="TRUE"}
		    </a>
	    {/listTD}

	    {listTD icon=TRUE extra="onClick='event.cancelBubble=true;'" cycle_color="TRUE"}
		    
		<a onClick="showReportLayer('{$info_dic.ras_ip}_{$info_dic.unique_id_val}',this); return false;" href="#">
		    {listTableBodyIcon action="details" }
		</a>
		{reportDetailLayer name=`$info_dic.ras_ip`_`$info_dic.unique_id_val` title="Report Details"}
		    {layerTable}
		    {foreach from=`$info_dic.attrs` key=key item=item}
    			{layerTR cycle_color=TRUE}
			    {listTD}
				{$key}
	    		    {/listTD}
			    {listTD}
				{$item}
	    		    {/listTD}
			{/layerTR}
		    {/foreach}
		    {/layerTable}
		{/reportDetailLayer}
	    {/listTD}
	{/listTR}
	
	{/if}
    {/foreach}

{/listTable}
