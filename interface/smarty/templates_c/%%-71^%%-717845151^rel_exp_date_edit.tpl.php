<?php /* Smarty version 2.6.2, created on 2004-07-16 17:39:27
         compiled from plugins/rel_exp_date_edit.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'default', 'plugins/rel_exp_date_edit.tpl', 13, false),array('function', 'relative_units', 'plugins/rel_exp_date_edit.tpl', 15, false),)), $this); ?>
<table>
    <tr>
	<td align=center>
	    Relative Expiration Date

    <tr>
	<td>
	    <input type=checkbox name=has_attr <?php if (isset ( $this->_tpl_vars['has_attr'] ) || ( ! isset ( $this->_tpl_vars['update'] ) && $this->_tpl_vars['has_rel_exp'] )): ?> checked <?php endif; ?> > Have Relative Expiration Date
	    <input type=hidden name=attr__1 value="rel_exp_date">
	    <input type=hidden name=attr__2 value="rel_exp_date_unit">
    <tr>
        <td>
	    Relative Expiration Date: <input type=text name=rel_exp_date value="<?php echo ((is_array($_tmp=@$this->_tpl_vars['rel_exp_date'])) ? $this->_run_mod_handler('default', true, $_tmp, "") : smarty_modifier_default($_tmp, "")); ?>
">
	<td>
	    <?php echo smarty_function_relative_units(array('default' => 'rel_exp_date_unit','name' => 'rel_exp_date_unit'), $this);?>

    <tr>
	<td>
	    <input type=submit value=update>
</table>
	