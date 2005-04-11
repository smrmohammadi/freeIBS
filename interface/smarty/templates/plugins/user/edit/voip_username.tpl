{attrUpdateMethod update_method="voipAttrs"}
{viewTable title="VoIP Username and Password" table_width="380" nofoot="TRUE"} 
    {addEditTD type="left"}
	Has VoIP Username
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="has_voip_username" value="t" class=checkbox {if attrDefault($user_attrs,"voip_username","has_voip_username")!=""}checked{/if} onClick='voip_select.toggle("voip_username")'>
    {/addEditTD}

    {addEditTD type="left"}
	VoIP Username
    {/addEditTD}

    {addEditTD type="right"}
	<input type=hidden name=current_voip_username value='{attrDefault target="user" default_var="voip_username" default_request="current_voip_username"}'>
	<input id="voip_username" type=text  class=text name="voip_username" 
	    value="{attrDefault target="user" default_var="voip_username" default_request="voip_username"}" 
	    onChange="updateUserAddCheckImage('voip','{attrDefault target="user" default_var="voip_username" default_request="current_voip_username"}',0);" 
	    onKeyUp="updateUserAddCheckImage('voip','{attrDefault target="user" default_var="voip_username" default_request="current_voip_username"}',1);"
	> 
	{multistr form_name="user_edit" input_name="voip_username"}
	{helpicon subject="voip username" category="user"}
	<a href="#" onClick="showUserAddCheckWindow('voip','{attrDefault target="user" default_var="voip_username" default_request="voip_username"}');">
	    <img border=0 name="voip_user_exists" src="/IBSng/admin/user/check_user_for_add.php?image=t&username=&type=voip&current_username=" title="Users Exist">
	</a>
	<script language=javascript>
	    updateUserAddCheckImage('voip','{attrDefault target="user" default_var="voip_username" default_request="current_voip_username"}',1);
	</script>
    {/addEditTD}

    {addEditTD type="left"}
	Generate Password
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox id="voip_generate_password" name="voip_generate_password" value="t" class=checkbox {ifisinrequest name="voip_generate_password" value="checked" } onClick='voipGeneratePasswordOnClick(this);'>
	{helpicon subject="generate password" category="user"}
    {/addEditTD}

    {addEditTD type="left" id="voip_password_char_tr"}
	Password Includes
    {/addEditTD}

    {addEditTD type="right"}
	Character <input type=checkbox class=checkbox name="voip_password_character" id="voip_password_character" value="t" {ifisinrequest name="voip_password_character" value="checked" default="checked"}> 
	Digit <input type=checkbox class=checkbox name="voip_password_digit" id="voip_password_digit" value="t" {ifisinrequest name="voip_password_digit" value="checked" default="checked"}> 
	{helpicon subject="password characters" category="user"}
    {/addEditTD}

    {addEditTD type="left" id="voip_password_len_tr"}
	Generated Password Length
    {/addEditTD}

    {addEditTD type="right"}
	<input type=text id="voip_password_len" name="voip_password_len" value="{ifisinrequest name="voip_password_len" default="6"}" class=small_text>
	{helpicon subject="password length" category="user"}
    {/addEditTD}

    {addEditTD type="left" id="voip_password_tr"}
	Password
    {/addEditTD}

    {addEditTD type="right"}
	<input type=text id="voip_password" name="voip_password" value="{ifisinrequest name="voip_password"}" class=text>
	{multistr form_name="user_edit" input_name="voip_password"}
	{helpicon subject="password" category="user"}
    {/addEditTD}

    {addEditTD type="left"}
	Save In List<font size=1>[Usernames/Passwords]</font>
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="voip_save_user_add" id="voip_save_user_add" value="t" class=checkbox {ifisinrequest name="voip_save_user_add" value="checked"}>
	{helpicon subject="save username and password" category="user"}
    {/addEditTD}
{/viewTable}
<br>
<script language="javascript">
	voip_select=new DomContainer();
	voip_select.disable_unselected=true;
	voip_select.addByID("voip_username",new Array("voip_generate_password","voip_password","voip_password_len","voip_password_character","voip_password_digit","voip_save_user_add"));
{if attrDefault($user_attrs,"voip_username","has_voip_username")!=""}
    voip_select.select("voip_username");
{else}
    voip_select.select(null);
{/if}
	voip_generate_password=new DomContainer();
	voip_generate_password.addByID("voip_password_tr",[]);
	voip_generate_password.addByID("voip_password_char_tr",new Array("voip_password_len_tr"));
	voip_generate_password.setOnSelect("display","");
	voip_generate_password.setOnUnSelect("display","none");	
{if isInRequest("voip_generate_password")}
	voip_generate_password.select("voip_password_char_tr");
{else}
	voip_generate_password.select("voip_password_tr");	
{/if}
{literal}
function voipGeneratePasswordOnClick(obj)
{
    if(obj.checked)
    {
	voip_generate_password.select("voip_password_char_tr");
	document.user_edit.voip_save_user_add.checked=true;
    }
    else
	voip_generate_password.select("voip_password_tr");
}
{/literal}
</script>