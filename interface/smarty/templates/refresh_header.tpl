<form method=get action="{requestToUrl ignore="refresh"}" name="refresh_form">
{addEditTable title=$title action_icon="ok" action_onclick="updateRefresh()"}
    {addEditTD type="left"}
	Refresh Every 
    {/addEditTD}
    {addEditTD type="right"}
	{html_options name="refresh" values=$refresh_times output=$refresh_times selected=$refresh_default}
	Seconds <font size=1>(<span id="timer">&nbsp;</span> seconds remaining)</font>
    {/addEditTD}
{/addEditTable}
</form>

<script language=javascript>
{if isInRequest("refresh")}
    refresh={$smarty.request.refresh};
{else}
    refresh=10;
{/if}
    url_without_refresh='{requestToUrl ignore="refresh"}';
{literal}
    updateTimer();
    function updateTimer()
    {
	refresh-=1;
	span_obj=document.getElementById("timer");
	span_obj.childNodes[0].nodeValue=refresh;
	if(refresh==0)
	    window.location.reload();
	else	    
	    setTimeout("updateTimer()",1000);
    }

    function updateRefresh()
    {
	window.location=url_without_refresh+"&refresh="+document.refresh_form.refresh.value;
	return false;
    }
{/literal}

</script>