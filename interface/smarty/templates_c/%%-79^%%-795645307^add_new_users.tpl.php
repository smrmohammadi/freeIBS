<?php /* Smarty version 2.6.2, created on 2004-07-15 21:10:31
         compiled from admin/user/add_new_users.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'helpicon', 'admin/user/add_new_users.tpl', 20, false),array('function', 'ifibserr', 'admin/user/add_new_users.tpl', 21, false),array('function', 'admin_names_select', 'admin/user/add_new_users.tpl', 50, false),array('function', 'group_names_select', 'admin/user/add_new_users.tpl', 64, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add New Users')));
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
		Add New Users <?php echo smarty_function_helpicon(array('subject' => 'add new users','category' => 'user'), $this);?>

	<tr <?php echo smarty_function_ifibserr(array('varname' => 'count_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Count:
	    <td>
		<input type=text name=count value="<?php echo $this->_tpl_vars['count']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'count','category' => 'user'), $this);?>


	<tr <?php echo smarty_function_ifibserr(array('varname' => 'credit_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Credit:
	    <td>
		<input type=text name=credit value="<?php echo $this->_tpl_vars['credit']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'credit','category' => 'user'), $this);?>


	<tr <?php echo smarty_function_ifibserr(array('varname' => 'credit_comment_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Credit Change Comment:
	    <td>
		<input type=text name=credit_comment value="<?php echo $this->_tpl_vars['credit_comment']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'credit_comment','category' => 'user'), $this);?>


	<tr <?php echo smarty_function_ifibserr(array('varname' => 'owner_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Owner:
	    <td>
		<?php if (canDo ( 'CHANGE_USER_OWNER' )): ?>
		    <?php echo smarty_function_admin_names_select(array('name' => 'owner_name','default' => 'owner_name'), $this);?>

		<?php else: ?>
		    <?php echo $this->_tpl_vars['auth_name']; ?>

		    <input type=hidden name="owner_name" value="<?php echo $this->_tpl_vars['auth_name']; ?>
">
		<?php endif; ?>
	    	
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'owner','category' => 'user'), $this);?>


	    
	<tr <?php echo smarty_function_ifibserr(array('varname' => 'group_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Group:
	    <td>
		    <?php echo smarty_function_group_names_select(array('name' => 'group_name','default' => 'group_name'), $this);?>

	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'group','category' => 'user'), $this);?>


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