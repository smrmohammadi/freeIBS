function getSelectedOption(form_name,select_name)
{
    select_obj=eval("document."+form_name+"."+select_name);
    if (select_obj.selectedIndex<0) //select is empty
	return "";
    return select_obj.options[select_obj.selectedIndex].text;
}

function showHelp(subject,category)
{
    subject=escape(subject);
    category=escape(category);
    open("/IBSng/help/show_help.php?subject="+subject+"&category="+category,"help","width=500,height=300,scrollbars=yes,alwaysRaised=yes,dependent=yes");
}

function showMultiStr(form_name,input_name)
{
    input_obj=eval("document."+form_name+"."+input_name);
    open("/IBSng/util/show_multistr.php?str="+input_obj.value,"Show MultiString","width=500,height=300,scrollbars=yes,alwaysRaised=yes,dependent=yes");
}

