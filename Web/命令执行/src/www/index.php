<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>command execution</title>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet" />


</head>
<body>

<h1>PING</h1>
<form class="form-inline" method="post">

    <div class="input-group">
        <input style="width:280px;" id="target" type="text" class="form-control" placeholder="请输入需要ping的地址" aria-describedby="basic-addon1" name="target">
    </div>
    <br/>
    <br/>

    <button  style="width:280px;" class="btn btn-default">PING</button>


</form>
<br /><pre>
<?php 
if (isset($_POST['target'])) {
	system("ping -c 3 ".$_POST['target']);
}
?>
</pre></body>
</html>