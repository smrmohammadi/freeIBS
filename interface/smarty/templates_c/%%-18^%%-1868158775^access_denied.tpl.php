<?php /* Smarty version 2.6.2, created on 2004-05-25 17:09:53
         compiled from access_denied.tpl */ ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "header.tpl", 'smarty_include_vars' => array('title' => 'Access Denied')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<table align=center border=1>
<tr>
  <td align=center>
    <h2>
	<font color=red>
	    Access Denied
	</font>
    </h2>

    You must log in to access this page. <br>
    This page needs IBS authenticated <b><?php echo $this->_tpl_vars['role']; ?>
</b>.<br>
    You can login <a href="<?php echo $this->_tpl_vars['url']; ?>
"> here </a>
  </td>
</tr>
</table>