{viewTable title="Persistent Lan" table_width="380" nofoot="TRUE"} 
    {addEditTD type="left"}
	{canDo perm_name="CHANGE NORMAL USER ATTRIBUTES"}
	    {editCheckBox edit_tpl_name="persistent_lan"}
	{/canDo}
	Persistent Lan Mac
    {/addEditTD}

    {addEditTD type="right"}
	{ifHasAttr var_name="persistent_lan_mac" object="user"}
	    {$user_attrs.persistent_lan_mac}
	{/ifHasAttr}
	{helpicon subject="persistent lan mac" category="user"}
    {/addEditTD}

    {addEditTD type="left"}
	Persistent Lan IP
    {/addEditTD}

    {addEditTD type="right"}
	{ifHasAttr var_name="persistent_lan_ip" object="user"}
	    {$user_attrs.persistent_lan_ip}
	{/ifHasAttr}
	{helpicon subject="persistent lan ip" category="user"}
    {/addEditTD}

    {addEditTD type="left"}
	Persistent Lan Ras IP
    {/addEditTD}

    {addEditTD type="right"}
	{ifHasAttr var_name="persistent_lan_ras_ip" object="user"}
	    {$user_attrs.persistent_lan_ras_ip}
	{/ifHasAttr}
	{helpicon subject="persistent lan ras ip" category="user"}
    {/addEditTD}
{/viewTable}
