{if amIGod() or permValueRestricted("CHANGE_USER_OWNER",getAuthUsername())}
{counter name="owner_search_id" start=0 print=false}
{foreach from=$admin_names item=owner_name}
    {counter name="owner_search_id" assign="owner_search_id"}
    <input name="owner_name_{$owner_search_id}" value="{$owner_name}" type=checkbox {ifisinrequest name="owner_name_`$owner_search_id`" value="checked"}> {$owner_name}
{/foreach}
{/if}