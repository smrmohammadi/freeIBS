function DomContainer()
{/* Dom Container keep html elements refrenced by dom ids.
    it's capable of selecting on of elements , and change attributes of the selected element
    (ex. changing background..)

*/
    this.objs=new Array();
    this.dependent_objs=new Array();
    this.set_on_select=Array(); /*array of arrays*/
    this.set_on_unselect=Array(); /*array of arrays*/
    
    this.setAttribute=setAttribute;
    this.__addObj=__addObj;
    this.addByID=addByID;
    this.setOnSelect=setOnSelect;
    this.setOnUnSelect=setOnUnSelect;
    this.select=select;
    this.__getObjByID=__getObjByID;
    this.__setSelectedAttrs=__setSelectedAttrs;
    this.__setUnselectedsAttrs=__setUnselectedsAttrs;
    this.__addDependents=__addDependents;
    this.__setUnselectedAttr=__setUnselectedAttr;
}
    function setAttribute(obj,attr_name,attr_value)
    {
	eval("obj.style."+attr_name+"=attr_value");
    }

    function __addObj(obj)
    {
	this.objs.push(obj);
    }

    function addByID(dom_id,dependent_ids)
    {/*add a new element with id "dom_id"
       dependent_ids is array of id's that will be selected when dom_id is selected too 
    */
	this.__addObj(document.getElementById(dom_id));
	this.__addDependents(dependent_ids);
    }

    function __addDependents(dependent_ids)
    {
	dep_objs=new Array();
	for (dep_index in dependent_ids)
	    dep_objs.push(document.getElementById(dependent_ids[dep_index]));
        this.dependent_objs.push(dep_objs);
    }
    function setOnSelect(attr_name,attr_value)
    {/*
	add a new attribute to set when element is selected
    */
	this.set_on_select.push(new Array(attr_name,attr_value));
    }

    function setOnUnSelect(attr_name,attr_value)
    {/*
	add a new attribute to set when element is unselected
    */
	this.set_on_unselect.push(new Array(attr_name,attr_value));
    }
    
    
    function select(id)
    {/* select of elements */
	this.__setSelectedAttrs(id);
	this.__setUnselectedsAttrs(id);
    }
    
    function __getObjByID(id)
    {
	for (obj_index in this.objs)
	{
	    if (this.objs[obj_index].id == id)
		return new Array(this.objs[obj_index],this.dependent_objs[obj_index]);
	}
	return null;
    }
    
    function __setSelectedAttrs(id)
    {

	arr=this.__getObjByID(id);
	obj=arr[0];
	dependents=arr[1];
	for (attr_index in this.set_on_select)
	{
	    attr_name=this.set_on_select[attr_index][0];
	    attr_value=this.set_on_select[attr_index][1];
	    this.setAttribute(obj,attr_name,attr_value);
	    for (dep_index in dependents)
		this.setAttribute(dependents[dep_index],attr_name,attr_value);
	}
    }
    
    function __setUnselectedsAttrs(id)
    {
	for (obj_index in this.objs)
	{
	    if (this.objs[obj_index].id == id)
		continue;

	    obj=this.objs[obj_index];
	    this.__setUnselectedAttr(obj);
	    for (dep_index in this.dependent_objs[obj_index])
		this.__setUnselectedAttr(this.dependent_objs[obj_index][dep_index]);
	}
    }

    function __setUnselectedAttr(obj)
    {
        for (attr_index in this.set_on_unselect)
        {
    	    attr_name=this.set_on_unselect[attr_index][0];
	    attr_value=this.set_on_unselect[attr_index][1];
	    this.setAttribute(obj,attr_name,attr_value);
	}
    }
