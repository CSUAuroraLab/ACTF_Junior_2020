<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>万能密码??</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<?php
error_reporting(0);
include 'config.php';
if($_POST[username] && $_POST[passwd]) {
    $conn = new mysqli($servername,$username,$password,$dbname);
    if($conn->connect_error){
        echo "数据库连接失败";
    } 
}else{
   
} 
$username = $_POST[username];
$passwd = md5($_POST[passwd]);
$sql = "select username from users where (username='$username') and (passwd='$passwd')";
// echo $sql;
$result = $conn->query($sql);
if($result->num_rows > 0){
    $row = $result->fetch_assoc();
    if($row['username']=="admin") {
        echo "<p>Logged in! Key: ACTF{just_beginner_in_sql_injection} </p>";
    }
    if($row['username'] != "admin") {
        echo("<p>You are not admin!</p>");
    }
}
?>
<form method='post' action=index.php>
<input type='text' name='username' placeholder="Username">
<input type='password' name='passwd' placeholder="Password">
<br>
<input type='submit'>
</form>
<a href='index.txt'></a>
</body>
</html>