{* 
*}

{include file="admin_header.tpl" title="Connection Logs" selected="Connection Logs"} 
{include file="err_head.tpl"} 

<form method=POST>
<input type=hidden name=show value=1>
{addEditTable double=TRUE title="Connection Log Conditions"}
    {addEditTD type="left1" double=TRUE}
	User IDs
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=text class=text name=user_ids value="{ifisinrequest name="user_ids"}">
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Owner
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	{admin_names_select name="owner" default="All" default_request="owner" add_all=TRUE}
    {/addEditTD}


    {addEditTD type="left1" double=TRUE}
	Login Time
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=text class=text name=login_time value="{ifisinrequest name="login_time"}">
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Logout Time
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	<input type=text class=text name=logout_time value="{ifisinrequest name="logout_time"}">
    {/addEditTD}


    {addEditTD type="left1" double=TRUE}
	Credit Used
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	{op class="ltgteq" name="credit_used_op" selected="credit_used_op"}
	<input type=text class=text name=credit_used value="{ifisinrequest name="credit_used"}">
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
    {/addEditTD}

    {addEditTD type="left1" double=TRUE}
	Show Total Credit
    {/addEditTD}

    {addEditTD type="right1" double=TRUE}
	<input type=checkbox class=checktext name=show_total_credit_used {checkBoxValue name="show_total_credit_used"}">
    {/addEditTD}

    {addEditTD type="left2" double=TRUE}
	Show Total Duration
    {/addEditTD}

    {addEditTD type="right2" double=TRUE}
	<input type=checkbox class=checktext name=show_total_duration {checkBoxValue name="show_total_duration"}">
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

    {addEditTD type="right" double=TRUE comment=TRUE}
    	{rasCheckBoxes prefix="ras"}
    {/addEditTD}




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
		<a href="/IBSng/admin/user/user_info.php?user_id={$row.user_id|escape:"url"}">
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
    	    <a onClick="toggleVisibility('{$row.connection_log_id}'); return false;" href="#">
		{listTableBodyIcon cycle_color=TRUE action="details"}
	    </a>
		{reportDetailLayer name=`$row.connection_log_id` title="Report Details"}
		    <table>
		    {foreach from=`$row.details` item=tuple}
			<tr>
			    <td>
				{$tuple[0]}:
			    </td>
			    <td>
				{$tuple[1]}
			    </td>
			</tr>
		    {/foreach}
		    </table>
		{/reportDetailLayer}
	{/listTD}
	
    {/listTR}
  {/foreach}


{/listTable}

{listTable title=Totals cols_num=2}
	{listTR type="body"}
	    {listTD}
		<b>Page</b> Total Credit Used:
    	    {/listTD}
	    {listTD}
	        {$page_total_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}

	{listTR type="body"}
	    {listTD}
		<b>Page</b> Total Duration:
    	    {/listTD}
	    {listTD}
	        {$page_total_duration|duration}
	    {/listTD}

	{/listTR}

	{listTR type="body"}
	    {listTD}
		Total Number Of Rows:
    	    {/listTD}
	    {listTD}
	        {$total_rows} 
	    {/listTD}

	{/listTR}


    {if $total_credit!=-1}
	{listTR type="body"}
	    {listTD}
		Total Credit Used:
    	    {/listTD}
	    {listTD}
	        {$total_credit|price} {$MONEY_UNIT}
	    {/listTD}

	{/listTR}
    {/if}

    {if $total_duration!=-1}
	{listTR type="body"}
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


{addRelatedLink}
    <a href="/IBSng/admin/report/online_users.php" class="RightSide_links">
	Online Users
    </a>
{/addRelatedLink}


{setAboutPage title="Connection Log"}
    
{/setAboutPage}


{include file="admin_footer.tpl"}