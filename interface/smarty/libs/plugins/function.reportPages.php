<?php
function smarty_function_reportPages($params,&$smarty)
{/*
    parameter total_results(integer,requrired): total number of results
    parameter file_path(string,optional): set the file path that will be used in page urls
    parameter pages_to_show(integer,optional): set number of pages we want to show the user on page select, default 12
*/
    $url_params=convertRequestToUrl(array("page"));
    $file_path=isset($params["file_path"])?$params["file_path"]:$_SERVER["PHP_SELF"];
    $pages_to_show=isset($params["pages_to_show"])?(int)$params["pages_to_show"]:12;
    $total_pages=calcTotalPages($params["total_results"],getRPP());
    $cur_page=min(getCurrentPage(),$total_pages);
    $link="{$file_path}?{$url_params}";
    $pages=createReportPagesArray($link,$cur_page,$total_pages,$pages_to_show);
    return createReportPagesTable($pages,$cur_page,$link,$total_pages);
}

function createReportPagestable($pages,$cur_page,$link,$total_pages)
{
    $page_nos=array_keys($pages);
    $ret="<table><tr>";
    
    $ret.=linkedPageTD(pageImage("first"),createReportPageLink($link,1));
	
    if(in_array($cur_page-1,$page_nos))
	$ret.=linkedPageTD(pageImage("back"),$pages[$cur_page-1]);
    
    foreach($pages as $page=>$complete_link)
	if($page==$cur_page)
	{
	    $ret.=<<<END
	    <td>
		{$page}
	    </td>
END;
	}
	else
	    $ret.=linkedPageTD($page,$complete_link);
	
    if(in_array($cur_page+1,$page_nos))
	$ret.=linkedPageTD(pageImage("next"),$pages[$cur_page+1]);

    $ret.=linkedPageTD(pageImage("last"),createReportPageLink($link,$total_pages));

    $ret.="</tr></table>";
    return $ret;
}

function pageImage($type)
{
    return "<img border=0 src=/IBSng/images/arrow/arrow-{$type}.gif>";
}

function linkedPageTD($face,$link)
{
    return <<<END
    	<td>
	    <a href="{$link}">{$face}</a>
	</td>
END;
}

function getCurrentPage()
{
    $page=(int)requestVal("page",1);
    if($page<=0)
	$page=1;
    return $page;
}

function getRPP()
{
    $rpp=(int)requestVal("rpp",30);
    if($rpp<=0)
	return 30;
    return $rpp;
}

function createReportPagesArray($link,$cur_page,$total_pages,$pages_to_show)
{/* return an array of  page_no=>page_link */
    $pages=array();
    $to_show_pages=calcToShowPages($total_pages,$cur_page,$pages_to_show);
    foreach($to_show_pages as $page_no)
	$pages[$page_no]=createReportPageLink($link,$page_no);
    return $pages;
}

function createReportPageLink($link,$page_no)
{
    return $link."&page={$page_no}#show_results";
}	

function calcToShowPages($total_pages,$cur_page,$pages_to_show)
{/*
    return a range of page numbers that should be showed
    $pages_to_show should be an even number or else it will be floored to
*/
    $neigh_pages=floor($pages_to_show/2);
    $pre_default_pages=min($cur_page-1,$neigh_pages);
    $post_default_pages=min($total_pages-$cur_page,$neigh_pages);
    $pre_pages=min(max($pre_default_pages,$pre_default_pages+($neigh_pages-($total_pages-$cur_page))),$cur_page-1);
    $post_pages=min(max($post_default_pages,$post_default_pages+($neigh_pages-$cur_page)),$total_pages-$cur_page);
    return range($cur_page-$pre_pages,$cur_page+$post_pages);
}

function calcTotalPages($total_results,$rpp)
{
    return (int)floor($total_results/$rpp)+1;
}

?>