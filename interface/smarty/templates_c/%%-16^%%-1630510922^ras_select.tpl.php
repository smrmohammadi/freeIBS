<?php /* Smarty version 2.6.2, created on 2004-05-12 17:42:51
         compiled from admin/charge/ras_select.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'ipescape', 'admin/charge/ras_select.tpl', 19, false),array('function', 'ifisinrequest', 'admin/charge/ras_select.tpl', 25, false),)), $this); ?>
<script language="javascript" src="/IBSng/js/dom_container.js"> </script>
<script language="javascript">
    ras_select=new DomContainer();
    ras_select.setOnSelect("display","");
    ras_select.setOnUnSelect("display","none");
</script>

<table width=100%>
    <tr>
	<td>
	    <input type=radio name=ras value=_ALL_ <?php if ($this->_tpl_vars['ras_selected'] == '_ALL_'): ?> checked <?php endif; ?> onClick='ras_select.select("_ALL_")'> All Rases

	    <div id="_ALL_"></div>
	    <script language="javascript">
		ras_select.addByID("_ALL_");
	    </script>

    <?php if (count($_from = (array)$this->_tpl_vars['rases'])):
    foreach ($_from as $this->_tpl_vars['ras_ip'] => $this->_tpl_vars['ports']):
?>
	<?php echo smarty_function_ipescape(array('ip' => $this->_tpl_vars['ras_ip'],'assign' => 'ras_ip_escaped'), $this);?>


	<tr>
	    <td>
		<input type=radio name=ras value="<?php echo $this->_tpl_vars['ras_ip']; ?>
"  <?php if ($this->_tpl_vars['ras_selected'] == $this->_tpl_vars['ras_ip']): ?> checked <?php endif; ?> onClick='ras_select.select("<?php echo $this->_tpl_vars['ras_ip']; ?>
")'> <?php echo $this->_tpl_vars['ras_ip']; ?>

	    <td>
		<input type=checkbox name="<?php echo $this->_tpl_vars['ras_ip_escaped']; ?>
_ALL_" <?php echo smarty_function_ifisinrequest(array('name' => ($this->_tpl_vars['ras_ip_escaped'])."_ALL_",'default_var' => ($this->_tpl_vars['ras_ip'])."_ALL_",'default' => "",'value' => 'checked'), $this);?>
 > All Ports
    
	<tr id="<?php echo $this->_tpl_vars['ras_ip']; ?>
">
	    <td colspan=2>
		<table width=100%>
		    <?php if (count($_from = (array)$this->_tpl_vars['ports'])):
    foreach ($_from as $this->_tpl_vars['index'] => $this->_tpl_vars['port']):
?>
			<?php if ($this->_tpl_vars['index']%3 == 0): ?>
			    <tr>
			<?php endif; ?>
			<td>
			    <input type=checkbox name="<?php echo $this->_tpl_vars['ras_ip_escaped']; ?>
__<?php echo $this->_tpl_vars['port']['port_name']; ?>
" <?php echo smarty_function_ifisinrequest(array('name' => ($this->_tpl_vars['ras_ip_escaped'])."__".($this->_tpl_vars['port']['port_name']),'default_var' => ($this->_tpl_vars['ras_ip'])."_".($this->_tpl_vars['port']['port_name']),'default' => "",'value' => 'checked'), $this);?>
 > <?php echo $this->_tpl_vars['port']['port_name']; ?>

	
		    <?php endforeach; unset($_from); endif; ?>
		</table>
	    <script language="javascript">
		ras_select.addByID("<?php echo $this->_tpl_vars['ras_ip']; ?>
");
	    </script>
	
    <?php endforeach; unset($_from); endif; ?>
</table>
    <script language="javascript">
	ras_select.select("<?php echo $this->_tpl_vars['ras_selected']; ?>
");
    </script>