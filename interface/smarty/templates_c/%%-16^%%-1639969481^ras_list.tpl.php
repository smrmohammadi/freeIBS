<?php /* Smarty version 2.6.2, created on 2004-07-17 19:24:29
         compiled from admin/ras/ras_list.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'helpicon', 'admin/ras/ras_list.tpl', 29, false),array('modifier', 'escape', 'admin/ras/ras_list.tpl', 51, false),)), $this); ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Ras List')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
<?php if (isset ( $this->_tpl_vars['deactive_success'] ) && $this->_tpl_vars['deactive_success']): ?>
    <h2>
	Ras DeActivated Successfully
    </h2>
<?php endif; ?>

<?php if (isset ( $this->_tpl_vars['reactive_success'] ) && $this->_tpl_vars['reactive_success']): ?>
    <h2>
	Ras ReActivated Successfully
    </h2>
<?php endif; ?>

    <table>
	<tr>	
	    <th bgcolor=gray colspan=7>
		<h2>Active Rases</2> 
	<tr>
	    <th colspan=7>
	    	<?php echo smarty_function_helpicon(array('subject' => 'deactive ras','category' => 'ras','body' => 'Help On Deactive Ras'), $this);?>

	<tr>
	    <th>
		ID
	    <th>
		Ras IP
	    <th>
		Type
	    <th>
		Radius Secret
		
	<?php if (count($_from = (array)$this->_tpl_vars['ras_infos'])):
    foreach ($_from as $this->_tpl_vars['ras_info']):
?>
	    <tr>
		<td>
		    <?php echo $this->_tpl_vars['ras_info']['ras_id']; ?>

		<td>
		    <?php echo $this->_tpl_vars['ras_info']['ras_ip']; ?>

		<td>
		    <?php echo $this->_tpl_vars['ras_info']['ras_type']; ?>

		<td>
		    <?php echo $this->_tpl_vars['ras_info']['radius_secret']; ?>

		<td>
		    <a href="/IBSng/admin/ras/ras_info.php?ras_ip=<?php echo ((is_array($_tmp=$this->_tpl_vars['ras_info']['ras_ip'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">
			info
		    </a>
		<?php if ($this->_tpl_vars['can_change']): ?>
	    	    <td>
			<a href="/IBSng/admin/ras/ras_list.php?deactive=<?php echo ((is_array($_tmp=$this->_tpl_vars['ras_info']['ras_ip'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">
			    DeActive
			</a> 
		    <td>

		<?php endif; ?>
	<?php endforeach; unset($_from); endif; ?>

	<tr>	
	    <th bgcolor=gray colspan=7>
		<h2>INActive Rases</2> 
	<tr>
	    <th colspan=7>
	    	<?php echo smarty_function_helpicon(array('subject' => 'reactive ras','category' => 'ras','body' => 'Help On Reactive Ras'), $this);?>

	<?php if (count($_from = (array)$this->_tpl_vars['inactive_ras_infos'])):
    foreach ($_from as $this->_tpl_vars['ras_info']):
?>
	    <tr>
		<td>
		    <?php echo $this->_tpl_vars['ras_info']['ras_id']; ?>

		<td>
		    <?php echo $this->_tpl_vars['ras_info']['ras_ip']; ?>

		<td>
		    <?php echo $this->_tpl_vars['ras_info']['ras_type']; ?>

		<td>
		    <?php echo $this->_tpl_vars['ras_info']['radius_secret']; ?>

		<td>
		
		<?php if ($this->_tpl_vars['can_change']): ?>
	    	    <td>
			<a href="/IBSng/admin/ras/ras_list.php?reactive=<?php echo ((is_array($_tmp=$this->_tpl_vars['ras_info']['ras_ip'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
">
			    ReActive
			</a>
		    <td>
		<?php endif; ?>

	<?php endforeach; unset($_from); endif; ?>
    </table>


</center>
</form>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>