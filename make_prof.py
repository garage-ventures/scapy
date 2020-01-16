from scapy.all import rdpcap
import time

start_time = time.time()
rdpcap('/Users/tetor/work/gp-pcap-viewer/sample.pcap')
end_time = time.time()

print(end_time - start_time)
