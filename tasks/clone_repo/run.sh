#!/bin/bash

cd /data

if [ -d ./blog ]
then
  cd blog
  git pull origin master
else
  git clone https://github.com/EndPointCorp/end-point-blog.git blog
fi
