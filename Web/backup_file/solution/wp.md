由题目描述可知本题需要查找备份文件

这里可以尝试常见的备份文件名，如index.php.bak, index.php.swp等。

或者是使用后台扫描工具扫描后台找到备份文件

![image-20200215210857984](E:\study\Aurora\git\Newpeople\Web\backup_file\solution\image-20200215210857984.png)

找到源码

![image-20200215211014730](E:\study\Aurora\git\Newpeople\Web\backup_file\solution\image-20200215211014730.png)

可以看到，要求key必须为数字，但又同时要和一个字符串进行比较

这里用到的是php的弱类型比较，php中==和===是不同的本处使用的是==。php中使用==进行字符串和数字之间的比较时，会将字符串中前n位连续数字字符转化为数字后与数字比较，此处的str以123开头，因此比较时str转化为123，因此key为123时即可

![image-20200215211423882](E:\study\Aurora\git\Newpeople\Web\backup_file\solution\image-20200215211423882.png)