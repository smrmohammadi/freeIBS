{* 
*}

{include file="admin_header.tpl" title="Connection Logs" selected="Connection Logs"} 
{include file="err_head.tpl"} 
{include file="util/calendar.tpl"}

<form method=POST action="connections.php" name="connections">
<input type=hidden name=show value=1>
<input type=hidden name=page value=1>

{addEditTable double=TRUE title="Connection Log Conditions"}
    {addEditTD type="left1" double=TRUE}
	User IDs
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=text class=text name=user_ids value="{ifisinrequest name="user_ids"}"> {multistr input_name="user_ids" form_name="connections"}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Owner
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{admin_names_select name="owner" default="All" default_request="owner" add_all=TRUE}
    {/addEditTD}


    {addEditTD type="left1" double=TRUE}
	Login Time From
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{absDateSelect name="login_time_from" default_request="login_time_from"}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Login Time To
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{absDateSelect name="login_time_to" default_request="login_time_to"}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Logout Time From
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{absDateSelect name="logout_time_from" default_request="logout_time_from"}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Logout Time To
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{absDateSelect name="logout_time_to" default_request="logout_time_to"}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Successful Logins
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{html_options name="successful" values=$successful_options output=$successful_options selected=$successful_default}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Service
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{html_options name="service" values=$services output=$services selected=$services_default}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Credit Used
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{op class="ltgteq" name="credit_used_op" selected="credit_used_op"}
	<input type=text class=text name=credit_used value="{ifisinrequest name="credit_used"}"> {$MONEY_UNIT}
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Show Total Credit
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=checkbox class=checktext name=show_total_credit_used {checkBoxValue name="show_total_credit_used"}>
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Show Total Duration
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	<input type=checkbox class=checktext name=show_total_duration {checkBoxValue name="show_total_duration"}>
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

    {addEditTD type="left" double=TRUE comment=TRUE}
	Rases
    {/addEditTD}

    <td class="Form_Content_Row_right_Textarea_2col" valign="top" colspan="7">
    	{rasCheckBoxes prefix="ras"}
    </td></tr>
    <tr>
	<td colspan="9" class="Form_Content_Row_Space"></td>
    </tr>


{/addEditTable}

</form>
{if isInRequest("show")}

<a name="show_results"></a>
{listTable title="Connection Logs" cols_num=8}
    {listTableHeaderIcon action="details" close_tr=TRUE}
    {listTR type="header"}
	{listTD}
	    User ID
	{/listTD}

	{listTD}
	    Login Time
	{/listTD}

	{listTD}
	    Logout Time
	{/listTD}

	{listTD}
	    Duration
	{/listTD}

	{listTD}
	    Credit Used
	{/listTD}

	{listTD}
	    Successful
	{/listTD}

	{listTD}
	    Service
	{/listTD}

	{listTD}
	    Ras IP
	{/listTD}

    {/listTR}

  {assign var="page_total_credit" value=0}
  {assign var="page_total_duration" value=0}

  {foreach from=$report item=row}
	{listTR type="body"}
	    {listTD}
		<a class="link_in_body" href="/IBSng/admin/user/user_info.php?user_id={$row.user_id|escape:"url"}">
		    {$row.user_id}
		</a>
	    {/listTD}

	{listTD}
	    {$row.login_time_formatted}
	{/listTD}

	{listTD}
	    {$row.logout_time_formatted}
	{/listTD}

	{listTD}
	    {math equation="x + y" assign=page_total_duration x=`$row.duration_seconds` y=$page_total_duration}
	    {$row.duration}
	{/listTD}

	{listTD}
	    {math equation="x + y" assign=page_total_credit x=`$row.credit_used` y=$page_total_credit}
	    {$row.credit_used|price}
	{/listTD}

	{listTD}
	    {eval var=`$row.successful` assign="successful"}
	    {if $successful ==  "t"}
		Yes
	    {else}
		No
	    {/if}
	{/listTD}

	{listTD}
	    {$row.service_type}
    	{/listTD}

	{listTD}
	    {$row.ras_ip}
	{/listTD}

	{listTD icon=TRUE}
    	    <a onClick="showReportLayer('{$row.connection_log_id}',this); return false;" href="#">
		{listTableBodyIcon cycle_color=TRUE action="details"}
	    </a>
		{reportDetailLayer name=`$row.connection_log_id` title="Report Details"}
		    {layerTable}
			{foreach from=`$row.details` item=tuple}
	    		    {layerTR cycle_color=TRUE}
				{listTD}
				    {$tuple[0]}:
				{/listTD}
				{listTD}
				    {$tuple[1]}
				{/listTD}
			{/layerTR}
		    {/foreach}
		    {/layerTable}
		{/reportDetailLayer}
	{/listTD}
	
    {/listTR}
  {/foreach}


{/listTable}

{listTable title=Totals cols_num=2}
	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		<b>Page</b> Total Credit Used:
    	    {/listTD}
	    {listTD}
	        {$page_total_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}

	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		<b>Page</b> Total Duration:
    	    {/listTD}
	    {listTD}
	        {$page_total_duration|duration}
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


    {if isInRequest("show_total_credit_used")}
	{listTR type="body" cycle_color=TRUE}
	    {listTD}
		Total Credit Used:
    	    {/listTD}
	    {listTD}
	        {$total_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}
    {/if}

    {if isInRequest("show_total_duration")}
	{listTR type="body" cycle_color=TRUE}
	    {listTD}
    		Total Duration: 
	    {/listTD}
	    {listTD}
	        {$total_duration}
	    {/listTD}
	{/listTR}
    {/if}
{/listTable}

{reportPages total_results=$total_rows}


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
    <a href="/IBSng/admin/report/credit_change.php" class="RightSide_links">
	Credit Changes
    </a>
{/addRelatedLink}


{setAboutPage title="Connection Log"}
    
{/setAboutPage}


{include file="admin_footer.tpl"}