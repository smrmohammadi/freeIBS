<?php /* Smarty version 2.6.2, created on 2004-07-13 17:04:16
         compiled from admin/admins/admin_info.tpl */ ?>
<?php require_once(SMARTY_DIR . 'core' . DIRECTORY_SEPARATOR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('block', 'canDo', 'admin/admins/admin_info.tpl', 59, false),)), $this); ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Admin Information')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
<center>
<?php if ($this->_tpl_vars['update_success']): ?>
    Admin Info Updates Successfully
<?php endif; ?>
    <table>
	<tr>	
	    <td>
		Admin Username:
	    <td>
		<?php echo $this->_tpl_vars['username']; ?>

	    <td>
		Admin ID:
	    <td>
		<?php echo $this->_tpl_vars['admin_id']; ?>

	<tr>
	    <td>
		Name:
	    <td>
		<?php if ($this->_tpl_vars['is_editing']): ?>
		    <form method=POST action="admin_info.php">
		    <input type=hidden name=admin_username value=<?php echo $this->_tpl_vars['username']; ?>
>
		    <input type=text name=name value="<?php echo $this->_tpl_vars['name']; ?>
">
		<?php else: ?>		
		    <?php echo $this->_tpl_vars['name']; ?>

		<?php endif; ?>
	    <td>
		Creator:
	    <td>
		<?php echo $this->_tpl_vars['creator']; ?>

	<tr>
	    <td>
		Deposit:
	    <td>
		<?php echo $this->_tpl_vars['deposit']; ?>

	    <td>
	    <td>
	<tr>
	    <td>
		Comment:
	    <td colspan=3>
		<?php if ($this->_tpl_vars['is_editing']): ?>
		    <textarea name=comment><?php echo $this->_tpl_vars['comment']; ?>
</textarea>
		<?php else: ?>
		    <?php echo $this->_tpl_vars['comment']; ?>

		<?php endif; ?>
    </table>
</center>
<table>
<?php if (! $this->_tpl_vars['is_editing']): ?>
    <tr>
	<td>
	    <?php $this->_tag_stack[] = array('canDo', array('perm_name' => 'CHANGE USER INFO','username' => $this->_tpl_vars['username'])); smarty_block_canDo($this->_tag_stack[count($this->_tag_stack)-1][1], null, $this, $_block_repeat=true);while ($_block_repeat) { ob_start(); ?>
    		<a href="/IBSng/admin/admins/admin_info.php?edit=1&admin_username=<?php echo $this->_tpl_vars['username']; ?>
">    
		    Edit
		</a>
	    <?php $this->_block_content = ob_get_contents(); ob_end_clean(); echo smarty_block_canDo($this->_tag_stack[count($this->_tag_stack)-1][1], $this->_block_content, $this, $_block_repeat=false); }  array_pop($this->_tag_stack); ?>
    <tr>
	<td>
	    <?php $this->_tag_stack[] = array('canDo', array('perm_name' => 'SEE ADMIN PERMISSIONS','username' => $this->_tpl_vars['username'])); smarty_block_canDo($this->_tag_stack[count($this->_tag_stack)-1][1], null, $this, $_block_repeat=true);while ($_block_repeat) { ob_start(); ?>
    		<a href="/IBSng/admin/admins/admin_perms_list.php?admin_username=<?php echo $this->_tpl_vars['username']; ?>
">    
		    Permissions List
		</a>
	    <?php $this->_block_content = ob_get_contents(); ob_end_clean(); echo smarty_block_canDo($this->_tag_stack[count($this->_tag_stack)-1][1], $this->_block_content, $this, $_block_repeat=false); }  array_pop($this->_tag_stack); ?>

    <tr>
	<td>
	    <?php $this->_tag_stack[] = array('canDo', array('perm_name' => 'CHANGE ADMIN PASSWORD','username' => $this->_tpl_vars['username'])); smarty_block_canDo($this->_tag_stack[count($this->_tag_stack)-1][1], null, $this, $_block_repeat=true);while ($_block_repeat) { ob_start(); ?>
    		<a href="/IBSng/admin/admins/change_password.php?username=<?php echo $this->_tpl_vars['username']; ?>
">    
		    Change Password
		</a>
	    <?php $this->_block_content = ob_get_contents(); ob_end_clean(); echo smarty_block_canDo($this->_tag_stack[count($this->_tag_stack)-1][1], $this->_block_content, $this, $_block_repeat=false); }  array_pop($this->_tag_stack);  else: ?>
    <input type=submit name=submit>
    </form>
<?php endif; ?>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>