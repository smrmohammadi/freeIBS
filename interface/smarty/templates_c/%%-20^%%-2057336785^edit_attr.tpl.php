<?php /* Smarty version 2.6.2, created on 2004-06-13 16:34:11
         compiled from admin/user/edit_attr.tpl */ ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Edit Attributes')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
<form method=POST action="edit_attr.php">
    <input type=hidden name=target value="<?php echo $this->_tpl_vars['target']; ?>
">
    <input type=hidden name=target_id value="<?php echo $this->_tpl_vars['target_id']; ?>
">
    <input type=hidden name=update value="true">
    <?php if (isset ( $this->_tpl_vars['template_file'] ) && $this->_tpl_vars['template_file'] != ""): ?>
	<input type=hidden name=template_name value="<?php echo $this->_tpl_vars['template_name']; ?>
">
	<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => $this->_tpl_vars['template_file'], 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <?php endif; ?>
</form>