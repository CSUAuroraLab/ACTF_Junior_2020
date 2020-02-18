进入链接后看到源代码。

![image-20200215205227063](E:\study\Aurora\git\Newpeople\Web\easyphp\solution\image-20200215205227063.png)

可以看到，第一步是需要用post请求传一个key变量，和session中的key值相同

由于session中的值并未设置，因此key值设为空即可

第二步是md5函数的绕过，由于php中向md5函数传入数组变量会返回null，因此只需要get请求传入两个数组即可。

payload：http://106.15.207.47:21004/?username[]=1&password[]=2

post报文：key=

![image-20200215205721062](E:\study\Aurora\git\Newpeople\Web\easyphp\solution\image-20200215205721062.png)

使用的插件为http request maker，浏览器为火狐