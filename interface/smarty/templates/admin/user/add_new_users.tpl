{* Add New User
    count: new group
    credit: 
    owner_name:
    group_name:
    credit_comment
    
    Success: client will be redirected to the new users information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Add New Users"}
{include file="err_head.tpl"}

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Users {helpicon subject="add new users" category="user"}
	<tr {ifibserr varname="count_err" add="bgcolor=red"} >
	    <td>
		Count:
	    <td>
		<input type=text name=count value="{$count}">
	    <td>
		{helpicon subject="count" category="user"}

	<tr {ifibserr varname="credit_err" add="bgcolor=red"} >
	    <td>
		Credit:
	    <td>
		<input type=text name=credit value="{$credit}">
	    <td>
		{helpicon subject="credit" category="user"}

	<tr {ifibserr varname="credit_comment_err" add="bgcolor=red"} >
	    <td>
		Credit Change Comment:
	    <td>
		<input type=text name=credit_comment value="{$credit_comment}">
	    <td>
		{helpicon subject="credit_comment" category="user"}

	<tr {ifibserr varname="owner_err" add="bgcolor=red"} >
	    <td>
		Owner:
	    <td>
		{if canDo("CHANGE_USER_OWNER")}
		    {admin_names_select name="owner_name" default="owner_name"}
		{else}
		    {$auth_name}
		    <input type=hidden name="owner_name" value="{$auth_name}">
		{/if}
	    	
	    <td>
		{helpicon subject="owner" category="user"}

	    
	<tr {ifibserr varname="group_err" add="bgcolor=red"}>
	    <td>
		Group:
	    <td>
		    {group_names_select name="group_name" default="group_name"}
	    <td>
		{helpicon subject="group" category="user"}

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
{include file="footer.tpl"}
