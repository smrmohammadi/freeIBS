<?php /* Smarty version 2.6.2, created on 2004-07-17 19:33:48
         compiled from admin/misc/show_ibs_defs.tpl */ ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'IBS Definitions')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
    <h2>
	IBS Definitions 
    </h2>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<?php if ($this->_tpl_vars['save_success']): ?>
    Definitions updated successfully
<?php endif; ?>

    <p>
	Warning: Changing these value may result IBS not working properly. Don't change any value until you know
	what are you doing.
    </p>

<table align=center border=1>
    <form method=POST>
    <?php if (count($_from = (array)$this->_tpl_vars['defs_arr'])):
    foreach ($_from as $this->_tpl_vars['def_arr']):
?>
    <tr valign=top>
	<td>
	    <?php echo $this->_tpl_vars['def_arr']['name']; ?>

	<td>
	    <?php if (is_array ( $this->_tpl_vars['def_arr']['value'] )): ?>
		<table>
		<?php if (count($_from = (array)$this->_tpl_vars['def_arr']['value'])):
    foreach ($_from as $this->_tpl_vars['index'] => $this->_tpl_vars['member']):
?>
		    <tr>
			<td>
			    <input type=text name="def_<?php echo $this->_tpl_vars['def_arr']['name']; ?>
__<?php echo $this->_tpl_vars['index']; ?>
__" value="<?php echo $this->_tpl_vars['member']; ?>
">
		<?php endforeach; unset($_from); endif; ?>
		    <font size=1>(new value)</font><input type=text name="def_<?php echo $this->_tpl_vars['def_arr']['name']; ?>
__new__" value="">
		</table>
	    <?php else: ?>
		<input type=text name="def_<?php echo $this->_tpl_vars['def_arr']['name']; ?>
" value="<?php echo $this->_tpl_vars['def_arr']['value']; ?>
">
	    <?php endif; ?>
    
    
    <?php endforeach; unset($_from); endif; ?>

</table>
    <input type=hidden name=action value=save>
    <input type=submit name=submit value="save">
</center>
</form>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>