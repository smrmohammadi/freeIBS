<?php /* Smarty version 2.6.2, created on 2004-05-13 12:07:38
         compiled from admin/charge/internet_charge_rule_list.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'escape', 'admin/charge/internet_charge_rule_list.tpl', 62, false),array('function', 'jsconfirm', 'admin/charge/internet_charge_rule_list.tpl', 66, false),)), $this); ?>
<table border=1>
    <tr>
	<th>
	    Rule ID
	<th>
	    Start Time
	<th>
	    End Time
	<th>
	    CPM
	<th>
	    CPK
	<th>
	    Assumed KPS
	<th>
	    bandwidth_limit(kbytes)

	<th>
	    Ras
	<th>
	    Ports
	<th>
	    Day Of Weeks

<?php if (count($_from = (array)$this->_tpl_vars['rules'])):
    foreach ($_from as $this->_tpl_vars['rule']):
?>
<tr>
    <td>
	<?php echo $this->_tpl_vars['rule']['rule_id']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['start_time']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['end_time']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['cpm']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['cpk']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['assumed_kps']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['bandwidth_limit']; ?>

    <td>
	<?php echo $this->_tpl_vars['rule']['ras']; ?>

    <td>
        <table>
    	    <tr>
	    <?php if (count($_from = (array)($this->_tpl_vars['rule']['ports']))):
    foreach ($_from as $this->_tpl_vars['port']):
?>
		<td>
		    <?php echo $this->_tpl_vars['port']; ?>

	    <?php endforeach; unset($_from); endif; ?>
	</table}

    <td>
        <table>
    	    <tr>
	    <?php if (count($_from = (array)($this->_tpl_vars['rule']['day_of_weeks']))):
    foreach ($_from as $this->_tpl_vars['day_name']):
?>
		<td>
		    <?php echo $this->_tpl_vars['day_name']; ?>

	    <?php endforeach; unset($_from); endif; ?>
	</table}
    <td>
    <?php if ($this->_tpl_vars['can_change']): ?>
	<a href="/IBSng/admin/charge/edit_internet_charge_rule.php?charge_rule_id=<?php echo $this->_tpl_vars['rule']['rule_id']; ?>
&charge_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['charge_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">Edit</a>
    <?php endif; ?>
    <td>
    <?php if ($this->_tpl_vars['can_change']): ?>
        <a <?php echo smarty_function_jsconfirm(array('msg' => "Are you sure you want to delete charge rule with id ".($this->_tpl_vars['rule']['rule_id'])), $this);?>
 href="/IBSng/admin/charge/charge_info.php?charge_rule_id=<?php echo $this->_tpl_vars['rule']['rule_id']; ?>
&charge_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['charge_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
&delete_charge_rule=1">Delete</a>
    <?php endif; ?>
		
<?php endforeach; unset($_from); endif; ?>
</table>