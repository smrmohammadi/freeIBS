<table >
    {literal}
    <script language="javascript" src="/IBSng/js/check_box_container.js"></script>
    <script language="javascript">
	var dows=new CheckBoxContainer();
    </script>
    {/literal}
    <tr>
	<td>
	    <input type=checkbox name=checkall > Check All
        
    {foreach from=$day_of_weeks key=index item=day_of_week}
	{if $index%2-1}
	    <tr>
	{/if}
	    <td>
		{$day_of_week}
	    <td>
		<input type=checkbox name="{$day_of_week}" {ifisinrequest name=$day_of_week default_var=$day_of_week default="" value="checked"} >
		<script language="javascript">
		    dows.addByName("{$form_name}","{$day_of_week}");
		</script>
    {/foreach}
    <script language="javascript">
	    {if isset($check_all_days) and $check_all_days}
		dows.checkAll();
	    {/if}
	    dows.setCheckAll("{$form_name}","checkall");
    </script>	    
</table>
