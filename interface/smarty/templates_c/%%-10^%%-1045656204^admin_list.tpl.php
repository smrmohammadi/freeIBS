<?php /* Smarty version 2.6.2, created on 2004-07-13 17:04:14
         compiled from admin/admins/admin_list.tpl */ ?>
<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "admin_header.tpl", 'smarty_include_vars' => array('title' => 'Admin List')));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
  $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "err_head.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

<center>
    <table>
	<tr>	
	    <th>
		ID
	    <th>
		Username
	    <th>
		Name
	    <th>
		Deposit
		
	<?php if (isset($this->_sections['index'])) unset($this->_sections['index']);
$this->_sections['index']['name'] = 'index';
$this->_sections['index']['loop'] = is_array($_loop=$this->_tpl_vars['admin_infos']) ? count($_loop) : max(0, (int)$_loop); unset($_loop);
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
		    <?php echo $this->_tpl_vars['admin_infos'][$this->_sections['index']['index']]['admin_id']; ?>

		<td>
		    <?php echo $this->_tpl_vars['admin_infos'][$this->_sections['index']['index']]['username']; ?>

		<td>
		    <?php echo $this->_tpl_vars['admin_infos'][$this->_sections['index']['index']]['name']; ?>

		<td>
		    <?php echo $this->_tpl_vars['admin_infos'][$this->_sections['index']['index']]['deposit']; ?>

		<td>
		    <a href="/IBSng/admin/admins/admin_info.php?admin_username=<?php echo $this->_tpl_vars['admin_infos'][$this->_sections['index']['index']]['username']; ?>
">
			info
		    </a>
	
	<?php endfor; endif; ?>



    </table>
</center>
</form>

<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "footer.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>