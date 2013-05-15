#!/bin/sh

echo "Cleaning Down Existing Data"
echo "Dropping HCat table"
hcat -e "DROP TABLE FIREWALL_LOGS;"
echo "Deleting ElasticSearch Index"
curl -XDELETE http://localhost:9200/fw/
echo "Creating table"
hcat -e "CREATE TABLE FIREWALL_LOGS(time STRING, ip STRING, country STRING, status STRING) ROW FORMAT DELIMITED   FIELDS TERMINATED BY '|' LOCATION '/flume/events';"
