{* Admin Info
    Shows one admin information, on error, client is redirected to admin_list
    so no error will be shown here
*}
{include file="admin_header.tpl" title="Admin Information" selected="Admin List"}

{include file="err_head.tpl"}
<center>
{headerMsg var_name="update_success"}
    Admin Info Updates Successfully
{/headerMsg}
{if $is_editing}
    <form method=POST action="admin_info.php">
    <input type=hidden name=admin_username value={$username}>
    	{addEditTable title="Admin Information" double="TRUE"}
	    {addEditTD type="left1" double="TRUE"}
		Admin Username
	    {/addEditTD}
	    {addEditTD type="right1" double="TRUE"}
		{$username}
	    {/addEditTD}
	    {addEditTD type="left2" double="TRUE"}
	    	Admin ID
	    {/addEditTD}
	    {addEditTD type="right2" double="TRUE"}
		{$admin_id}
	    {/addEditTD}
	    {addEditTD type="left1" double="TRUE"}
		Name
	    {/addEditTD}
	    {addEditTD type="right1" double="TRUE"}
	        <input class="text" type=text name=name value="{$name}">
	    {/addEditTD}
	    {addEditTD type="left2" double="TRUE"} 
	        Creator
	    {/addEditTD}
	    {addEditTD type="right2" double="TRUE"}
	    	{$creator}
    	    {/addEditTD}
	    {addEditTD type="left1" double="TRUE"}
		    Deposit
	    {/addEditTD}
	    {addEditTD type="right1" double="TRUE"}
		    {$deposit}
	    {/addEditTD}
	    {addEditTD type="left2"  double="TRUE"}
		    
	    {/addEditTD}
	    {addEditTD type="right2" double="TRUE"}
		    
	    {/addEditTD}
	    {addEditTD type="left" comment="TRUE" double="TRUE"}
	    	    Comment
	    {/addEditTD}
	    {addEditTD type="right" comment="TRUE" double="TRUE"}
		    <textarea class="text" name=comment>{$comment|strip}</textarea>
	    {/addEditTD}
	{/addEditTable}
</form>
{else}
	{viewTable title="Admin Information" double="TRUE" table_width="580"}
	    {addEditTD type="left1" double="TRUE"}
		Admin Username
	    {/addEditTD}
	    {addEditTD type="right1" double="TRUE"}
		{$username}
	    {/addEditTD}
	    {addEditTD type="left2" double="TRUE"}
	    	Admin ID
	    {/addEditTD}
	    {addEditTD type="right2" double="TRUE"}
		{$admin_id}
	    {/addEditTD}
	    {addEditTD type="left1" double="TRUE"}
		Name
	    {/addEditTD}
	    {addEditTD type="right1" double="TRUE"}
	        {$name}
	    {/addEditTD}
	    {addEditTD type="left2" double="TRUE"} 
	        Creator
	    {/addEditTD}
	    {addEditTD type="right2" double="TRUE"}
	    	{$creator}
    	    {/addEditTD}
	    {addEditTD type="left1" double="TRUE"}
		    Deposit
	    {/addEditTD}
	    {addEditTD type="right1" double="TRUE"}
		    {$deposit}
	    {/addEditTD}
	    {addEditTD type="left2"  double="TRUE"}
		    
	    {/addEditTD}
	    {addEditTD type="right2" double="TRUE"}
		    
	    {/addEditTD}
	    {addEditTD type="left" comment="TRUE" double="TRUE"}
	    	    Comment
	    {/addEditTD}
	    {addEditTD type="right" comment="TRUE" double="TRUE"}
		    {$comment|strip}
	    {/addEditTD}
	{/viewTable}
{/if}
{canDo perm_name="CHANGE USER INFO" username=$username}
	{addRelatedLink}
    		<a class="RightSide_links" href="/IBSng/admin/admins/admin_info.php?edit=1&admin_username={$username}">    
		    Edit Admin <b>{$username}</b>
		</a>
	{/addRelatedLink}
{/canDo}
{canDo perm_name="SEE ADMIN PERMISSIONS" username=$username}
	{addRelatedLink}
    		<a class="RightSide_links" href="/IBSng/admin/admins/admin_perms_list.php?admin_username={$username}">    
		    <b>{$username}</b> Permissions List
		</a>
	{/addRelatedLink}
{/canDo}

{canDo perm_name="CHANGE ADMIN PASSWORD" username=$username}
	{addRelatedLink}
    		<a class="RightSide_links" href="/IBSng/admin/admins/change_password.php?username={$username}">    
		Change Password <font size=1><b>{$username}</b></font>
		</a>
	{/addRelatedLink}
{/canDo}
{addRelatedLink}
    <a href="/IBSng/admin/admins/admin_list.php" class="RightSide_links">
	Admin List
    </a>
{/addRelatedLink}
{setAboutPage title="Admin Information"}

{/setAboutPage}


{include file="admin_footer.tpl"}