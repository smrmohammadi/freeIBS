{headerMsg}
    {$msg}
{/headerMsg}
<center>
    You'll redirect to <a href="/IBSng/admin/user/user_info.php?user_id_multi={$user_id|escape:"url"}">UserInfo</a> 
    Page in <b><span id="redir_timer">&nbsp;</span></b> Seconds
</center>

<script language="javascript">
    user_id="{$user_id|escape:"url"}";
    redir_timer=5;
    updateTimer();
    {literal}
    function updateTimer()
    {
	redir_timer-=1;
	span_obj=document.getElementById("redir_timer");
	span_obj.childNodes[0].nodeValue=redir_timer;
	if(redir_timer==0)
	    window.location="/IBSng/admin/user/user_info.php?user_id_multi="+user_id;
	else
	    setTimeout("updateTimer()",1000);
    }
    {/literal}
</script>
    