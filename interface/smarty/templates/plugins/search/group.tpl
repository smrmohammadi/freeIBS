
{counter name="group_search_id" start=0 print=false}
{foreach from=$group_names item=group_name}
    {counter name="group_search_id" assign="group_search_id"}
    <input name="group_name_{$group_search_id}" value="{$group_name}" type=checkbox {ifisinrequest name="group_name_`$group_search_id`" value="checked"}> {$group_name}
{/foreach}