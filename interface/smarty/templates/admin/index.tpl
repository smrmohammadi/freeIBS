{* Admin Login Page


*}

{include file="header.tpl" title="Admin Login"}

<body topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginwidth="0" marginheight="0">

<!-- Header -->
<table border="0" width="100%" cellspacing="0" cellpadding="0">
	<tr>
		<td width="107"><img border="0" src="/IBSng/images/logoibsng.gif"></td>
		<td width="100%" class="Header_color"></td>
	</tr>
	<tr>
		<td align="right" colspan="2" class="Header_Submenu">
			<table align="right" border="0" cellspacing="0" cellpadding="0" class="Header_Submenu">
				<tr>
				    <td>
				    </td>
				</tr>
			</table>
		</td>
	</tr>
</table>
<!-- End Header -->
<!-- Page title & Info -->
<table border="0" width="100%" cellspacing="0" cellpadding="0">
	<tr>
		<td width="200" rowspan="2">
		<table border="0" width="100%" cellspacing="0" cellpadding="0">
			<tr>
				<td width="22"><img border="0" src="/IBSng/images/arrow_before_page_title.gif"></td>
				<td class="Page_Title"><nobr>Admin Login</b></td>
				<td width="27" ><img border="0" src="/IBSng/images/arrow_after_page_title.gif"></td>
			</tr>
		</table>
		</td>
		<td class="Page_Header_Line"></td>
	</tr>
	<tr>
		<td class="Page_Header_Info">{$smarty.now|date_format:"%A, %B %e, %Y"}&nbsp;&nbsp;</td>
	</tr>
	<tr>
		<td colspan="2" class="Page_Top_Space"></td>
	</tr>
</table>
<!-- End Page title & Info -->


<!-- Main Table -->
<table border="0" cellspacing="0" cellpadding="0" class="Main_Page">
	<tr>
		<td align="center">		
    {include file="err_head.tpl"}

    <form method=POST>
        {addEditTable title="Admin Login"}
	{addEditTD type="left"}
	    Username
	{/addEditTD}
	{addEditTD type="right"}
	    <input type=text name=username class=text>
	{/addEditTD}

	{addEditTD type="left"}
	    Password
	{/addEditTD}

	{addEditTD type="right"}
    	    <input class=text type=password name=password>
	{/addEditTD}

    {/addEditTable}
    </form>
	</td>
</tr>
</table>
<!-- End Main Table -->


<!-- Footer -->
<table border="0" width="100%" cellspacing="0" cellpadding="0">
	<tr>
		<td class="Page_Bottom_Space" colspan="3"></td>
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td width="34" rowspan="2"><img border="0" src="/IBSng/images/logo_parspooyesh.gif"></td>
		<td rowspan="2" width="280" class="Page_Footer">
		<!--Footer Links -->
			<a class="Footer_Link" target="_blank" href="http://www.ParsPooyesh.com">www.Parspooyesh.com</a>
			&nbsp; 
			Contact Info | 
			Help | 
			License</td>
		<!--END Footer Links -->
	</tr>
	<tr>
		<td class="Page_Footer_Line"></td>
	</tr>
</table>
<!-- End Footer -->


{include file="footer.tpl"}