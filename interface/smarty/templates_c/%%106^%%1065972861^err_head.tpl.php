<?php /* Smarty version 2.6.2, created on 2004-06-11 15:43:04
         compiled from err_head.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'escape', 'err_head.tpl', 6, false),)), $this); ?>
<table align=center border=1>
<?php if (isset ( $this->_tpl_vars['err_msgs'] )): ?>
    <?php if (count($_from = (array)$this->_tpl_vars['err_msgs'])):
    foreach ($_from as $this->_tpl_vars['err']):
?>
	<tr>
	    <td align=center>
		<?php echo ((is_array($_tmp=$this->_tpl_vars['err'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'html') : smarty_modifier_escape($_tmp, 'html')); ?>

	    </td>
	</tr>
    <?php endforeach; unset($_from); endif;  endif; ?>
</table>