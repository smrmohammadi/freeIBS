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
    $pages=createReportPagesArray("{$file_path}?{$url_params}",$cur_page,$total_pages,$pages_to_show);
    return createReportPagesTable($pages,$cur_page);
}

function createReportPagestable($pages,$cur_page)
{
    $page_nos=array_keys($pages);
    $ret="<table><tr>";
    
    if(in_array($cur_page-1,$page_nos))
	$ret.=<<<END
	<td>
	    <a href="{$pages[$cur_page-1]}">back</a>
	</td>
END;
    
    foreach($pages as $page=>$link)
	if($page==$cur_page)
	{
	    $ret.=<<<END
	<td>
	    {$page}
	</td>
END;
	}
	else
	{
	    $ret.=<<<END
	<td>
	    <a href="{$link}">{$page}</a>
	</td>
END;
	}
	
    if(in_array($cur_page+1,$page_nos))
	$ret.=<<<END
	<td>
	    <a href="{$pages[$cur_page+1]}">next</a>
	</td>
END;

    $ret.="</tr></table>";
    return $ret;
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
	$pages[$page_no]=$link."&page={$page_no}";
    return $pages;
}

function calcToShowPages($total_pages,$cur_page,$pages_to_show)
{/*
    return a range of page numbers that should be showed
    $pages_to_show should be an even number or else it will be floored to
*/
    $neigh_pages=floor($pages_to_show/2);
    $pre_default_pages=min($cur_page-1,$neigh_pages-1);//pages we normally want to see, $neigh-1 causes to show 1 fewer page than post
    $post_default_pages=min($total_pages-$cur_page-1,$neigh_pages);
    $pre_pages=min(max($pre_default_pages,1+$pre_default_pages+($neigh_pages-($total_pages-$cur_page))),$cur_page-1);
    $post_pages=min(max($post_default_pages,$post_default_pages+($neigh_pages-$cur_page)),$total_pages-$cur_page-1);
    return range($cur_page-$pre_pages,$cur_page+$post_pages+1);
}

function calcTotalPages($total_results,$rpp)
{
    return floor($total_results/$rpp)+1;
}

?>