function Tab()
{
    this.tab_names=Array();
    this.selected=null;
    this.addTab=addTab;
    this.__setTabEventHandlers=__setTabEventHandlers;
    this.__setTabHoverCursor=__setTabHoverCursor;
    this. __addTabObj= __addTabObj;
    this.handleOnClick=handleOnClick;
    this.__unSelectFirst=__unSelectFirst;
    this.__unSelectMiddle=__unSelectMiddle;
    this.__selectFirst=__selectFirst;
    this.__selectMiddle=__selectMiddle;
    this.__changeImageTo=__changeImageTo;
    this.__changeStyleToGray=__changeStyleToGray;
    this.__changeStyleToRed=__changeStyleToRed;
    this.__changeContent=__changeContent;
    this.initContent=initContent;
}
    function addTab(tab_name)
    {
	this.tab_names.push(tab_name);
	this.__setTabEventHandlers(tab_name);
	this.__setTabHoverCursor(tab_name);
	this.__addTabObj(tab_name);
	if(this.selected==null)
	{
	    this.selected=tab_name;
    	    this.__changeStyleToRed(tab_name);
	}
	else
	    this.__changeStyleToGray(tab_name);

    }
    
    function __setTabEventHandlers(tab_name)
    {
	el=document.getElementById(tab_name+"_td");
	if(el.addEventListener)
	    el.addEventListener("click", this.handleOnClick, false);
	else if (el.attachEvent)
	    el.attachEvent("onclick",this.handleOnClick);
    }
    
    function __setTabHoverCursor(tab_name)
    {
	el=document.getElementById(tab_name+"_td");
	el.style.cursor="pointer";
    }

    function __addTabObj(tab_name)
    {
	el=document.getElementById(tab_name+"_td");
	el.tab_obj=this;
    }

    
    function handleOnClick(e)
    {
	if(e.target)
	    td_id=e.target.id;
	else if (e.srcElement)
	    td_id=e.srcElement.id;
	tab_name=td_id.substr(0,td_id.length-3);
	tab=document.getElementById(tab_name+"_td").tab_obj;
	if(tab_name!=self.selected)
	{
	    if(tab.tab_names[0]==tab.selected)
		tab.__unSelectFirst(tab.selected);
	    else
		tab.__unSelectMiddle(tab.selected);
		
	    if(tab.tab_names[0]==tab_name)
		tab.__selectFirst(tab_name);
    	    else
		tab.__selectMiddle(tab_name);
	    tab.__changeContent(tab.selected,false);
	    tab.__changeContent(tab_name,true);
	    tab.selected=tab_name;
	}
    }
    
    function __unSelectFirst(tab_name)
    {
	this.__changeImageTo(tab_name+"_begin","/IBSng/images/tab/begin_of_tab_gray.gif");
	this.__changeImageTo(tab_name+"_end","/IBSng/images/tab/end_of_tab_gray.gif");
	this.__changeStyleToGray(tab_name);
    }

    function __unSelectMiddle(tab_name)
    {
	this.__changeImageTo(tab_name+"_begin","/IBSng/images/tab/mid_begin_of_tab_gray.gif");
	this.__changeImageTo(tab_name+"_end","/IBSng/images/tab/end_of_tab_gray.gif");
	this.__changeStyleToGray(tab_name);
    }

    function __selectFirst(tab_name)
    {
	this.__changeImageTo(tab_name+"_begin","/IBSng/images/tab/begin_of_tab_red.gif");
	this.__changeImageTo(tab_name+"_end","/IBSng/images/tab/end_of_tab_red.gif");
	this.__changeStyleToRed(tab_name);

    }
    
    function __selectMiddle(tab_name)
    {
	this.__changeImageTo(tab_name+"_begin","/IBSng/images/tab/mid_begin_of_tab_red.gif");
	this.__changeImageTo(tab_name+"_end","/IBSng/images/tab/end_of_tab_red.gif");
	this.__changeStyleToRed(tab_name);
    }
    
    function __changeImageTo(img_id,img_src)
    {
	img_el=document.getElementById(img_id);
	img_el.src=img_src;
    }

    function __changeStyleToGray(tab_name)
    {
	td_el=document.getElementById(tab_name+"_td");
	td_el.style.backgroundColor="#929292";
	td_el.style.backgroundImage="url('/IBSng/images/tab/middle_of_tab_gray.gif')";
	td_el.style.height=18;
    }    

    function __changeStyleToRed(tab_name)
    {
	td_el=document.getElementById(tab_name+"_td");
	td_el.style.backgroundImage="";
	td_el.style.backgroundColor="#9A1111";
	td_el.style.height=20;
    }    

    function __changeContent(tab_name,display)
    {
	content=document.getElementById(tab_name+"_content");
	if(content)
	    if(display)
		content.style.display="";
	    else
		content.style.display="none";
    }
    
    function initContent(tab_name)
    {
	if(tab_name!=this.selected)
	    this.__changeContent(tab_name,false);
    }