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
    open("/IBSng/help/show_help.php?subject="+subject+"&category="+category,"","width=500,height=300,scrollbars=yes,alwaysRaised=yes,dependent=yes,resizable=yes");
}

function showMultiStr(form_name,input_name)
{
    input_obj=eval("document."+form_name+"."+input_name);
    open("/IBSng/util/show_multistr.php?str="+input_obj.value,"","width=500,height=300,scrollbars=yes,alwaysRaised=yes,dependent=yes,resizable=yes");
}

function updateUserAddCheckImage(user_type,current_username,update_timer)
{//user_type can be 'normal' or 'voip' used to select image and pass to user_exists.php
 //update_timer: tell the timer to update the image in seconds. if set to zero, update immediately
//    alert(window.user_add_check_timer);
//    alert(update_timer);
    if(update_timer>=0)
    {
	if ((window.user_add_check_timer && window.user_add_check_timer<=0) || undefined==window.user_add_check_timer)
	    setTimeout("updateUserAddCheckImage('"+user_type+"','"+current_username+"',-1)",500);
	window.user_add_check_timer=update_timer*1000+500;
    }
    else if (update_timer<0)
    {
	if (window.user_add_check_timer==0)
	{
	    window.user_add_check_timer=undefined;
	    img_obj=eval("document."+user_type+"_user_exists");
	    username=eval("document.user_edit."+user_type+"_username");
	    img_obj.src="/IBSng/admin/user/check_user_for_add.php?image=t&username="+username.value+"&type="+user_type+"&current_username="+current_username;
	}
	else
	{
	    window.user_add_check_timer-=500;
	    setTimeout("updateUserAddCheckImage('"+user_type+"','"+current_username+"',-1)",500);
	}
    }
}

function showUserAddCheckWindow(user_type,current_username)
{
    username=eval("document.user_edit."+user_type+"_username");
    open("/IBSng/admin/user/check_user_for_add.php?image=f&username="+username.value+"&type="+user_type+"&current_username="+current_username,"user_check","width=500,height=300,scrollbars=yes,alwaysRaised=yes,dependent=yes");
}

function changeTRColor(obj,color)
{
    if(color==null)
    {
    	if(obj.original_color)
    	    obj.style.backgroundColor=obj.original_color;
    }
    else
    {
	obj.original_color=getObjCurrentStyle(obj).backgroundColor;
    	obj.style.backgroundColor=color;
    }
}

function getObjCurrentStyle(obj)
{
    if(window.getComputedStyle)
	return window.getComputedStyle(obj,null);
    else if (obj.currentStyle)
	return obj.currentStyle;
}

function showReportLayer(layer_id,show_obj)
{
    layer_obj=document.getElementById(layer_id)
    obj_top=findPosY(show_obj) + show_obj.offsetTop;
    if(show_obj.firstChild.height) //ie
	obj_top+=show_obj.firstChild.height;
    
    layer_obj.style.top=obj_top;
    layer_obj.style.left=findPosX(show_obj) - layer_obj.offsetWidth;
    toggleVisibility(layer_obj);
}


function toggleVisibility(obj)
{
    if(obj.style.visibility=='hidden')
	obj.style.visibility='visible';
    else
	obj.style.visibility='hidden';
}

function absDateSelectChanged(select_obj,calendar_id)
{
    calendar_obj=document.getElementById(calendar_id);
    if(select_obj.value=="Gregorian")
    {
	calendar_obj.date_type="G";
	calendar_obj.disabled=false;
    }
    else if (select_obj.value=="Jalali")
    {
	calendar_obj.date_type="J";
	calendar_obj.disabled=false;
    }
    else
	calendar_obj.disabled=true;
}
function findPosX(obj)
{
	var curleft = 0;
	if (obj.offsetParent)
	{
		while (obj.offsetParent)
		{
			curleft += obj.offsetLeft
			obj = obj.offsetParent;
		}
	}
	else if (obj.x)
		curleft += obj.x;
	return curleft;
}

function findPosY(obj)
{
	var curtop = 0;
	if (obj.offsetParent)
	{
		while (obj.offsetParent)
		{
			curtop += obj.offsetTop
			obj = obj.offsetParent;
		}
	}
	else if (obj.y)
		curtop += obj.y;
	return curtop;
}
