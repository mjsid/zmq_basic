import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)

socket.bind(f"tcp://*:{port}")

while True:
    topic = random.randrange(9999, 10005)
    messagedata = random.randrange(1, 215) - 80
    print(f"{topic} -- {messagedata}")
    socket.send(b"%d %d" % (topic, messagedata))
    time.sleep(3)