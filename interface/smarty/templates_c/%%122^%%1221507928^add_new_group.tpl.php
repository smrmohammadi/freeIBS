<?php /* Smarty version 2.6.2, created on 2004-05-23 12:11:56
         compiled from admin/group/add_new_group.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'helpicon', 'admin/group/add_new_group.tpl', 17, false),array('function', 'ifibserr', 'admin/group/add_new_group.tpl', 18, false),array('modifier', 'strip', 'admin/group/add_new_group.tpl', 31, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add New Group')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Group <?php echo smarty_function_helpicon(array('subject' => 'add new group','category' => 'group'), $this);?>

	<tr <?php echo smarty_function_ifibserr(array('varname' => 'group_name_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Group Name:
	    <td>
		<input type=text name=group_name value="<?php echo $this->_tpl_vars['group_name']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'group name','category' => 'group'), $this);?>

	    
	<tr <?php echo smarty_function_ifibserr(array('varname' => 'comment_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    <?php echo ((is_array($_tmp=$this->_tpl_vars['comment'])) ? $this->_run_mod_handler('strip', true, $_tmp) : smarty_modifier_strip($_tmp)); ?>

		</textarea>
	    <td>

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>