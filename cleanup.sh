#!/bin/bash


docker rm -f flaskcont
docker rm -f mariadbcont
docker rmi -f  wwl0004flask:latest
docker rmi -f wwl0004mariadb
docker network rm wwl0004net


