<?php /* Smarty version 2.6.2, created on 2004-07-17 19:23:46
         compiled from admin/charge/charge_info.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'strip', 'admin/charge/charge_info.tpl', 83, false),array('modifier', 'escape', 'admin/charge/charge_info.tpl', 114, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Charge Information')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
<?php if (isset ( $this->_tpl_vars['update_success'] ) && $this->_tpl_vars['update_success']): ?>
    <h2>
	Charge Updated Successfully
    </h2>        
<?php endif; ?>

<?php if (isset ( $this->_tpl_vars['del_charge_rule_success'] ) && $this->_tpl_vars['del_charge_rule_success']): ?>
    <h2>
	Charge Rule Deleted Successfully
    </h2>        
<?php endif; ?>


<?php if (isInRequest ( 'update_charge_rule_success' )): ?>
    <h2>
	Charge Rule Updated Successfully
    </h2>        
<?php endif; ?>



<?php if ($this->_tpl_vars['is_editing']): ?>
    <form action="/IBSng/admin/charge/charge_info.php" method=POST>
    <input name=charge_id value="<?php echo $this->_tpl_vars['charge_id']; ?>
" type=hidden>
    <input name=old_charge_name value="<?php echo $this->_tpl_vars['charge_name']; ?>
" type=hidden>
<?php endif; ?>

<table>
    <tr>
	<td>
	    Charge Name:
	<td>
	    <?php if ($this->_tpl_vars['is_editing']): ?>
		<input type=text name=charge_name value="<?php echo $this->_tpl_vars['charge_name']; ?>
">
	    <?php else: ?>
        	<?php echo $this->_tpl_vars['charge_name']; ?>

	    <?php endif; ?>
	<td>
	    Charge ID:
	<td>
	    <?php echo $this->_tpl_vars['charge_id']; ?>

    <tr>
	<td>
	    Charge Type:
	<td>
		<?php echo $this->_tpl_vars['charge_type']; ?>

	<td>
	    Visible To All:
	<td>
	    <?php if ($this->_tpl_vars['is_editing']): ?>
		<input type=checkbox name=visible_to_all <?php echo $this->_tpl_vars['visible_to_all_checked']; ?>
>
	    <?php else: ?>
		<?php echo $this->_tpl_vars['visible_to_all']; ?>

	    <?php endif; ?>

    <tr>
	<td>
	    Comment:
	<td>
	    <?php if ($this->_tpl_vars['is_editing']): ?>
		<textarea name=comment><?php echo ((is_array($_tmp=$this->_tpl_vars['comment'])) ? $this->_run_mod_handler('strip', true, $_tmp) : smarty_modifier_strip($_tmp)); ?>
</textarea>
	    <?php else: ?>
		<?php echo $this->_tpl_vars['comment']; ?>

	    <?php endif; ?>
	<td>
	    Creator Admin:
	<td>
	    <?php echo $this->_tpl_vars['creator']; ?>

	    
</table>

<?php if ($this->_tpl_vars['is_editing']): ?>
    <input type=submit value=change>
    </form>
<?php endif; ?>

</center>

<?php if (! $this->_tpl_vars['is_editing']): ?>
    <?php if ($this->_tpl_vars['charge_type'] == 'Internet'): ?>
	<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin/charge/internet_charge_rule_list.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <?php else: ?>
    
    <?php endif; ?>

<?php endif; ?>

<?php if (! $this->_tpl_vars['is_editing'] && $this->_tpl_vars['can_change']): ?>
<table>
    <tr>
	<td>
	    <a href="/IBSng/admin/charge/charge_info.php?charge_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['charge_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
&edit=1">
		Edit
	    </a>
    <tr>
	<td>
	    <a href="/IBSng/admin/charge/<?php if ($this->_tpl_vars['charge_type'] == 'Internet'): ?>add_internet_charge_rule<?php else: ?>add_voip_charge_rule<?php endif; ?>.php?charge_name=<?php echo ((is_array($_tmp=$this->_tpl_vars['charge_name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">
		Add Charge Rule
	    </a>

<?php endif; ?>


<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>