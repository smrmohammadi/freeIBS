{* Group Info


    Group Properties:
	$group_name
	$group_id
	$comment
	$owner_id
	$owner_name
	$attrs





*}
{include file="admin_header.tpl" title="Group Information"}
{include file="err_head.tpl"}

<center>
    <table>
	<tr>
	    <td>    
		Group ID: 
	    <td>
		{$group_id}
	    <td>
		Group Name:
	    <td>
		{$group_name}
	<tr>
	    <td>
		Owner Name:
	    <td>
		{$owner_name}
	<tr>
	    <td>
		Comment:
	    <td colspan=3>
		{$comment}
    </table>
</center>
<table>
    <tr>
	<td>
	    {include file="plugins/rel_exp_date_view.tpl"}
    <tr>
	<td>
	    {include file="plugins/multi_login_view.tpl"}
    <tr>
</table>

{include file="footer.tpl"}
