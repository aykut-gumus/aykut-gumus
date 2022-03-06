#!/bin/bash

if [ -z $1 ]
then
  docker run -d -it -p 80:8000 stevebrownlee/api
 
else
  docker run -p 80:8000 stevebrownlee/api

fi

