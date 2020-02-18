#!/bin/bash
function upload_clean()
{
	dir=/var/www/html/uplo4d/
	#删除周期为30分钟
	min=30
	echo "`date` find $dir -type d -mmin +$min -empty -exec rm -rf {} \;" >> ${filename}.log
	#删除30分钟前的空文件夹
	find $dir -mindepth 1 -type d -mmin +$min -empty -exec rm -rf {} \;
	#删除30分钟前的文件
	find $dir -type f -mmin +$min -exec rm -rf {} \;
}
while true
do
	upload_clean
done