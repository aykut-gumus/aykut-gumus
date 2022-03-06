#!/bin/bash

docker stop `docker ps | grep 'stevebrownlee/api' | awk '{ print $1 }'`

