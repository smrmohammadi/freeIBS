<?php /* Smarty version 2.6.2, created on 2004-05-23 13:02:20
         compiled from admin/admins/show_perms.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'config_load', 'admin/admins/show_perms.tpl', 4, false),array('function', 'eval', 'admin/admins/show_perms.tpl', 20, false),array('function', 'html_options', 'admin/admins/show_perms.tpl', 84, false),array('modifier', 'nl2br', 'admin/admins/show_perms.tpl', 39, false),array('modifier', 'escape', 'admin/admins/show_perms.tpl', 107, false),array('modifier', 'truncate', 'admin/admins/show_perms.tpl', 111, false),)), $this); ?>
<?php echo smarty_function_config_load(array('file' => "perm_category_names.conf"), $this);?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Add Permission to admin')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    

<center>
<?php if ($this->_tpl_vars['add_success'] == TRUE): ?>
    <h3>
	Permission Added Successfully
    </h3>
<?php endif; ?>
	

    <h2> 
	Adding permission to <?php echo $this->_tpl_vars['admin_username']; ?>
 <a href="/IBSng/admin/admins/admin_perms_list.php?admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
">Permission List</a>
    </h2>
	Category : <?php echo smarty_function_eval(array('var' => $this->_tpl_vars['category_name']), $this);?>

    <table border=1>
	<tr>
	    <th>
		Name
	    <th>
		Description
	    <th>
		Affected Pages
	    <th>
		Dependencies
	<?php if (count($_from = (array)$this->_tpl_vars['perms'])):
    foreach ($_from as $this->_tpl_vars['perm']):
?>

	    <?php if ($this->_tpl_vars['perm']['name'] == $this->_tpl_vars['selected']): ?>
		<a name="selected">
		<tr bgcolor=#0a9ffc>
		    <td>
			<nobr><?php echo $this->_tpl_vars['perm']['name']; ?>
</nobr>
		    <td>
			<?php echo ((is_array($_tmp=$this->_tpl_vars['perm']['description'])) ? $this->_run_mod_handler('nl2br', true, $_tmp) : smarty_modifier_nl2br($_tmp)); ?>
  
		    <td>
			<?php if (count($_from = (array)$this->_tpl_vars['perm']['affected_pages'])):
    foreach ($_from as $this->_tpl_vars['affected_page']):
?>
			    <nobr><?php echo $this->_tpl_vars['affected_page']; ?>
</nobr><br>
			<?php endforeach; unset($_from); endif; ?>
		    <td>
			<?php if (count($_from = (array)$this->_tpl_vars['perm']['dependencies'])):
    foreach ($_from as $this->_tpl_vars['dependency']):
?>
			    <nobr><?php echo $this->_tpl_vars['dependency']; ?>
</nobr><br>
			<?php endforeach; unset($_from); endif; ?>
		<tr bgcolor=#0a9ffc>
		    <form action=/IBSng/admin/admins/show_perms.php>
    		    <input type=hidden name=admin_username value="<?php echo $this->_tpl_vars['admin_username']; ?>
">
		    <input type=hidden name=category value="<?php echo $this->_tpl_vars['category']; ?>
">
		    <input type=hidden name=perm_name value="<?php echo $this->_tpl_vars['selected']; ?>
">
		    <input type=hidden name=selected value="<?php echo $this->_tpl_vars['selected']; ?>
">
		    <td colspan=5>
			<table border=1 width=100%>
			    <tr>
				<td>
				    Admin Has this Permission: 
					<?php if ($this->_tpl_vars['has_selected_perm'] == TRUE): ?> Yes <br> Current Value: 
					    <?php if ($this->_tpl_vars['perm']['value_type'] == 'NOVALUE'): ?>
						Permission doesn't need value
					    <?php elseif ($this->_tpl_vars['cur_val'] == ""): ?>
						Empty
					    <?php elseif (is_array ( $this->_tpl_vars['cur_val'] )): ?>
    						<table>
						    <tr>
						<?php if (count($_from = (array)$this->_tpl_vars['cur_val'])):
    foreach ($_from as $this->_tpl_vars['val']):
?>
						    <td>	    
							<?php echo $this->_tpl_vars['val']; ?>

						<?php endforeach; unset($_from); endif; ?>
						</table>
					    <?php else: ?>
						<?php echo $this->_tpl_vars['cur_val']; ?>

					    <?php endif; ?>
					<?php else: ?> 
					    No 
					<?php endif; ?>

		    <?php if ($this->_tpl_vars['can_change'] == TRUE && $this->_tpl_vars['perm']['value_type'] == 'SINGLEVALUE' || $this->_tpl_vars['perm']['value_type'] == 'MULTIVALUE'): ?>
			<td>
			    New Value:
			<?php if (isset ( $this->_tpl_vars['perm']['value_candidates'] )): ?>
			    <select name="value">
				<?php echo smarty_function_html_options(array('values' => $this->_tpl_vars['perm']['value_candidates'],'output' => $this->_tpl_vars['perm']['value_candidates'],'selected' => $this->_tpl_vars['selected_value']), $this);?>

			    </select>
			<?php else: ?>
			    <input type=text name=value 
			    <?php if ($this->_tpl_vars['selected_value'] != ""): ?>
				value="<?php echo $this->_tpl_vars['selected_value']; ?>
"
			    <?php elseif ($this->_tpl_vars['perm']['value_type'] == 'SINGLEVALUE' && $this->_tpl_vars['has_selected_perm'] == TRUE): ?> 
				value="<?php echo $this->_tpl_vars['cur_val']; ?>
" 
			    <?php endif; ?> 
			    >
			<?php endif; ?>


		    <?php endif; ?>
			<td>
			    <input type=submit name="submit" value="Add This Permission">
			    

		    </table>

	    <?php else: ?>
		<tr>
		    <td>
			<a href="/IBSng/admin/admins/show_perms.php?category=<?php echo $this->_tpl_vars['category']; ?>
&admin_username=<?php echo $this->_tpl_vars['admin_username']; ?>
&selected=<?php echo ((is_array($_tmp=$this->_tpl_vars['perm']['name'])) ? $this->_run_mod_handler('escape', true, $_tmp, 'url') : smarty_modifier_escape($_tmp, 'url')); ?>
#selected">
			    <nobr><?php echo $this->_tpl_vars['perm']['name']; ?>
</nobr>
			</a>
		    <td>
			<?php echo ((is_array($_tmp=((is_array($_tmp=$this->_tpl_vars['perm']['description'])) ? $this->_run_mod_handler('nl2br', true, $_tmp) : smarty_modifier_nl2br($_tmp)))) ? $this->_run_mod_handler('truncate', true, $_tmp, 150, "...", false) : smarty_modifier_truncate($_tmp, 150, "...", false)); ?>

		    <td>
			<?php if (count($_from = (array)$this->_tpl_vars['perm']['affected_pages'])):
    foreach ($_from as $this->_tpl_vars['affected_page']):
?>
			    <nobr><?php echo $this->_tpl_vars['affected_page']; ?>
</nobr><br>
			<?php endforeach; unset($_from); endif; ?>
		    <td>
			<?php if (count($_from = (array)$this->_tpl_vars['perm']['dependencies'])):
    foreach ($_from as $this->_tpl_vars['dependency']):
?>
			    <nobr><?php echo $this->_tpl_vars['dependency']; ?>
</nobr><br>
			<?php endforeach; unset($_from); endif; ?>
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