<?php
error_reporting(0);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Cookie</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <p>请设置如下cookie:</p>
    <p>flag = ACTF</p>
</body>
</html>

<?php
if(isset($_COOKIE['flag']) && $_COOKIE['flag'] == 'ACTF') {
    header('Location: 0sfjo2sof9s9j3p0sfu9woxljwu3782sfh9w2urjswf.php');
}
