<?php /* Smarty version 2.6.2, created on 2004-05-27 19:39:01
         compiled from help/error.tpl */ ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "help_header.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
<center>
Error in Loading Help!<br>
Error Message is: <b><?php echo $this->_tpl_vars['msg']; ?>
</b>

<p>
Maybe Help file is not written yet, or subject/category is misspelled
</p>

</center>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "help_footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>