<?php /* Smarty version 2.6.2, created on 2004-07-17 19:24:47
         compiled from admin/ras/ras_info.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'ifibserr', 'admin/ras/ras_info.tpl', 63, false),array('function', 'html_options', 'admin/ras/ras_info.tpl', 81, false),array('function', 'jsconfirm', 'admin/ras/ras_info.tpl', 148, false),array('function', 'multistr', 'admin/ras/ras_info.tpl', 192, false),array('modifier', 'escape', 'admin/ras/ras_info.tpl', 148, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Ras Information')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>

<?php if (isset ( $this->_tpl_vars['update_ras_info_success'] ) && $this->_tpl_vars['update_ras_info_success']): ?>
    <h2>
	Ras Info Updated Successfully
    </h2>
<?php endif; ?>

<?php if (isset ( $this->_tpl_vars['update_ras_attrs_success'] ) && $this->_tpl_vars['update_ras_attrs_success']): ?>
    <h2>
	Ras Attributes Updated Successfully
    </h2>
<?php endif; ?>


<?php if (isset ( $this->_tpl_vars['reset_ras_attrs_success'] ) && $this->_tpl_vars['reset_ras_attrs_success']): ?>
    <h2>
	Ras Attributes Reset Successfully
    </h2>
<?php endif; ?>

<?php if (isset ( $this->_tpl_vars['del_port_success'] ) && $this->_tpl_vars['del_port_success']): ?>
    <h2>
	Port(s) Deleted Successfully
    </h2>
<?php endif; ?>

</center>


<?php if ($this->_tpl_vars['is_editing'] || $this->_tpl_vars['attr_editing']): ?>
    <form method=POST action="/IBSng/admin/ras/ras_info.php">
<?php endif;  if ($this->_tpl_vars['is_editing']): ?>
    <input type=hidden name=edit value=1>
    <input type=hidden name=old_ras_ip value="<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
">
    <input type=hidden name=ras_id value="<?php echo $this->_tpl_vars['info']['ras_id']; ?>
">
<?php endif; ?>

<?php if ($this->_tpl_vars['attr_editing']): ?>
    <input type=hidden name=attr_editing_done value=1>
    <input type=hidden name=ras_ip value="<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
">
<?php endif; ?>
    
<center>
    <table border=1>
	<tr>	
	    <td>

		Ras IP:
	    <td <?php echo smarty_function_ifibserr(array('varname' => 'ras_ip_err','add' => "bgcolor=red"), $this);?>
>
		<?php if ($this->_tpl_vars['is_editing']): ?>
		    <input type=text name=ras_ip value="<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
">
		    
		    
		<?php else: ?>		
		    <?php echo $this->_tpl_vars['info']['ras_ip']; ?>

		<?php endif; ?>
	    <td>
		Ras ID:
	    <td>
		<?php echo $this->_tpl_vars['info']['ras_id']; ?>

	<tr>
	    <td>
		Type:
	    <td <?php echo smarty_function_ifibserr(array('varname' => 'ras_type_err','add' => "bgcolor=red"), $this);?>
>
		<?php if ($this->_tpl_vars['is_editing']): ?>
		    <select name=ras_type>
			<?php echo smarty_function_html_options(array('output' => $this->_tpl_vars['ras_types'],'values' => $this->_tpl_vars['ras_types'],'default' => $this->_tpl_vars['info']['ras_type']), $this);?>

		    </select>
		<?php else: ?>		
		    <?php echo $this->_tpl_vars['info']['ras_type']; ?>

		<?php endif; ?>
	    <td>
		Radius Secret:
	    <td <?php echo smarty_function_ifibserr(array('varname' => 'ras_radius_secret_err','add' => "bgcolor=red"), $this);?>
>
		<?php if ($this->_tpl_vars['is_editing']): ?>
		    <input type=text name=radius_secret value="<?php echo $this->_tpl_vars['info']['radius_secret']; ?>
">
		<?php else: ?>		
		    <?php echo $this->_tpl_vars['info']['radius_secret']; ?>

		<?php endif; ?>
    </table>
</center>
<table width=100% border=1>
    <tr valign=top>
	<td>
	    <table border=1>
		<tr>
		    <td colspan=2 align=center>
			Attributes
		<tr>
		    <td align=center>
			Name
		    <td align=center>
			Value
	    
		<?php if (count($_from = (array)$this->_tpl_vars['attrs'])):
    foreach ($_from as $this->_tpl_vars['attr_name'] => $this->_tpl_vars['attr_value']):
?>
		    <tr>
			<td>
			    <?php echo $this->_tpl_vars['attr_name']; ?>

			<td>
			    <?php if ($this->_tpl_vars['attr_editing']): ?>
				<input type=text name="attr__<?php echo $this->_tpl_vars['attr_name']; ?>
" value="<?php echo $this->_tpl_vars['attr_value']; ?>
">
			    <?php else: ?>
				<?php echo $this->_tpl_vars['attr_value']; ?>

			    <?php endif; ?>
		<?php endforeach; unset($_from); endif; ?>
	    </table>
	<td>
	    <table border=1>
		<tr>
		    <td colspan=4 align=center>
			Ports
		<tr>
		    <td align=center>
			Port Name
		    <td align=center>
			Type
		    <td align=center>
			Phone
		    <td align=center>
			Comment

		<?php if (count($_from = (array)$this->_tpl_vars['ports'])):
    foreach ($_from as $this->_tpl_vars['port_info']):
?>
		    <tr>
			<td>
			    <?php echo $this->_tpl_vars['port_info']['port_name']; ?>

			<td>
			    <?php echo $this->_tpl_vars['port_info']['type']; ?>

			<td>
			    <?php echo $this->_tpl_vars['port_info']['phone']; ?>

			<td>
			    <?php echo $this->_tpl_vars['port_info']['comment']; ?>

			<?php if (! $this->_tpl_vars['is_editing'] && ! $this->_tpl_vars['attr_editing'] && $this->_tpl_vars['can_change']): ?>
			    <td>
				<a href="/IBSng/admin/ras/ras_info.php?ras_ip=<?php echo ((is_array($_tmp=$this->_tpl_vars['info']['ras_ip'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
&del_port=<?php echo ((is_array($_tmp=$this->_tpl_vars['port_info']['port_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
" <?php echo smarty_function_jsconfirm(array('msg' => "Are you sure you want to delete port ".($this->_tpl_vars['port_info']['port_name'])), $this);?>
>
				    del
				</a>

			    <td>
				<a href="/IBSng/admin/ras/edit_port.php?ras_ip=<?php echo ((is_array($_tmp=$this->_tpl_vars['info']['ras_ip'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
&port_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['port_info']['port_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">
				    edit
				</a>
			<?php endif; ?>
		<?php endforeach; unset($_from); endif; ?>

	    </table>
	    
</table>
<table>
<?php if (! $this->_tpl_vars['is_editing'] && ! $this->_tpl_vars['attr_editing'] && $this->_tpl_vars['can_change']): ?>
    <table>
	<tr>
	    <td>
		<a href="/IBSng/admin/ras/ras_info.php?ras_ip=<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
&edit=1">
		    Edit Ras Informations
		</a>
	<tr>
	    <td>
		<a href="/IBSng/admin/ras/ras_info.php?ras_ip=<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
&edit_attrs=1">
		    Edit Ras Attributes
		</a>

	<tr>
	    <td>
		<a href="/IBSng/admin/ras/ras_info.php?ras_ip=<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
&reset_attrs=1" <?php echo smarty_function_jsconfirm(array('msg' => "Reset attributes of ras ".($this->_tpl_vars['info']['ras_ip'])." to default?"), $this);?>
>
		    Reset Ras Attributes To Default
		</a>

	<tr>
	    <td>
		<a href="/IBSng/admin/ras/add_port.php?ras_ip=<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
">
		    Add Port(s)
		</a>

	<tr>
	    <td>
				<form method=POST action="/IBSng/admin/ras/ras_info.php" name=del_port>
				<input type=hidden name=ras_ip value="<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
">
		    Del Port(s): <input type=text name=del_port> <?php echo smarty_function_multistr(array('form_name' => 'del_port','input_name' => 'del_port'), $this);?>

				<input type=submit value=del <?php echo smarty_function_jsconfirm(array('msg' => "Are you sure?"), $this);?>
>
				</form>


	<tr>
	    <td>
				<form method=POST action="/IBSng/admin/ras/edit_port.php" name=edit_port>
				<input type=hidden name=ras_ip value="<?php echo $this->_tpl_vars['info']['ras_ip']; ?>
">
		    Edit Port(s): <input type=text name=port_name> <?php echo smarty_function_multistr(array('form_name' => 'edit_port','input_name' => 'port_name'), $this);?>

				<input type=submit value=edit>
				</form>


    </table>
<?php else: ?>
    <input type=submit name=submit>
    </form>
<?php endif; ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>