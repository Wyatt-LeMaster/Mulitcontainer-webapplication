#!/bin/bash

#sudo apt install mariadb-client-core-10.6

docker build -t wwl0004mariadb ~/containerFiles/mariadbFile/
docker  build -t wwl0004flask   ~/containerFiles/flaskFile/.

sudo docker network create --subnet=172.75.0.0/16  wwl0004net

docker run  -d  -it  --net wwl0004net --ip 172.75.0.2 -p 8080:8080  --name flaskcont wwl0004flask 
docker run --net wwl0004net --ip 172.75.0.3 -p 3306:3306 -d --name mariadbcont -eMARIADB_ROOT_PASSWORD=Password123! wwl0004mariadb

docker exec -d flaskcont python3 /home/flask-working/api.py

echo "sleeping for 1 minute to give containers time to get ready..."
sleep 10
echo " 50 remaining "
sleep 10
echo " 40 remaining "
sleep 10
echo " 30 remaining "
sleep 10
echo " 20 remaining "
sleep 10
echo " 10 remaining "
sleep 10
echo " done sleeping "  
sleep 1
echo " executing curl command "
echo " curl http://172.75.0.2:8080/ " 

curl http://172.75.0.2:8080/
