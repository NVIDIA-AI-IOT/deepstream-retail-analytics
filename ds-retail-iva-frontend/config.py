# Set TEST_MODE to false to show dashboard metrics from actual data
TEST_MODE = True

ksql_server = "http://localhost:8088"
kafka_server = "localhost:9092"

# test_stream is a dummy stream created to read/write generated data
# test_topic is a dummy kafka topic created to read/write generated data
# This is done to separate actual data from generated data

if TEST_MODE:
    ksql_stream_name = "test_stream"
    kafka_topic = "test_topic"
else:
    ksql_stream_name = "detections_stream"
    kafka_topic = "detections"