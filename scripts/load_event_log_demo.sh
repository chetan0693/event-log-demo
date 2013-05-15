#!/bin/sh

echo "Pushing Data To ElasticSearch"
pig -useHCatalog -f /usr/local/event-log-demo-0.2/fw_logs_to_es.pig
