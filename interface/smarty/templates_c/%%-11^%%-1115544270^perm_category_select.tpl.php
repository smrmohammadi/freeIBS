<?php /* Smarty version 2.6.2, created on 2004-05-23 13:02:15
         compiled from admin/admins/perm_category_select.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'config_load', 'admin/admins/perm_category_select.tpl', 4, false),)), $this); ?>
<?php echo smarty_function_config_load(array('file' => "perm_category_names.conf"), $this);?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add Permission to admin')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

Adding permission to "<?php echo $this->_tpl_vars['admin_username']; ?>
"<br>
<center>
    <h2> 
	
	Please Select Permission category
    </h2>

    <table>
	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=ADMIN&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['ADMIN']; ?>
</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=BASIC_USER&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['BASIC_USER']; ?>
</a>
		
	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=NORMAL_USER&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['NORMAL_USER']; ?>
</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=VOIP_USER&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['VOIP_USER']; ?>
</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=CHARGE&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['CHARGE']; ?>
</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=GROUP&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['GROUP']; ?>
</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=RAS&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['RAS']; ?>
</a>

	<tr>	
	    <td>
		<a href="/IBSng/admin/admins/show_perms.php?category=MISC&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
"><?php echo $this->_config[0]['vars']['MISC']; ?>
</a>


    </table>
</center>
</form>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>