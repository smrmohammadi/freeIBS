<?php /* Smarty version 2.6.2, created on 2004-05-27 19:39:01
         compiled from help/skeleton.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'capitalize', 'help/skeleton.tpl', 8, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "help_header.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
<table border=1 align=center width=100% bgcolor=#FAFFC5 id="help_table">
<tr align=center bgcolor=#3E91EB>
    <td>
	<h2>Help!</h2>
<tr align=left>
    <td>
	Subject: <b><?php echo ((is_array($_tmp=$this->_tpl_vars['subject'])) ? $this->_run_mod_handler('capitalize', true, $_tmp) : smarty_modifier_capitalize($_tmp)); ?>
</b>
<tr align=left>
    <td>
	Category: <b><?php echo ((is_array($_tmp=$this->_tpl_vars['category'])) ? $this->_run_mod_handler('capitalize', true, $_tmp) : smarty_modifier_capitalize($_tmp)); ?>
</b>
<tr>
    <td>
	<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => $this->_tpl_vars['tpl_file'], 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

</table>

<?php echo '
<script language="javascript">

    window.focus();
    element=document.getElementById("help_table");
    height=0;
    while (element)
    {    
	height+=element.offsetHeight;
	if(element.offsetTop)
	    height+=element.offsetTop;
	if(element.offsetParent)
	    element=element.offsetParent;
	else
	    element=null;
    }
//    alert(height);
    window.resizeTo(window.outerWidth,height-100);
</script>
'; ?>


<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "help_footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>