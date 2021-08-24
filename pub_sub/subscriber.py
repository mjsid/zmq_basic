import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting update from server..")
socket.connect(f"tcp://localhost:{port}")

socket.subscribe("10001")
socket.setsockopt_string(zmq.SUBSCRIBE, "10000")

while True:
    print(socket.recv())