{* 
*}

{include file="header.tpl" title="Check Usernames For User Add"}
{include file="err_head.tpl"}
    {foreach from=$alerts key=error item=users}
	Error: {$error}<br>
	{foreach from=$users item=user}
	    {$user}
	{/foreach}
    {foreachelse}
	No Alerts!
    {/foreach}
{include file="footer.tpl"}
