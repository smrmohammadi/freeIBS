<?php /* Smarty version 2.6.2, created on 2004-07-17 19:24:37
         compiled from admin/ras/add_new_ras.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'helpicon', 'admin/ras/add_new_ras.tpl', 18, false),array('function', 'ifibserr', 'admin/ras/add_new_ras.tpl', 19, false),array('function', 'html_options', 'admin/ras/add_new_ras.tpl', 32, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add New Ras')));
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
		Add New Ras <?php echo smarty_function_helpicon(array('subject' => 'add new ras','category' => 'ras'), $this);?>

	<tr <?php echo smarty_function_ifibserr(array('varname' => 'ras_ip_err','add' => "bgcolor=red"), $this);?>
 >
	    <td>
		Ras IP:
	    <td>
		<input type=text name=ras_ip value="<?php echo $this->_tpl_vars['ras_ip']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'ras ip','category' => 'ras'), $this);?>

	    
	<tr <?php echo smarty_function_ifibserr(array('varname' => 'ras_type_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Ras Type:
	    <td>
		<select name=ras_type>
		    <?php echo smarty_function_html_options(array('output' => $this->_tpl_vars['ras_types'],'values' => $this->_tpl_vars['ras_types'],'default' => $this->_tpl_vars['ras_type']), $this);?>

		</select>
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'ras type','category' => 'ras'), $this);?>



	<tr <?php echo smarty_function_ifibserr(array('varname' => 'radius_secret_err','add' => "bgcolor=red"), $this);?>
>
	    <td>
		Radius Secret
	    <td>
		<input type=text name=radius_secret value="<?php echo $this->_tpl_vars['radius_secret']; ?>
">
	    <td>
		<?php echo smarty_function_helpicon(array('subject' => 'radius secret','category' => 'ras'), $this);?>


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