import time
import random
from scapy.all import Ether, Raw, sendp

dst_mac = "00:11:22:33:44:55"  #dest MAC.add
src_mac = "66:77:88:99:AA:BB"  #src MAC.add
eth_type = 0x0800               

def generate_random_payload():
    return bytes([random.randint(0, 255) for _ in range(4)])

counter = 0
while True:
    if counter % 10 == 0:
        #every 10th iteration send frame with valid payload
        payload = bytes.fromhex("DEADBEEF") 
    else:
        # Send frame with rand payload
        payload = generate_random_payload()

    frame = Ether(dst=dst_mac, src=src_mac, type=eth_type) / Raw(payload)
    sendp(frame, iface="VMware Network Adapter VMnet8")
    
    print(f"Sent frame {counter + 1} with payload: {payload.hex()}")
    time.sleep(2)
    counter += 1
