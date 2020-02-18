<?php
/**
* autor: CoCo1er
* date: 2020-1-10
*/
error_reporting(0);
$Lucky_number = 77777;
$result = null;


libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');

try{
	$dom = new DOMDocument();
	$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
	$lucky_number = simplexml_import_dom($dom);
	if($lucky_number == $Lucky_number){
		$result = sprintf("<result><code>%d</code><msg>You get it! %s but flag in Server /flag...\n  tips: Take a closer look at the format of your upload</msg></result>",1,$lucky_number);
	}else{
		$result = sprintf("<result><code>%d</code><msg>No No No not %s</msg></result>",0,$lucky_number);
	}	
}catch(Exception $e){
	$result = sprintf("<result><code>%d</code><msg>%s</msg></result>",3,$e->getMessage());
}

header('Content-Type: text/html; charset=utf-8');
echo $result;
?>