<?php /* Smarty version 2.6.2, created on 2004-06-11 16:15:51
         compiled from admin/group/group_info.tpl */ ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Group Information')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
    <table>
	<tr>
	    <td>    
		Group ID: 
	    <td>
		<?php echo $this->_tpl_vars['group_id']; ?>

	    <td>
		Group Name:
	    <td>
		<?php echo $this->_tpl_vars['group_name']; ?>

	<tr>
	    <td>
		Owner Name:
	    <td>
		<?php echo $this->_tpl_vars['owner_name']; ?>

	<tr>
	    <td>
		Comment:
	    <td colspan=3>
		<?php echo $this->_tpl_vars['comment']; ?>

    </table>
</center>
<table>
    <tr>
	<td>
	    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "plugins/rel_exp_date_view.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <tr>
	<td>
	    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "plugins/multi_login_view.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <tr>
</table>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>