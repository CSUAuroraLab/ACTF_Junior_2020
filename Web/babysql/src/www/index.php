<?php
header("Content-Type: text/html;charset=utf-8");
highlight_file('sql.txt');
echo '<br><br>';

if(isset($_POST['id'])){

	waf($_POST['id']);

	$con = new mysqli("localhost","admin","FrwAwg5oilPC");
	if ($con->connect_error)
	  {
	  die('Could not connect: ' . mysql_error());
	  }

	mysqli_select_db($con, 'ctf');

	$result = $con->query("SELECT * FROM users where id='" . $_POST['id'] ."'");

	$row = $result->fetch_array();
	
	echo "用户名: " . $row['username'];
	echo "<br />";
	echo "密码: " . $row['password'];
	

	$con->close();
}

function waf($str)
{
	$filter = 'outfile|readfile|;|load_file|sleep|delete|insert|update|database|user|information_schema';
	if(preg_match('/'. $filter .'/i', $str)){
		exit('hacker!');
	}
}

?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<h1>用户信息查询</h1>
<span><S>select flag from flag</S></span>
<form action="index.php" method="post">
  <p>id: <input type="text" name="id" /></p>
  <input type="submit" value="Submit" />
</form>
</html>
