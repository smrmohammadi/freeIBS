<?php /* Smarty version 2.6.2, created on 2004-05-13 11:41:46
         compiled from admin/charge/add_internet_charge_rule.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'ifibserr', 'admin/charge/add_internet_charge_rule.tpl', 31, false),array('function', 'ifisinrequest', 'admin/charge/add_internet_charge_rule.tpl', 37, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add New Internet Charge Rule')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
<form method=POST name=add_internet_rule>
<table border=1>
    <tr>
	<td>
	    Charge Name:
	<td>
	    <?php echo $this->_tpl_vars['charge_name']; ?>

	    <input type=hidden name=charge_name value="<?php echo $this->_tpl_vars['charge_name']; ?>
">
	<td>
	    <?php if ($this->_tpl_vars['is_editing']): ?>
		Charge Rule ID:
	    <?php endif; ?>
	<td>
	    <?php if ($this->_tpl_vars['is_editing']): ?>
		<?php echo $this->_tpl_vars['rule_id']; ?>

		<input type=hidden name=charge_rule_id value="<?php echo $this->_tpl_vars['rule_id']; ?>
">
	    <?php endif; ?>


    <tr>
	<td colspan=4 <?php echo smarty_function_ifibserr(array('varname' => 'dow_err','add' => "bgcolor=red"), $this);?>
>
	    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin/charge/day_of_week_select.tpl", 'smarty_include_vars' => array('form_name' => 'add_internet_rule')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <tr>
	<td <?php echo smarty_function_ifibserr(array('varname' => 'rule_start_err','add' => "bgcolor=red"), $this);?>
>
	    Rule Start Time:
	<td <?php echo smarty_function_ifibserr(array('varname' => 'rule_start_err','add' => "bgcolor=red"), $this);?>
>
	    <input type=text name=rule_start value="<?php echo smarty_function_ifisinrequest(array('name' => 'rule_start','default_var' => 'start_time'), $this);?>
" >

	<td <?php echo smarty_function_ifibserr(array('varname' => 'rule_end_err','add' => "bgcolor=red"), $this);?>
>
	    Rule End Time:
	<td <?php echo smarty_function_ifibserr(array('varname' => 'rule_end_err','add' => "bgcolor=red"), $this);?>
>
	    <input type=text name=rule_end value="<?php echo smarty_function_ifisinrequest(array('name' => 'rule_end','default_var' => 'end_time'), $this);?>
">

    <tr>
	<td <?php echo smarty_function_ifibserr(array('varname' => 'cpm_err','add' => "bgcolor=red"), $this);?>
>
	    Charge Per Minute:
	<td <?php echo smarty_function_ifibserr(array('varname' => 'cpm_err','add' => "bgcolor=red"), $this);?>
>
	    <input type=text name=cpm value="<?php echo smarty_function_ifisinrequest(array('name' => 'cpm','default_var' => 'cpm'), $this);?>
"> <?php echo $this->_tpl_vars['MONEY_UNIT']; ?>

	    
	<td <?php echo smarty_function_ifibserr(array('varname' => 'cpk_err','add' => "bgcolor=red"), $this);?>
>
	    Charge Per KiloByte:
	<td <?php echo smarty_function_ifibserr(array('varname' => 'cpk_err','add' => "bgcolor=red"), $this);?>
>
	    <input type=text name=cpk value="<?php echo smarty_function_ifisinrequest(array('name' => 'cpk','default_var' => 'cpk'), $this);?>
"> <?php echo $this->_tpl_vars['MONEY_UNIT']; ?>


    <tr>
	<td <?php echo smarty_function_ifibserr(array('varname' => 'assumed_kps_err','add' => "bgcolor=red"), $this);?>
>
	    Assumed Kilo Byte Per Second:
	<td <?php echo smarty_function_ifibserr(array('varname' => 'assumed_kps_err','add' => "bgcolor=red"), $this);?>
>
	    <input type=text name=assumed_kps value="<?php echo smarty_function_ifisinrequest(array('name' => 'assumed_kps','default_var' => 'assumed_kps'), $this);?>
"> Kilo Bytes
	    
	<td <?php echo smarty_function_ifibserr(array('varname' => 'bw_limit_err','add' => "bgcolor=red"), $this);?>
>
	    Bandwidth Limit:
	<td <?php echo smarty_function_ifibserr(array('varname' => 'bw_limit_err','add' => "bgcolor=red"), $this);?>
>
	    <input type=text name=bandwidth_limit_kbytes value="<?php echo smarty_function_ifisinrequest(array('name' => 'bandwidth_limit_kbytes','default_var' => 'bandwidth_limit'), $this);?>
"> KB/s

    <tr>
	<td colspan=4>
	    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin/charge/ras_select.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <tr>
	<td colspan=4>
	    <input type=submit value=add>
</table>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>