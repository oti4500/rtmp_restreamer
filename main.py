import pynginx

# Create an RTMP configuration
rtmp_config = pynginx.RtmpConfig()

# Define the source application and stream
source_app = rtmp_config.add_application('source')
source_stream = source_app.add_stream('stream_key')
source_stream.pull('rtmp://source-server-ip:1935/live/stream-key')

# Define the target application and stream
target_app = rtmp_config.add_application('target')
target_stream = target_app.add_stream('stream_key')
target_stream.push('rtmp://target-server-ip:1935/live/stream-key')

# Start the RTMP server
rtmp_server = pynginx.RtmpServer(rtmp_config)
rtmp_server.start()

# Run the server indefinitely
try:
    while True:
        pass
except KeyboardInterrupt:
    rtmp_server.stop()
