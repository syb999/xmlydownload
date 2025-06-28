#!/bin/sh

m4a=$(ls | grep m4a | sort)

for i in $m4a;do
	ffmpeg -i ${i} $(echo ${i}.mp3 | sed 's/\.m4a//')
done

