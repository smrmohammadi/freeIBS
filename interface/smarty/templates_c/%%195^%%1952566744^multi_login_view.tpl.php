<?php /* Smarty version 2.6.2, created on 2004-06-14 15:36:12
         compiled from plugins/multi_login_view.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'edit_attr_link', 'plugins/multi_login_view.tpl', 12, false),)), $this); ?>
<table>
    <tr>
	<td align=center bgcolor=blue>
	    Multi Login
    <?php if (array_key_exists ( 'multi_login' , $this->_tpl_vars['attrs'] )): ?>
	<tr>
	    <td>
		Can Login Up To <b><?php echo $this->_tpl_vars['attrs']['multi_login']; ?>
</b> instances
    <?php endif; ?>
    <tr>
	<td>
	<?php echo smarty_function_edit_attr_link(array('template_name' => 'multi_login_edit'), $this);?>

</table>
	