<?php  
$servername = "localhost";
$username = "admin";
$password = "6m0I9sVcoAMj";
$dbname = "wanneng";

function init(){
    // 创建数据库
    global $servername;
    global $username ;
    global $password ;
    global  $dbname ;
    $conn = new mysqli($servername,$username,$password);
    $sql = "CREATE DATABASE $dbname";
    if ($conn->query($sql) === TRUE) {
        echo "数据库创建成功";
    } else {
        echo "Error creating database: " . $conn->error;
    }
    mysqli_select_db($conn,$dbname);
    
    $sql = "create table `users` (
        `id` int(10) unsigned NOT NULL PRIMARY KEY  AUTO_INCREMENT ,
        `username` varchar(30) NOT NULL,
        `passwd` varchar(32) NOT NULL
        )DEFAULT CHARSET=utf8";
    if ($conn->query($sql)) {
        $sql = "insert into `users`(`username`,`passwd`) values ('admin','".md5('kOeGttPimdiIkGBS')."')";
        $conn->query($sql);
    }
    $conn->close();
}

$conn = new mysqli($servername,$username,$password,$dbname);
if($conn->connect_error){
    init();
    header("Location:index.php");
    exit;
}

?>
