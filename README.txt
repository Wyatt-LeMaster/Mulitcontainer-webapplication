Homework2 
Wyatt LeMaster
to run type ./script
to clean up type ./cleanup

the address to test the curl command is http://172.75.0.2:8080/
to access the database directly you need to install the connector or un-comment out the line in the script
that installs it. 

Please note that the connector is not removed during the clean-up script. 

the script should run without any images installed. It will build two containers one for the flask application
and one for the mariadb database. The database will be filled using a mysql dump file. When both containers
are built the script will sleep for one minute and then execute the curl command.   
