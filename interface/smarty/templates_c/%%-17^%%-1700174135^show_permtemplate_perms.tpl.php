<?php /* Smarty version 2.6.2, created on 2004-05-25 17:02:29
         compiled from admin/admins/show_permtemplate_perms.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'config_load', 'admin/admins/show_permtemplate_perms.tpl', 4, false),array('modifier', 'capitalize', 'admin/admins/show_permtemplate_perms.tpl', 13, false),array('modifier', 'truncate', 'admin/admins/show_permtemplate_perms.tpl', 53, false),)), $this); ?>
<?php echo smarty_function_config_load(array('file' => "perm_category_names.conf"), $this);?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "header.tpl", 'smarty_include_vars' => array('title' => 'Template Permission List')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

    

<center>

    <h2> 
	Template "<?php echo ((is_array($_tmp=$this->_tpl_vars['template_name'])) ? $this->_run_mod_handler('capitalize', true, $_tmp) : smarty_modifier_capitalize($_tmp)); ?>
" Permission List
    </h2>
    <?php if (count($_from = (array)$this->_tpl_vars['perms'])):
    foreach ($_from as $this->_tpl_vars['category'] => $this->_tpl_vars['cat_perms']):
?>
	<table>
	    <tr>
		<td>
		    Category: <?php echo $this->_tpl_vars['category_names'][$this->_tpl_vars['category']]; ?>

	    <tr>
		<td>
		    <table border=1>
			<tr>
			    <th>
				Name
			    <th>
				Value
			    <th>
				Description
			

	    <?php if (isset($this->_sections['index'])) unset($this->_sections['index']);
$this->_sections['index']['loop'] = is_array($_loop=$this->_tpl_vars['cat_perms']) ? count($_loop) : max(0, (int)$_loop); unset($_loop);
$this->_sections['index']['name'] = 'index';
$this->_sections['index']['show'] = true;
$this->_sections['index']['max'] = $this->_sections['index']['loop'];
$this->_sections['index']['step'] = 1;
$this->_sections['index']['start'] = $this->_sections['index']['step'] > 0 ? 0 : $this->_sections['index']['loop']-1;
if ($this->_sections['index']['show']) {
    $this->_sections['index']['total'] = $this->_sections['index']['loop'];
    if ($this->_sections['index']['total'] == 0)
        $this->_sections['index']['show'] = false;
} else
    $this->_sections['index']['total'] = 0;
if ($this->_sections['index']['show']):

            for ($this->_sections['index']['index'] = $this->_sections['index']['start'], $this->_sections['index']['iteration'] = 1;
                 $this->_sections['index']['iteration'] <= $this->_sections['index']['total'];
                 $this->_sections['index']['index'] += $this->_sections['index']['step'], $this->_sections['index']['iteration']++):
$this->_sections['index']['rownum'] = $this->_sections['index']['iteration'];
$this->_sections['index']['index_prev'] = $this->_sections['index']['index'] - $this->_sections['index']['step'];
$this->_sections['index']['index_next'] = $this->_sections['index']['index'] + $this->_sections['index']['step'];
$this->_sections['index']['first']      = ($this->_sections['index']['iteration'] == 1);
$this->_sections['index']['last']       = ($this->_sections['index']['iteration'] == $this->_sections['index']['total']);
?>
	    <tr>
		<td>

		    <?php echo $this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['name']; ?>

		<td>
		    <?php if ($this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['value_type'] == 'NOVALUE'): ?>
			No Value
		    <?php elseif ($this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['value_type'] == 'SINGLEVALUE'): ?>
			<?php echo $this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['value']; ?>
 
		    <?php elseif ($this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['value_type'] == 'MULTIVALUE'): ?>
			<table>
			<?php if (count($_from = (array)$this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['value'])):
    foreach ($_from as $this->_tpl_vars['val']):
?>
			    <tr>
				<td>
				    <?php echo $this->_tpl_vars['val']; ?>
 
			<?php endforeach; unset($_from); endif; ?>
			</table>
			    			
		    <?php endif; ?>
		<td>
		    <?php echo ((is_array($_tmp=$this->_tpl_vars['cat_perms'][$this->_sections['index']['index']]['description'])) ? $this->_run_mod_handler('truncate', true, $_tmp, 50) : smarty_modifier_truncate($_tmp, 50)); ?>

	    <?php endfor; endif; ?>
		    </table>
	
	</table>
    <?php endforeach; unset($_from); endif;  echo '
<script language="javascript">
    window.focus();
</script>
'; ?>


<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>