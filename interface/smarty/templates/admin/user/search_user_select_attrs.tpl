<script language="javascript">
    attrs=new CheckBoxContainer();
</script>
<table>
    <tr>
	<td colspan=20>
	    <input type=checkbox name=attrs_check_all> Check All Attrs
	</td>
    <tr>
	<td>
	    {reportToShowCheckBox name="show__normal_username" output="Normal Username" default_checked="TRUE" always_in_form="search" value="normal_username" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__credit" output="Credit" default_checked="TRUE" always_in_form="search" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__group" output="Group" default_checked="TRUE" always_in_form="search" value="group_name" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__owner" output="Owner" default_checked="TRUE" always_in_form="search" value="owner_name" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__creation_date" output="Creation Date" default_checked="FALSE" always_in_form="search" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__rel_exp_date" output="Relative Expiration Date" default_checked="FALSE" always_in_form="search" value="rel_exp_date" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__multi_login" output="Multi Login" default_checked="FALSE" always_in_form="search" value="multi_login" form_name="search_user" container_name="attrs"}
	<td>
	    {reportToShowCheckBox name="show__normal_charge" output="Normal Charge" default_checked="FALSE" always_in_form="search" value="normal_charge" form_name="search_user" container_name="attrs"}
	    
    </tr>
</table>

<script language="javascript">
    attrs.setCheckAll('search_user','attrs_check_all');
</script>
	    