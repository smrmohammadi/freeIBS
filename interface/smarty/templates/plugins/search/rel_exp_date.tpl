{addEditTD type="left"}
    Relative Expiration Date
{/addEditTD}
{addEditTD type="right"}
    {op class="ltgteq" name="rel_exp_date_op" selected="rel_exp_date_op"} 
    <input class="text" type=text name=rel_exp_date value="{ifisinrequest name="rel_exp_date"}"> 
    {relative_units name="rel_exp_date_unit" default_request="rel_exp_date_unit"}
{/addEditTD}
