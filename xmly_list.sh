#!/bin/bash

[[ "$1" == "" ]] && echo -e " Usage: ./xmly_list.sh 节目名称"  && exit 1

audioname=$1
count=1
file=$(ls -rt *.m4a)

for i in ${file};do
	if [ ${count} -le 9 ];then
			newnum="第000${count}集-${audioname}"
	elif [ ${count} -le 99 ];then
			newnum="第00${count}集-${audioname}"
	elif [ ${count} -le 999 ];then
			newnum="第0${count}集-${audioname}"
	else
			newnum="第${count}集-${audioname}"
	fi
	mv ${i} ${newnum}.m4a
	count=$(expr ${count} + 1)
done


