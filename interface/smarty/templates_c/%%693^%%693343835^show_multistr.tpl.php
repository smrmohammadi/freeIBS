<?php /* Smarty version 2.6.2, created on 2004-07-17 19:27:51
         compiled from util/show_multistr.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'math', 'util/show_multistr.tpl', 23, false),)), $this); ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "header.tpl", 'smarty_include_vars' => array('title' => 'Show Multiple Strings')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
<table border=1 align=center width=100% bgcolor=#FAFFC5>
<tr align=center bgcolor=#3E91EB>
    <td>
	<h2>Show Multiple Strings</h2>
<tr align=left>
    <td>
	Raw Multi String: <b><?php echo $this->_tpl_vars['raw_str']; ?>
</b>
<tr align=left>
    <table width=100% border=1>
    <?php if (count($_from = (array)$this->_tpl_vars['all_strs'])):
    foreach ($_from as $this->_tpl_vars['index'] => $this->_tpl_vars['str']):
?>
	<?php if ($this->_tpl_vars['index']%3 == 0): ?> <tr align=center>  <?php endif; ?>
	    <td bgcolor=#3E91EB width=10%>
		<?php echo smarty_function_math(array('equation' => "index+1",'index' => $this->_tpl_vars['index']), $this);?>

	    <td width=20%>
		<?php echo $this->_tpl_vars['str']; ?>

    <?php endforeach; unset($_from); endif; ?>
    </table>
</table>

<?php echo '
<script language="javascript">
    window.focus();
</script>
'; ?>


<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>