<?php /* Smarty version 2.6.2, created on 2004-06-13 14:23:54
         compiled from admin/group/group_list.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'escape', 'admin/group/group_list.tpl', 28, false),)), $this); ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Group List')));
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
	    Group ID
	<th>
	    Group Name
	<th>
	    Owner
	    	
    
    <?php if (count($_from = (array)$this->_tpl_vars['group_infos'])):
    foreach ($_from as $this->_tpl_vars['group_info']):
?>
	<tr>
	    <td>
		<?php echo $this->_tpl_vars['group_info']['group_id']; ?>

	    <td>
		<?php echo $this->_tpl_vars['group_info']['group_name']; ?>

    	    <td>
		<?php echo $this->_tpl_vars['group_info']['owner_name']; ?>

	    <td>
		<a href="/IBSng/admin/group/group_info.php?group_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['group_info']['group_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">info</a>
	
    <?php endforeach; unset($_from); endif; ?>
</table>
</center>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>