<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>你也喜欢茶颜嘛！?</title>
<!-- Bootstrap core CSS -->
<link href="./static/css/bootstrap.min.css?v=0f52fcd7ae0704868d97b2c94e7bdd0f" rel="stylesheet">
<!-- Custom styles for this template -->
<link href="./static/css/jumbotron-narrow.css?v=4c747ccfb71bf04495c664e4f54f452f" rel="stylesheet">
<!-- semantic -->
<link href="./static/css/semantic.min.css?v=a5bbd42baa26cb1930bdfdbcc2ae641b" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="./static/css/default.css?v=aec5222129542140f11824b0fbedb2a3">
<script src="./static/js/semantic.min.js?v=d5550ed22664a5bb34fdbf5546dbbedd"></script>
<script src="./static/js/jquery.min.js?v=4b57cf46dc8cb95c4cca54afc85e9540"></script>
</head>
<body>
<!-- Page Contents -->

<!--找一找我最喜欢喝的幽兰拿铁!-->

<div class="main_bg1">
<div class="wrap">
<div class="main1">
<div class="ui grid ">
<div class="eight wide column left">
<h2>这里有你们喜欢的茶颜</h2>

<p class="zhenai">冲冲冲!（图文与实际无关）</p>
</div>
<div class="eight wide column right">
<div id="prog" class="jd ui inverted progress">
</div>
</div>
</div>
</div>
</div>
</div>
<div class="main_bg">
<div class="commodity-list wrap ">
<div class="main">



<?php 
//懒得弄数据库了,静态的凑合一下叭
error_reporting(0);
$page_Num = empty($_GET["page"])?1:intval($_GET["page"]);

if($page_Num > 1000)
{
	echo '<p>No more~</p>';
	exit(0);
}
$page_End = 1000;
$data_arr =array(
	'0' => "风栖绿桂:pic1:12",
	'1' => "抹茶葡提:pic2:16",
	'2' => "茉黛玉:pic3:11",
	'3' => "浮云沉香:pic4:12",
	'4' => "素颜锡兰:pic5:13",
	'5' => "芊芊马卡龙:pic6:18",
	'6' => "蔓越阑珊:pic7:17",
	'7' => "声声乌龙:pic8:15",
	'8' => "烟火易冷:pic9:15",
	'9' => "桂花弄:pic10:15",
	'10' =>"幽兰拿铁:pic11:ACTF{pyth0n_reque5ts_coo1llllll!}",
);

$Name = null;
$Price = null;
$Pic = null;
function random_data($flag){
	if($flag == True)
	{
		$index = 10;
	}
	else{
		$index = rand(0,9);
	}
	global $data_arr,$Name,$Price,$Pic;
	$Name = explode(":",$data_arr[$index])[0];
	$Pic = explode(":",$data_arr[$index])[1];
	$Price = explode(":",$data_arr[$index])[2];
}


if($_GET["page"]==986)
{
	for($i = 0;$i<9;$i++){
		if($i==8){
			random_data(True);
		}else{
			random_data(False);
		}
		echo '<div class="grids_of_3">';
		echo '<div class="grid1_of_3">';
		echo '<a href="/info/12">';
		echo '<img src="./static/img/'.$Pic.'.jpg" alt="">';
		echo '<img class="lv" src="./static/img/logo.jpg" alt="">';
		echo '<h3>'.$Name.'</h3>';
		echo '</a>';
		echo '<div class="price">';
		echo '<h4>'.$Price.'￥<span>购买</span></h4>';
		echo '</a></div>';
		echo '</div>';
		echo '</div>';
	}

}else{
	for($i = 0;$i<9;$i++){
		random_data(False);
		echo '<div class="grids_of_3">';
		echo '<div class="grid1_of_3">';
		echo '<a href="/info/12">';
		echo '<img src="./static/img/'.$Pic.'.jpg" alt="">';
		echo '<img class="lv" src="./static/img/logo.jpg" alt="">';
		echo '<h3>'.$Name.'</h3>';
		echo '</a>';
		echo '<div class="price">';
		echo '<h4>'.$Price.'￥<span>购买</span></h4>';
		echo '</a></div>';
		echo '</div>';
		echo '</div>';
	}
}

?>



</div>
<div class="pagination " id="pag-1">


<div class="ui animated button pull-left " id="but-r-2">
<a href="?page=<?php echo $page_Num==1?1:($page_Num-1)?>">
<div class="visible content">上一页</div>
</a>
</div>

<div class="ui animated button pull-right " id="but-r-2">
<a href="?page=<?php echo $page_Num==$page_End?1000 :($page_Num+1)?>">
<div class="visible content">下一页</div>
</a>
</div>

</div>
</div>
</div>

<div class="ui inverted vertical footer segment bottom">

</div>
</body></html>