<?php /* Smarty version 2.6.2, created on 2004-06-14 15:35:24
         compiled from plugins/multi_login_edit.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'default', 'plugins/multi_login_edit.tpl', 12, false),)), $this); ?>
<table>
    <tr>
	<td align=center>
	    Multi Login

    <tr>
	<td>
	    <input type=checkbox name=has_attr <?php if (isset ( $this->_tpl_vars['has_attr'] ) || ( ! isset ( $this->_tpl_vars['update'] ) && array_key_exists ( 'multi_login' , $this->_tpl_vars['attrs'] ) )): ?> checked <?php endif; ?> > Have Multi Login
	    <input type=hidden name=attr__1 value="multi_login">
    <tr>
        <td>
	    Multi Login: <input type=text name=multi_login value="<?php echo ((is_array($_tmp=@$this->_tpl_vars['attrs']['multi_login'])) ? $this->_run_mod_handler('default', true, $_tmp, "") : smarty_modifier_default($_tmp, "")); ?>
">
    <tr>
	<td>
	    <input type=submit value=update>
</table>