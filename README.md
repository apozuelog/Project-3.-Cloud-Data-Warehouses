# Project 3. Cloud Data Warehouse whith AWS

### Transition to AWS cloud of Sparkify song database

To undertake the following project we have tried to configure a cluster with Redshift in it, create a user with read permissions to S3 and full access Redshift, create an ARN ROLE, security group and assign it to the cluster.

As for the programming necessary to create the tables, data copy and logic, there are 5 files:

### 1. dwh.cfg

**[CLUSTER]**  
HOST=  
DB_NAME=  
DB_USER=  
DB_PASSWORD=  
DB_PORT=

**[IAM_ROLE]**  
ARN=

**[S3]**  
LOG_DATA=s3://udacity-dend/log_data  
LOG_JSONPATH=s3://udacity-dend/log_json_path.json  
SONG_DATA=s3://udacity-dend/song_data  

In this file we find everything necessary to connect to our AWS account, Redshift, give necessary permissions and the necessary routes to copy the files from S3 to Redshift.

### 1. dwh.cfg
