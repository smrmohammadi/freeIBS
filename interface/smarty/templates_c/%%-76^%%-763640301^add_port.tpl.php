<?php /* Smarty version 2.6.2, created on 2004-07-17 19:27:34
         compiled from admin/ras/add_port.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'helpicon', 'admin/ras/add_port.tpl', 20, false),array('function', 'ifibserr', 'admin/ras/add_port.tpl', 28, false),array('function', 'multistr', 'admin/ras/add_port.tpl', 35, false),array('function', 'html_options', 'admin/ras/add_port.tpl', 43, false),array('modifier', 'strip', 'admin/ras/add_port.tpl', 63, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add Port To Ras')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<form method=POST name=add_port>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add Port To Ras <?php echo smarty_function_helpicon(array('subject' => 'add ras port','category' => 'ras'), $this);?>

	<tr>
	    <td>
		Ras IP:
	    <td>
		<?php echo $this->_tpl_vars['ras_ip']; ?>

	    <td>
	    
	<tr <?php echo smarty_function_ifibserr(array('varname' => 'port_name_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Port Name:
	    <td>
		<input type=text name=port_name value="<?php echo $this->_tpl_vars['port_name']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'port name','category' => 'ras'), $this);?>

		<?php echo smarty_function_multistr(array('form_name' => 'add_port','input_name' => 'port_name'), $this);?>



	<tr <?php echo smarty_function_ifibserr(array('varname' => 'port_type_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Port Type:
	    <td>
		<select name=port_type>
		    <?php echo smarty_function_html_options(array('output' => $this->_tpl_vars['port_types'],'values' => $this->_tpl_vars['port_types'],'default' => $this->_tpl_vars['port_type']), $this);?>

		</select>
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'port type','category' => 'ras'), $this);?>



	<tr <?php echo smarty_function_ifibserr(array('varname' => 'phone_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Phone no.:
	    <td>
		<input type=text name=phone value="<?php echo $this->_tpl_vars['phone']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'phone','category' => 'ras'), $this);?>

		<?php echo smarty_function_multistr(array('form_name' => 'add_port','input_name' => 'phone'), $this);?>


	<tr <?php echo smarty_function_ifibserr(array('varname' => 'comment_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    <?php echo ((is_array($_tmp=$this->_tpl_vars['comment'])) ? $this->_run_mod_handler('strip', true, $_tmp) : smarty_modifier_strip($_tmp)); ?>

		</textarea>
	    <td>
		<?php echo smarty_function_multistr(array('form_name' => 'add_port','input_name' => 'comment'), $this);?>

	<tr>
	    <td colspan=2>
		<input type=submit name=submit>

    </table>
</center>
</form>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>