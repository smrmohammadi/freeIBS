<?php /* Smarty version 2.6.2, created on 2004-07-15 21:07:53
         compiled from plugins/rel_exp_date_view.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'edit_attr_link', 'plugins/rel_exp_date_view.tpl', 14, false),)), $this); ?>
<table>
    <tr>
	<td align=center bgcolor=blue>
	    Relative Expiration Date
    <?php if ($this->_tpl_vars['has_rel_exp']): ?>
	<tr>
	    <td>
		<?php echo $this->_tpl_vars['rel_exp_date']; ?>

	    <td>
		<?php echo $this->_tpl_vars['rel_exp_date_unit']; ?>

    <?php endif; ?>
    <tr>
	<td>
	<?php echo smarty_function_edit_attr_link(array('template_name' => 'rel_exp_date_edit'), $this);?>

</table>
	