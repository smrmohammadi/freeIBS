
<table align=center border=1>
    <tr>
	<td>
	    <form method=POST action="admin_perms_list.php">
	    Save This Admin Permissions into template:
	<td>
	    <input type=text name=template_name>
	    <input type=hidden name=action value=save>
	    <input type=hidden name=admin_username value={$admin_username}>
	<td>
	    <input type=submit value=save>
	    </form>
    <tr>
	<td>
	    <form method=POST action="admin_perms_list.php" name="load_template">
	    Load Permission Template into admin:
	<td>
	    {literal}
	    <script language="javascript">
		function showTemplatePerms(){
		    selected=getSelectedOption("load_template","template_name");
		    open("show_permtemplate_perms.php?template_name="+selected,"template_perms","width=500,height=400,scrollbars=yes");
		}
	    </script>
	    {/literal}
	    <select name=template_name>
		{html_options values=$templates_list output=$templates_list}
	    </select> <a href="javascript:showTemplatePerms();">Show Permissions</a>
	    <input type=hidden name=action value=load>
	    <input type=hidden name=admin_username value={$admin_username}>
	<td>
	    <input type=submit value=load 
	    {jsconfirm raw_msg='"Are you sure you want to load permission template "+getSelectedOption("load_template","template_name")+" to admin `$admin_username` ? \\nWarning: Loading template will delete --ALL-- of current admin permissions."'}>
	    </form>
    <tr>
	<td>
	    <form method=POST action="admin_perms_list.php" name="del_template">
	    Delete Permission Template
	<td>
	    <select name=template_name>
		{html_options values=$templates_list output=$templates_list}
	    </select>
	    <input type=hidden name=action value=delete>
	    <input type=hidden name=admin_username value={$admin_username}>
	<td>
	    <input type=submit value=delete {jsconfirm raw_msg="\"Are you sure you want to delete permission template \"+getSelectedOption(\"del_template\",\"template_name\")+\" ?\""}>
	    </form>

</table>
	    