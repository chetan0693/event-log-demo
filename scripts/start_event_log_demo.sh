#!/bin/sh

hcat -f /usr/local/event-log-demo-0.2/create-firewall-logs-table.sql
start_flume.sh
generate_logs.py
pig -useHCatalog fw_logs_to_es.pig
start_kibana.sh
