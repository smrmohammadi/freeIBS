<?php /* Smarty version 2.6.2, created on 2004-05-23 13:02:10
         compiled from admin/admins/admin_perms_list_templates.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'html_options', 'admin/admins/admin_perms_list_templates.tpl', 28, false),array('function', 'jsconfirm', 'admin/admins/admin_perms_list_templates.tpl', 34, false),)), $this); ?>

<table align=center border=1>
    <tr>
	<td>
	    <form method=POST action="admin_perms_list.php">
	    Save This Admin Permissions into template:
	<td>
	    <input type=text name=template_name>
	    <input type=hidden name=action value=save>
	    <input type=hidden name=admin_username value=<?php echo $this->_tpl_vars['admin_username']; ?>
>
	<td>
	    <input type=submit value=save>
	    </form>
    <tr>
	<td>
	    <form method=POST action="admin_perms_list.php" name="load_template">
	    Load Permission Template into admin:
	<td>
	    <?php echo '
	    <script language="javascript">
		function showTemplatePerms(){
		    selected=getSelectedOption("load_template","template_name");
		    open("show_permtemplate_perms.php?template_name="+selected,"template_perms","width=500,height=400,scrollbars=yes");
		}
	    </script>
	    '; ?>

	    <select name=template_name>
		<?php echo smarty_function_html_options(array('values' => $this->_tpl_vars['templates_list'],'output' => $this->_tpl_vars['templates_list']), $this);?>

	    </select> <a href="javascript:showTemplatePerms();">Show Permissions</a>
	    <input type=hidden name=action value=load>
	    <input type=hidden name=admin_username value=<?php echo $this->_tpl_vars['admin_username']; ?>
>
	<td>
	    <input type=submit value=load 
	    <?php echo smarty_function_jsconfirm(array('raw_msg' => '"Are you sure you want to load permission template "+getSelectedOption("load_template","template_name")+" to admin `$admin_username` ? \\nWarning: Loading template will delete --ALL-- of current admin permissions."'), $this);?>
>
	    </form>
    <tr>
	<td>
	    <form method=POST action="admin_perms_list.php" name="del_template">
	    Delete Permission Template
	<td>
	    <select name=template_name>
		<?php echo smarty_function_html_options(array('values' => $this->_tpl_vars['templates_list'],'output' => $this->_tpl_vars['templates_list']), $this);?>

	    </select>
	    <input type=hidden name=action value=delete>
	    <input type=hidden name=admin_username value=<?php echo $this->_tpl_vars['admin_username']; ?>
>
	<td>
	    <input type=submit value=delete <?php echo smarty_function_jsconfirm(array('raw_msg' => "\"Are you sure you want to delete permission template \"+getSelectedOption(\"del_template\",\"template_name\")+\" ?\""), $this);?>
>
	    </form>

</table>
	    