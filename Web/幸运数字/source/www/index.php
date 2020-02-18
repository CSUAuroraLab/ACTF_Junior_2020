<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>幸运数字</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='css/buttons.css' rel='stylesheet' type="text/css">
    <script type="text/javascript" src="js/jquery-2.2.4.min"></script>
    <script src="js/jquery.validate.min.js"></script>
</head>
<body>
    <p style="color:green;font-size:30px;text-align:center;">快来挑选一个幸运数字叭！</p>
    <center>
                <button class="button button-3d button-action button-circle button-jumbo" style="width: 300px;height: 300px" onclick="javascript:my_rand()"><i class="fa fa-thumbs-up"></i>rand</button>
                <br>
                <p>你的幸运数字：</p>
                <var id="lucky_number"></var>
    </center>

<center>
    <button class="submit" onclick="javascript:Getflag()">提交</button>
</center>

<!--我的幸运数字是一个5位数噢！-->

</body>
<script type='text/javascript'>
var lucky_number = null;
function my_rand(){
    //随机生成0-100000之间的数
    lucky_number = Math.ceil(Math.random()*100000);
    document.getElementById("lucky_number").innerHTML = lucky_number;
}
function Getflag(){
    if(lucky_number == null){
        alert("Please choose your lucky number!");
        return;
    }
    var data = "<lucky_number>" + lucky_number + "</lucky_number>";
    $.ajax({
        type: "POST",
        url: "getflag.php",
        contentType: "application/xml;charset=utf-8",
        data: data,
        dataType: "xml",
        anysc: false,
        success: function (result) {
            var code = result.getElementsByTagName("code")[0].childNodes[0].nodeValue;
            var msg = result.getElementsByTagName("msg")[0].childNodes[0].nodeValue;
            if(code == "0"){
               alert(msg + " check failed!");
            }else if(code == "1"){
                alert(msg + " check success!");
            }else{
                alert("error:" + msg);
            }
        },
        error: function (XMLHttpRequest,textStatus,errorThrown) {
            alert(errorThrown + ':' + textStatus);
        }
    });

}
</script>
</html>


