FROM		ubuntu
MAINTAINER      Wyatt LeMaster <wwl0004@auburn.edu> 
EXPOSE          8080
RUN             apt-get update -y
RUN             apt-get install -y iputils-ping
RUN             apt-get install nano
RUN             mkdir /home/flask-working
COPY            ./api.py/  /home/flask-working/
RUN             apt install python3-pip -y
RUN             pip3 install flask 
RUN             apt install libmariadb3 libmariadb-dev -y
RUN             apt install mariadb-client-core-10.6 -y
RUN             pip3 install mariadb
RUN             pip install sqlalchemy

CMD             ["/bin/bash"]
