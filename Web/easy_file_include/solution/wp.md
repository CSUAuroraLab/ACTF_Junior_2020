

点击tips后

![image-20200215211531800](E:\study\Aurora\git\Newpeople\Web\easy_file_include\solution\image-20200215211531800.png)

可以看到url中的file=flag.php，可以推测这里使用了php中的include函数

尝试使用php://filter

![image-20200215211847555](E:\study\Aurora\git\Newpeople\Web\easy_file_include\solution\image-20200215211847555.png)

得到flag.php文件的base64编码结果，只需要进行解码即可

![image-20200215212045202](E:\study\Aurora\git\Newpeople\Web\easy_file_include\solution\image-20200215212045202.png)

得到flag