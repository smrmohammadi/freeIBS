<script language="javascript">
    attrs=new CheckBoxContainer();
</script>
{listTable no_header=TRUE no_foot=TRUE table_width="100%"} 
    {listTableHeader cols_num=30 type="left"}
	Attributes to Show/Edit
    {/listTableHeader}
    {listTableHeader type="right"}
	<table cellpadding=0 cellspacing=0 border=0 class="List_Top_line" align="right">
	<tr>
	    <td><input style="height:11" type=checkbox name=attrs_check_all></td>
	    <td>Check All Attributes</td>	
	</tr>
	</table>
    {/listTableHeader}
        <tr><td colspan=30>
	{multiTable}
	{multiTableTR}
	    {reportToShowCheckBox name="show__normal_username" output="Normal Username" default_checked="TRUE" always_in_form="search" value="normal_username" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__credit" output="Credit" default_checked="TRUE" always_in_form="search" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__group" output="Group" default_checked="TRUE" always_in_form="search" value="group_name" form_name="search_user" container_name="attrs"}
        {multiTableTR}
	    {reportToShowCheckBox name="show__owner" output="Owner" default_checked="TRUE" always_in_form="search" value="owner_name" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__creation_date" output="Creation Date" default_checked="FALSE" always_in_form="search" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__rel_exp_date" output="Relative ExpDate" default_checked="FALSE" always_in_form="search" value="rel_exp_date" form_name="search_user" container_name="attrs"}
        {multiTableTR}
	    {reportToShowCheckBox name="show__abs_exp_date" output="Absolute ExpDate" default_checked="FALSE" always_in_form="search" value="abs_exp_date" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__multi_login" output="Multi Login" default_checked="FALSE" always_in_form="search" value="multi_login" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__normal_charge" output="Normal Charge" default_checked="FALSE" always_in_form="search" value="normal_charge" form_name="search_user" container_name="attrs"}
        {multiTableTR}
	    {reportToShowCheckBox name="show__lock" output="Lock Status" default_checked="FALSE" always_in_form="search" value="normal_charge" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__ippool" output="*IPpool" default_checked="FALSE" always_in_form="search" value="ippool" form_name="search_user" container_name="attrs"}
	    {reportToShowCheckBox name="show__comment" output="*Comment" default_checked="FALSE" always_in_form="search" value="comment" form_name="search_user" container_name="attrs"}
	{/multiTable}
{/listTable}
<script language="javascript">
    attrs.setCheckAll('search_user','attrs_check_all');
</script>
	    