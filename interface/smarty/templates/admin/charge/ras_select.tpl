<script language="javascript" src="/IBSng/js/dom_container.js"> </script>
<script language="javascript">
    ras_select=new DomContainer();
    ras_select.setOnSelect("display","");
    ras_select.setOnUnSelect("display","none");
</script>

<table width=100%>
    <tr>
	<td>
	    <input type=radio name=ras value=_ALL_ {if $ras_selected eq "_ALL_"} checked {/if} onClick='ras_select.select("_ALL_")'> All Rases

	    <div id="_ALL_"></div>
	    <script language="javascript">
		ras_select.addByID("_ALL_");
	    </script>

    {foreach from=$rases key=ras_ip item=ports}
	{ipescape ip=$ras_ip assign="ras_ip_escaped"}

	<tr>
	    <td>
		<input type=radio name=ras value="{$ras_ip}"  {if $ras_selected eq $ras_ip} checked {/if} onClick='ras_select.select("{$ras_ip}")'> {$ras_ip}
	    <td>
		<input type=checkbox name="{$ras_ip_escaped}_ALL_" {ifisinrequest name="`$ras_ip_escaped`_ALL_" default_var="`$ras_ip`_ALL_" default="" value="checked"} > All Ports
    
	<tr id="{$ras_ip}">
	    <td colspan=2>
		<table width=100%>
		    {foreach from=$ports key=index item=port}
			{if $index%3==0}
			    <tr>
			{/if}
			<td>
			    <input type=checkbox name="{$ras_ip_escaped}__{$port.port_name}" {ifisinrequest name="`$ras_ip_escaped`__`$port.port_name`" default_var="`$ras_ip`_`$port.port_name`" default="" value="checked"} > {$port.port_name}
	
		    {/foreach}
		</table>
	    <script language="javascript">
		ras_select.addByID("{$ras_ip}");
	    </script>
	
    {/foreach}
</table>
    <script language="javascript">
	ras_select.select("{$ras_selected}");
    </script>
