{include file="help_header.tpl"}

{viewTable title="Help " table_width=450 double="TRUE" id="help_table"}
    {addEditTD type="left1" double="TRUE"}
	Subject
    {/addEditTD}
    {addEditTD type="right1" double="TRUE"}
	<nobr>{$subject|capitalize}
    {/addEditTD}
    {addEditTD type="left2" double="TRUE"}
    	Category
    {/addEditTD}
    {addEditTD type="right2" double="TRUE"}
	<nobr>{$category|capitalize}
    {/addEditTD}

<tr>
    <td colspan=10>
		<table border="0" width="100%" cellspacing="0" cellpadding="0" >
			<tr>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/top_left_of_comment_dark.gif"></td>
				<td class="Form_Content_Row_Top_textarea_line_dark"></td>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/top_right_of_comment_dark.gif"></td>
			</tr>
			<tr>
				<td class="Form_Content_Row_Left_textarea_line_dark">&nbsp;</td>
				<td class="Form_Content_Row_Right_textarea_td_dark"><p class="in_body"><font color="#222222"> {include file=$tpl_file}</font></td>
				<td class="Form_Content_Row_Right_textarea_line_dark">&nbsp;</td>
			</tr>
			<tr>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/bottom_left_of_comment_dark.gif"></td>
				<td class="Form_Content_Row_Bottom_textarea_line_dark">&nbsp;</td>
				<td class="Form_Content_Row_Textarea_corner"><img border="0" src="/IBSng/images/bottom_right_of_comment_dark.gif"></td>
			</tr>
		</table>
</tr>
</td>	
{/viewTable}

{literal}
<script language="javascript">

    window.focus();
    element=document.getElementById("help_table");
    height=0;
    while (element)
    {    
	height+=element.offsetHeight;
	if(element.offsetTop)
	    height+=element.offsetTop;
	if(element.offsetParent)
	    element=element.offsetParent;
	else
	    element=null;
    }
//    alert(height);
    window.resizeTo(window.outerWidth,height-100);
</script>
{/literal}

{include file="help_footer.tpl"}