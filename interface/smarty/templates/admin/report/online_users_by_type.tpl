{* Online Users By Type : Show a list of online users, seperated by their type(eg. Internet or VoIP)
*}

{include file="admin_header.tpl" title="Online Users" selected="Online Users"} 
{include file="err_head.tpl"} 
<iframe name=msg id=msg border=0 FRAMEBORDER=0 SCROLLING=NO height=50 valign=top></iframe>
{literal}
    <script language=javascript>
	function killUser(user_id,username,ras_ip,unique_id_val,kill)
	{
	    url = "/IBSng/admin/user/kill_user.php?user_id="+user_id+"&username="+username+"&ras_ip="+ras_ip+"&unique_id_val="+unique_id_val+"&";
	    if(kill)
		url += "kill=1";
	    else
		url += "clear=1";
		
	    document.getElementById("msg").src = url;
	}
    </script>
{/literal}

{include file="refresh_header.tpl" title="Online Users"}

{include file="admin/report/internet_onlines.tpl"}
{include file="admin/report/voip_onlines.tpl"}

{addRelatedLink}
    <a href="/IBSng/admin/user/search_user.php" class="RightSide_links">
	Search User
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/user/user_info.php" class="RightSide_links">
	User Information
    </a>
{/addRelatedLink}

{setAboutPage title="Online Users"}
You can see online users, seperated by their service
{/setAboutPage}

{include file="admin_footer.tpl"}
