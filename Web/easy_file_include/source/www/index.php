<meta charset="utf8">
<?php
error_reporting(0);
$file = $_GET["file"];
if(stristr($file,"php://input") || stristr($file,"zip://") || stristr($file,"phar://") || stristr($file,"data:")){
	exit('hacker!');
}
if($file){
	include($file);
}else{
	echo '<a href="?file=flag.php">tips</a>';
}
?>
