<?php /* Smarty version 2.6.2, created on 2004-05-12 17:33:07
         compiled from admin/charge/day_of_week_select.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'ifisinrequest', 'admin/charge/day_of_week_select.tpl', 19, false),)), $this); ?>
<table >
    <?php echo '
    <script language="javascript" src="/IBSng/js/check_box_container.js"></script>
    <script language="javascript">
	var dows=new CheckBoxContainer();
    </script>
    '; ?>

    <tr>
	<td>
	    <input type=checkbox name=checkall > Check All
        
    <?php if (count($_from = (array)$this->_tpl_vars['day_of_weeks'])):
    foreach ($_from as $this->_tpl_vars['index'] => $this->_tpl_vars['day_of_week']):
?>
	<?php if ($this->_tpl_vars['index']%2-1): ?>
	    <tr>
	<?php endif; ?>
	    <td>
		<?php echo $this->_tpl_vars['day_of_week']; ?>

	    <td>
		<input type=checkbox name="<?php echo $this->_tpl_vars['day_of_week']; ?>
" <?php echo smarty_function_ifisinrequest(array('name' => $this->_tpl_vars['day_of_week'],'default_var' => $this->_tpl_vars['day_of_week'],'default' => "",'value' => 'checked'), $this);?>
 >
		<script language="javascript">
		    dows.addByName("<?php echo $this->_tpl_vars['form_name']; ?>
","<?php echo $this->_tpl_vars['day_of_week']; ?>
");
		</script>
    <?php endforeach; unset($_from); endif; ?>
    <script language="javascript">
	    <?php if (isset ( $this->_tpl_vars['check_all_days'] ) && $this->_tpl_vars['check_all_days']): ?>
		dows.checkAll();
	    <?php endif; ?>
	    dows.setCheckAll("<?php echo $this->_tpl_vars['form_name']; ?>
","checkall");
    </script>	    
</table>