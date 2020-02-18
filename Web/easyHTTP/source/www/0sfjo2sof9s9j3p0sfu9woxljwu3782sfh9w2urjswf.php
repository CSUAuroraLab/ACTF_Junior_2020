<?php
error_reporting(0);

function getip() {
    static $realip;
    if(isset($_SERVER)){
        if(isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
            $realip=$_SERVER['HTTP_X_FORWARDED_FOR'];
        }
        else if(isset($_SERVER['HTTP_CLIENT_IP'])){
            $realip=$_SERVER['HTTP_CLIENT_IP'];
        }
        else{
            $realip=$_SERVER['REMOTE_ADDR'];
        }
    }
    else{
        if(getenv('HTTP_X_FORWARDED_FOR')){
            $realip=getenv('HTTP_X_FORWARDED_FOR');
        }
        else if(getenv('HTTP_CLIENT_IP')){
            $realip=getenv('HTTP_CLIENT_IP');
        }
        else{
            $realip=getenv('REMOTE_ADDR');
        }
    }
    return $realip;
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>XFF</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<?php
include_once 'flag.php';
$ip = getip();
if ($ip === '127.0.0.1'){
    die($flag);
}else{
    echo '你的IP是:'.$ip;
    echo '<br>请伪造你的IP为127.0.0.1';
}
?>
</body>
</html>