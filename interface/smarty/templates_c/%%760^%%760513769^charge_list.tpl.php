<?php /* Smarty version 2.6.2, created on 2004-05-12 17:39:05
         compiled from admin/charge/charge_list.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'escape', 'admin/charge/charge_list.tpl', 33, false),)), $this); ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Charge List')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
<table>
    <tr>
	<th>
	    Charge Name
	<th>
	    Charge Type
	<th>
	    Visible To All
	<th>
	    Creator
	<th>
	    	
    
    <?php if (count($_from = (array)$this->_tpl_vars['charge_infos'])):
    foreach ($_from as $this->_tpl_vars['charge_name'] => $this->_tpl_vars['charge_info']):
?>
	<tr>
	    <td>
		<?php echo $this->_tpl_vars['charge_name']; ?>

	    <td>
		<?php echo $this->_tpl_vars['charge_info']['charge_type']; ?>
	
    	    <td>
		<?php echo $this->_tpl_vars['charge_info']['visible_to_all']; ?>

	    <td>
		<?php echo $this->_tpl_vars['charge_info']['creator']; ?>

	    <td>
		<a href="/IBSng/admin/charge/charge_info.php?charge_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['charge_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">info</a>
	
    <?php endforeach; unset($_from); endif; ?>
</table>
</center>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>