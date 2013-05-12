REGISTER /usr/local/event-log-demo-0.1/elasticsearch-hadoop-1.0.0.PATCH.jar;

RAW = LOAD 'FIREWALL_LOGS' USING org.apache.hcatalog.pig.HCatLoader();

ES = FOREACH RAW GENERATE time AS timestamp, ip, country, status;

STORE ES INTO 'fw/fw_logs' USING org.elasticsearch.hadoop.pig.ESStorage();

