{attrUpdateMethod update_method="normalAttrs"}
{viewTable title="Internet Username and Password" table_width="370"} 
    {addEditTD type="left"}
	Has Internet Username
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="has_normal_username" value="t" class=checkbox {if attrDefault($user_attrs,"normal_username","has_normal_username")!=""}checked{/if} onClick='normal_select.toggle("normal_username")'>
    {/addEditTD}

    {addEditTD type="left"}
	Internet Username
    {/addEditTD}

    {addEditTD type="right"}
	<input id="normal_username" type=text  class=text name="normal_username" value="{attrDefault target="user" default_var="normal_username" default_request="normal_username"}"> 
	{multistr form_name="user_edit" input_name="normal_username"}
	{helpicon subject="normal username" category="user"}
    {/addEditTD}

    {addEditTD type="left"}
	Generate Password
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox id="generate_password" name="generate_password" value="t" class=checkbox {ifisinrequest name="generate_password" value="checked" } onClick='normalGeneratePasswordOnClick(this);'>
	{helpicon subject="generate password" category="user"}
    {/addEditTD}

    {addEditTD type="left" id="password_char_tr"}
	Password Include
    {/addEditTD}

    {addEditTD type="right"}
	Character <input type=checkbox class=checkbox name="password_character" id="password_character" value="t" {ifisinrequest name="password_character" value="checked" default="checked"}> 
	Digit <input type=checkbox class=checkbox name="password_digit" id="password_digit" value="t" {ifisinrequest name="password_digit" value="checked" default="checked"}> 
	{helpicon subject="password characters" category="user"}
    {/addEditTD}

    {addEditTD type="left" id="password_len_tr"}
	Generated Password Length
    {/addEditTD}

    {addEditTD type="right"}
	<input type=text id="password_len" name="password_len" value="{ifisinrequest name="password_len" default="6"}" class=small_text>
	{helpicon subject="password length" category="user"}
    {/addEditTD}

    {addEditTD type="left" id="password_tr"}
	Password
    {/addEditTD}

    {addEditTD type="right"}
	<input type=text id="password" name="password" value="{ifisinrequest name="password"}" class=text>
	{multistr form_name="user_edit" input_name="password"}
	{helpicon subject="password" category="user"}
    {/addEditTD}



    {addEditTD type="left"}
	Save In List of username/passwords
    {/addEditTD}

    {addEditTD type="right"}
	<input type=checkbox name="normal_save_user_add" id="normal_save_user_add" value="t" class=checkbox {ifisinrequest name="normal_save_user_add" value="checked"}>
	{helpicon subject="save username and password" category="user"}
    {/addEditTD}
{/viewTable}
<script language="javascript">
	normal_select=new DomContainer();
	normal_select.disable_unselected=true;
	normal_select.addByID("normal_username",new Array("generate_password","password","password_len","password_character","password_digit","normal_save_user_add"));
{if attrDefault($user_attrs,"normal_username","has_normal_username")!=""}
    normal_select.select("normal_username");
{else}
    normal_select.select(null);
{/if}
	generate_password=new DomContainer();
	generate_password.addByID("password_tr",[]);
	generate_password.addByID("password_char_tr",new Array("password_len_tr"));
	generate_password.setOnSelect("display","");
	generate_password.setOnUnSelect("display","none");	
{if isInRequest("generate_password")}
	generate_password.select("password_char_tr");
{else}
	generate_password.select("password_tr");	
{/if}
{literal}
function normalGeneratePasswordOnClick(obj)
{
    if(obj.checked)
    {
	generate_password.select("password_char_tr");
	document.user_edit.normal_save_user_add.checked=true;
    }
    else
	generate_password.select("password_tr");
}
{/literal}
</script>