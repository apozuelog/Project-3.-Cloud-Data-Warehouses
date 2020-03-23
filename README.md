# Project 3. Cloud Data Warehouse whith AWS

### Transition to AWS cloud of Sparkify song database

To undertake the following project we have tried to configure a cluster with Redshift in it, create a user with read permissions to S3 and full access to Redshift, create an ARN ROLE to use in the connection and security group to assign it to the cluster.

As for the programming necessary to create the tables, data copy and logic, there are 6 files:

### **1. dwh.cfg**   
In this file we find everything necessary to connect to our AWS account, Redshift, give necessary permissions and the necessary routes to copy the files from S3 to Redshift.

[CLUSTER]  
HOST=  
DB_NAME=  
DB_USER=  
DB_PASSWORD=  
DB_PORT=  

[IAM_ROLE]  
ARN=

[S3]  
LOG_DATA=s3://udacity-dend/log_data  
LOG_JSONPATH=s3://udacity-dend/log_json_path.json  
SONG_DATA=s3://udacity-dend/song_data  

### **2. sql_queries.py**  
In this file we have: 
***CONFIG***, everything related to the connection with AWS and the .cfg file  
***DROP TABLES*** from *staging_events_table, staging_songs_table, songplays, users, songs, artist and time*  
***CREATE TABLES*** to *staging_events_table, staging_songs_table, songplays, users, songs, artist and time*  
***STAGING TABLES COPY*** to *staging_events_table y staging_songs_table*  
***INSERTS*** to *songplays, users, songs, artist and time*   
***QUERIES []***, 4 arrays that contain the queries necessary for the above, *create_table_queries, drop_table_queries, copy_table_queries and insert_table_queries*

### **3. create_tables.py**  
This file contains the definition of the functions, *drop_tables y create_tables*

### **4. etl.py**
Here the reading and inserting functions are defined, *load_staging_tables e insert_tables*

## **5. comprobaciones.ipynb**
Notebook with the instructions necessary to run all of the above and carry out the necessary checks

## **6. README.md**
I, who am the file to explain all the components indicated above.
