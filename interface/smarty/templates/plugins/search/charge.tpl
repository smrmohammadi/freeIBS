Charge Names:
{counter name="charge_search_id" start=0 print=false}
{foreach from=$charge_names item=charge_name}
    {counter name="charge_search_id" assign="charge_search_id"}
    <input name="charge_name_{$charge_search_id}" value="{$charge_name}" type=checkbox {ifisinrequest name="charge_name_`$charge_search_id`" value="checked"}> {$charge_name}
{/foreach}