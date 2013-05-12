sandbox.sources = weblog
sandbox.channels = mem_channel1 mem_channel2
sandbox.sinks = sink_to_elasticSearch sink_to_hdfs
#sandbox.sinks = sink_to_elasticSearch 

# Define / Configure source
sandbox.sources.weblog.type = exec
sandbox.sources.weblog.command = tail -F /var/log/eventlog-demo.log
sandbox.sources.weblog.selector.type = replicating
#sandbox.sources.weblog.type = seq

# HDFS sinks
sandbox.sinks.sink_to_hdfs.type = hdfs
sandbox.sinks.sink_to_hdfs.hdfs.fileType = DataStream
sandbox.sinks.sink_to_hdfs.hdfs.path = hdfs://sandbox/flume/events/
sandbox.sinks.sink_to_hdfs.filePrefix = weblog
sandbox.sinks.sink_to_hdfs.round = true
sandbox.sinks.sink_to_hdfs.roundValue = 10
sandbox.sinks.sink_to_hdfs.roundUnit = minute

# ElasticSearch Sinks
sandbox.sinks.sink_to_elasticSearch.type = org.apache.flume.sink.elasticsearch.ElasticSearchSink 
sandbox.sinks.sink_to_elasticSearch.hostNames = 192.168.56.102:9200 192.168.56.102:9300
sandbox.sinks.sink_to_elasticSearch.indexName = eventlog
sandbox.sinks.sink_to_elasticSearch.indexType = demo
sandbox.sinks.sink_to_elasticSearch.clusterName = elasticsearch 
sandbox.sinks.sink_to_elasticSearch.batchSize = 100 
sandbox.sinks.sink_to_elasticSearch.ttl = 5 
#sandbox.sinks.sink_to_elasticSearch.serializer = org.apache.flume.sink.elasticsearch.ElasticSearchDynamicSerializer 
sandbox.sinks.sink_to_elasticSearch.serializer = org.apache.flume.sink.elasticsearch.ElasticSearchLogStashEventSerializer


# Use a channel which buffers events in memory
sandbox.channels.mem_channel1.type = memory
sandbox.channels.mem_channel1.capacity = 1000
sandbox.channels.mem_channel1.transactionCapacity = 100
sandbox.channels.mem_channel2.type = memory
sandbox.channels.mem_channel2.capacity = 1000
sandbox.channels.mem_channel2.transactionCapacity = 100

# Bind the source and sink to the channel
sandbox.sources.weblog.channels = mem_channel1 mem_channel2
sandbox.sinks.sink_to_hdfs.channel = mem_channel1
sandbox.sinks.sink_to_elasticSearch.channel = mem_channel2


