## 出题思路

简单SQL注入读取数据库内容



## 题目部署须知

docker-compose up -d	注意端口

docker logs acb520e63e8d|grep admin

修改源文件中的数据库用户名和密码，无须进入容器

docker exec

mysql -uadmin -pFrwAwg5oilPC<ctf.sql
