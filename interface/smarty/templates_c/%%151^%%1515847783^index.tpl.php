<?php /* Smarty version 2.6.2, created on 2004-05-13 10:57:01
         compiled from admin/index.tpl */ ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "header.tpl", 'smarty_include_vars' => array('title' => 'Admin Login')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

    <form method=POST>
    <table>
	<tr>
	    <td colspan=2 align=center>
		Admin Login
	<tr>
	    <td>
		Username:
	    <td>
		<input type=text name=username>
	<tr>
	    <td>
		Password:
	    <td>
		<input type=password name=password>
	<tr>
	    <td colspan=2 align=center>
		<input type=submit name=submit value=submit>

    </table>
    </form>
</center>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>