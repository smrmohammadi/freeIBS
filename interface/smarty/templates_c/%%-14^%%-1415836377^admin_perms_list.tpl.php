<?php /* Smarty version 2.6.2, created on 2004-05-23 13:02:10
         compiled from admin/admins/admin_perms_list.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'config_load', 'admin/admins/admin_perms_list.tpl', 4, false),array('function', 'eval', 'admin/admins/admin_perms_list.tpl', 56, false),array('function', 'jsconfirm', 'admin/admins/admin_perms_list.tpl', 61, false),array('modifier', 'capitalize', 'admin/admins/admin_perms_list.tpl', 34, false),array('modifier', 'escape', 'admin/admins/admin_perms_list.tpl', 60, false),array('modifier', 'truncate', 'admin/admins/admin_perms_list.tpl', 102, false),)), $this); ?>
<?php echo smarty_function_config_load(array('file' => "admin_perms_list.conf"), $this);?>

<?php echo smarty_function_config_load(array('file' => "perm_category_names.conf"), $this);?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Admin Permission List')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

    

<center>

<?php if ($this->_tpl_vars['del_perm_success'] == TRUE): ?>
    Permission deleted from admin successfully
<?php endif; ?>

<?php if ($this->_tpl_vars['del_perm_val_success'] == TRUE): ?>
    Permission Value updated successfully
<?php endif; ?>

<?php if ($this->_tpl_vars['save_template_success'] == TRUE): ?>
    Permissions Saved to template successfully
<?php endif; ?>

<?php if ($this->_tpl_vars['load_template_success'] == TRUE): ?>
    Permission Template Loaded into admin successfully
<?php endif; ?>

<?php if ($this->_tpl_vars['del_template_success'] == TRUE): ?>
    Permission Template Deleted successfully
<?php endif; ?>

    <h2> 
	"<?php echo ((is_array($_tmp=$this->_tpl_vars['admin_username'])) ? $this->_run_mod_handler('capitalize', true, $_tmp) : smarty_modifier_capitalize($_tmp)); ?>
" Permission List
    </h2>
    <?php if (count($_from = (array)$this->_tpl_vars['perms'])):
    foreach ($_from as $this->_tpl_vars['category'] => $this->_tpl_vars['cat_perms']):
?>
	<table>
	    <tr>
		<td>
		    Category: <?php echo $this->_tpl_vars['category_names'][$this->_tpl_vars['category']]; ?>

	    <tr>
		<td>
		    <table border=1>
			<tr>
			    <th>
				Name
			    <th>
				Value
			    <th>
				Description
			

	    <?php if (count($_from = (array)$this->_tpl_vars['cat_perms'])):
    foreach ($_from as $this->_tpl_vars['perm']):
?>
	    <tr>
		<td>
		    <a href="<?php echo smarty_function_eval(array('var' => $this->_config[0]['vars']['show_perms_link']), $this);?>
">
		    <?php echo $this->_tpl_vars['perm']['name']; ?>

		    </a>
		    <?php if ($this->_tpl_vars['can_change'] == TRUE): ?>
			<a href="/IBSng/admin/admins/admin_perms_list.php?admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
&delete_perm=<?php echo ((is_array($_tmp=$this->_tpl_vars['perm']['name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
"
			<?php echo smarty_function_jsconfirm(array('msg' => "Are you sure you want to delete Permission ".($this->_tpl_vars['perm']['name'])), $this);?>
>
			    del
			</a>
		    <?php endif; ?>
		<td>
		    <?php if ($this->_tpl_vars['perm']['value_type'] == 'NOVALUE'): ?>
			No Value
		    <?php elseif ($this->_tpl_vars['perm']['value_type'] == 'SINGLEVALUE'): ?>
			<?php echo $this->_tpl_vars['perm']['value']; ?>
 
			<?php if ($this->_tpl_vars['can_change'] == TRUE): ?>
			    <a href="<?php echo smarty_function_eval(array('var' => $this->_config[0]['vars']['show_perms_link']), $this);?>
">
				Change
			    </a>
			<?php endif; ?>
		    <?php elseif ($this->_tpl_vars['perm']['value_type'] == 'MULTIVALUE'): ?>
			<table>
			<?php if (count($_from = (array)$this->_tpl_vars['perm']['value'])):
    foreach ($_from as $this->_tpl_vars['val']):
?>
			    <tr>
				<td>
				    <?php echo $this->_tpl_vars['val']; ?>
 
				<td>
				    <?php if ($this->_tpl_vars['can_change'] == TRUE): ?>
					<a href="/IBSng/admin/admins/admin_perms_list.php?admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
&delete_perm=<?php echo ((is_array($_tmp=$this->_tpl_vars['perm']['name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
&delete_perm_val=<?php echo ((is_array($_tmp=$this->_tpl_vars['val'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
" 
					 <?php echo smarty_function_jsconfirm(array('msg' => "Are you sure you want to delete value ".($this->_tpl_vars['val'])." from ".($this->_tpl_vars['perm']['name'])), $this);?>
>
					    del
					</a>
				    <?php endif; ?>
			<?php endforeach; unset($_from); endif; ?>
			<?php if ($this->_tpl_vars['can_change'] == TRUE): ?>
			    <tr>
				<td colspan=2>
				    <a href="<?php echo smarty_function_eval(array('var' => $this->_config[0]['vars']['show_perms_link']), $this);?>
">
					<font size=1>
					    Add Another Value
					</font>
				    </a>
			<?php endif; ?>
			</table>
			    			
		    <?php endif; ?>
		<td>
		    <?php echo ((is_array($_tmp=$this->_tpl_vars['perm']['description'])) ? $this->_run_mod_handler('truncate', true, $_tmp, 100) : smarty_modifier_truncate($_tmp, 100)); ?>

	    <?php endforeach; unset($_from); endif; ?>
		    </table>
	
	</table>
    <?php endforeach; unset($_from); endif; ?>


<?php if ($this->_tpl_vars['can_change'] == TRUE): ?>
    <a href="/IBSng/admin/admins/show_perm_categories.php?admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
">
	Add New Permission
    </a>
    
    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin/admins/admin_perms_list_templates.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  endif;  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>