{* Add New Interface
    interface_name: new ippool_name
    comment: comment!
    
    Success: client will be redirected to the new interface information page
    Failure: this page is shown again with error message at top of the page

*}
{include file="admin_header.tpl" title="Interface `$interface_name` Info" selected="Bandwidth"}
{include file="err_head.tpl"}
{headerMsg var_name="delete_leaf_service_success"}Leaf Service Deleted Successfully.{/headerMsg}
{headerMsg var_name="delete_node_success"}Node Deleted Successfully.{/headerMsg}
{headerMsg var_name="delete_leaf_success"}Leaf Deleted Successfully.{/headerMsg}


{$tree}

{if isset($show_layer_link)}
<script language="javascript">
    link='{$show_layer_link}';
    {literal}
	    window.onload=function(){document.getElementById(link).onclick();};
    {/literal}
</script>
{/if}

{addRelatedLink}
    <a href="/IBSng/admin/bw/interface_list.php" class="RightSide_links">
	Interface list
    </a>
{/addRelatedLink}

{addRelatedLink}
    <a href="/IBSng/admin/bw/interface_info.php?delete_interface=1&interface_name={$interface_name}" class="RightSide_links" {jsconfirm}>
	Delete Interface <b>{$interface_name}</b>
    </a>
{/addRelatedLink}

{setAboutPage title="Interface Info"}

{/setAboutPage}

{include file="admin_footer.tpl"}
