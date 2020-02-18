<?php
error_reporting(0);
?>
<html>
<head>
  <title>HTTP闯关</title>
</head>
<form action='index.php' method='POST'>
<p>服务器IP:
<input type='text' placeholder="127.0.0.1" name='ip'/>
</p>
<p>服务器操作系统:
<input type='text' placeholder="Ubuntu" name='server'/>
</p>
<p>PHP版本:
<input type='text' placeholder="PHP 7.0.30" name='php'/>
</p>
<p>端口:
<input type='text' placeholder="8888" name='port'/>
</p>
<input type="submit" value="Submit" />
<input type="reset" value="重置"  />
</form>


<?php
$s_php = explode('-',$_SERVER["SERVER_SOFTWARE"])[0];
$data=array($_SERVER["SERVER_NAME"],'Ubuntu',$s_php,$_SERVER["SERVER_PORT"]);

$ip = $_POST['ip'];
$server = $_POST['server'];
$php = $_POST['php'];
$port = $_POST['port'];
var_dump($data);

if ($ip===$data[0] && $server===$data[1] && $php===$data[2] && $port===$data[3] ){
  header('Location: fjwif738hwfskf23rwr2234sfiss224986.php');
  exit;
}
?>
