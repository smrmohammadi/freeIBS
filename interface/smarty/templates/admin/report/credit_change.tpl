{include file="admin_header.tpl" title="Credit Change Report" selected="Credit Change"} 
{include file="err_head.tpl"} 
{include file="util/calendar.tpl"}

<form method=POST action="credit_change.php" name="credit_change">
<input type=hidden name=show value=1>
<input type=hidden name=page value=1>

{addEditTable double=TRUE title="Credit Change Conditions"}
    {addEditTD type="left1" double=TRUE}
	User IDs
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=text class=text name=user_ids value="{ifisinrequest name="user_ids"}"> {multistr input_name="user_ids" form_name="credit_change"}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Issuer Admin
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{admin_names_select name="admin" default="All" default_request="admin" add_all=TRUE}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Change Time From
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{absDateSelect name="change_time_from" default_request="change_time_from"}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Change Time To
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{absDateSelect name="change_time_to" default_request="change_time_to"}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Per User Credit Change
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{op class="ltgteq" name="per_user_credit_op" selected="per_user_credit_op"}
	<input type=text class=text name=per_user_credit credit value="{ifisinrequest name="per_user_credit"}"> {$MONEY_UNIT}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Admin Credit Consumed
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{op class="ltgteq" name="admin_credit_op" selected="admin_credit_op"}
	<input type=text class=text name=admin_credit credit value="{ifisinrequest name="admin_credit"}"> {$MONEY_UNIT}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Actions
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{html_options name="action" options=$actions selected=$actions_default}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	IP Address Of Admin
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	<input type=text class=text name=remote_addr value="{ifisinrequest name="remote_addr"}"> {multistr input_name="remote_addr" form_name="credit_change"}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Show Total Per User Credit
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=checkbox class=checktext name=show_total_per_user_credit {checkBoxValue name="show_total_per_user_credit"}>
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Show Total Admin Consumed Credit
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	<input type=checkbox class=checktext name=show_total_admin_credit {checkBoxValue name="show_total_admin_credit"}>
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Sort By
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{html_options name="order_by" options=$order_bys selected=$order_by_default} 
	Desc <input name=desc type=checkbox {checkBoxValue name="desc" default_checked=TRUE always_in_form="show"}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Result Per Page
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{reportRPP}
    {/addEditTD}

{/addEditTable}
</form>

{if isInRequest("show")}

<a name="show_results"></a>
{listTable title="Credit Changes" cols_num=5}
    {listTableHeaderIcon action="details" close_tr=TRUE}
    {listTR type="header"}
	{listTD}
	    Date
	{/listTD}

	{listTD}
	    Action
	{/listTD}

	{listTD}
	    Issuer Admin
	{/listTD}

	{listTD}
	    Per User Credit
	{/listTD}

	{listTD}
	    Admin Credit Consumed
	{/listTD}
    {/listTR}

  {assign var="page_total_per_user_credit" value=0}
  {assign var="page_total_admin_credit" value=0}

  {foreach from=$report item=row}
    {listTR type="body"}
	{listTD}
	    {$row.change_time_formatted}
	{/listTD}

	{listTD}
	    {$row.action_text}
	{/listTD}

	{listTD}
	    <a href="/IBSng/admin/admins/admin_info.php?admin_username={$row.admin_name}">
	        {$row.admin_name}
	    </a>
	{/listTD}

	{listTD}
	    {$row.per_user_credit|price}
	    {math equation="x + y" assign=page_total_per_user_credit x=`$row.per_user_credit` y=$page_total_per_user_credit}
	{/listTD}

	{listTD}
	    {$row.admin_credit|price}
	    {math equation="x + y" assign=page_total_admin_credit x=`$row.admin_credit` y=$page_total_admin_credit}
	{/listTD}

	{listTD icon=TRUE}
    	    <a onClick="showReportLayer('{$row.credit_change_id}',this); return false;" href="#">
		{listTableBodyIcon cycle_color=TRUE action="details"}
	    </a>
		{reportDetailLayer name=`$row.credit_change_id` title="Report Details"}
		    Comment: {$row.comment} <br>
		    Admin IP Address: {$row.remote_addr} <br>
		    User IDs: {arrayJoin array=`$row.user_ids` glue=", "}
		{/reportDetailLayer}
	{/listTD}
	
    {/listTR}
  {/foreach}
    
{/listTable}    

{listTable title=Totals cols_num=2}
	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		<b>Page</b> Total Per User Credit:
    	    {/listTD}
	    {listTD}
	        {$page_total_per_user_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}

	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		<b>Page</b> Total Admin Consumed Credit:
    	    {/listTD}
	    {listTD}
	        {$page_total_admin_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}

	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		Total Number Of Rows:
    	    {/listTD}
	    {listTD}
	        {$total_rows} 
	    {/listTD}

	{/listTR}

    {if isInRequest("show_total_per_user_credit")}
	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		Total Per User Credit:
    	    {/listTD}
	    {listTD}
	        {$total_per_user_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}
    {/if}

    {if isInRequest("show_total_admin_credit")}
	{listTR type="body" cycle_color=TRUE}
	    {listTD}
    		Total Admin Credit: 
	    {/listTD}
	    {listTD}
	        {$total_admin_credit|price } {$MONEY_UNIT}
	    {/listTD}
	{/listTR}
    {/if}
{/listTable}


{/if}

{if requestVal("user_ids") ne ""}
    {addRelatedLink}
	<a href="/IBSng/admin/user/user_info.php?user_id_multi={$smarty.request.user_ids}" class="RightSide_links">
	    User <b>{$smarty.request.user_ids|truncate:15}</b> Info
        </a>
    {/addRelatedLink}

{/if}


{addRelatedLink}
    <a href="/IBSng/admin/report/online_users.php" class="RightSide_links">
	Online Users
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/report/connctions.php" class="RightSide_links">
	Connection Logs
    </a>
{/addRelatedLink}


{setAboutPage title="Credit Change"}
    
{/setAboutPage}


{include file="admin_footer.tpl"}