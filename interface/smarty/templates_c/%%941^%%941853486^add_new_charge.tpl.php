<?php /* Smarty version 2.6.2, created on 2004-05-13 10:57:16
         compiled from admin/charge/add_new_charge.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'helpicon', 'admin/charge/add_new_charge.tpl', 19, false),array('function', 'ifibserr', 'admin/charge/add_new_charge.tpl', 20, false),array('function', 'html_options', 'admin/charge/add_new_charge.tpl', 33, false),array('modifier', 'strip', 'admin/charge/add_new_charge.tpl', 44, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add New Charge')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<form method=POST>
<center>
    <table>
	<tr>	
	    <td colspan=2 align=center>
		Add New Charge <?php echo smarty_function_helpicon(array('subject' => 'add new charge','category' => 'charge'), $this);?>

	<tr <?php echo smarty_function_ifibserr(array('varname' => 'charge_name_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Charge Name:
	    <td>
		<input type=text name=charge_name value="<?php echo $this->_tpl_vars['charge_name']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'charge name','category' => 'charge'), $this);?>

	    
	<tr <?php echo smarty_function_ifibserr(array('varname' => 'charge_type_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Charge Type:
	    <td>
		<select name=charge_type>
		    <?php echo smarty_function_html_options(array('output' => $this->_tpl_vars['charge_types'],'values' => $this->_tpl_vars['charge_types'],'default' => $this->_tpl_vars['charge_type']), $this);?>

		</select>
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'charge type','category' => 'charge'), $this);?>



	<tr <?php echo smarty_function_ifibserr(array('varname' => 'comment_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Comment:
	    <td>
		<textarea name=comment>
		    <?php echo ((is_array($_tmp=$this->_tpl_vars['comment'])) ? $this->_run_mod_handler('strip', true, $_tmp) : smarty_modifier_strip($_tmp)); ?>

		</textarea>
	    <td>

	<tr <?php echo smarty_function_ifibserr(array('varname' => 'visible_to_all_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Visible To All
	    <td>
		<input type=checkbox name=visible_to_all <?php echo $this->_tpl_vars['visible_to_all']; ?>
>
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'visible to all','category' => 'charge'), $this);?>

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