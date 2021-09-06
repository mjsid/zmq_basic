import zmq;
import sys;
from string import ascii_letters, digits
from random import choice

if len(sys.argv) > 1:
    host = sys.argv[1]

context = zmq.Context()
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{host}:5555")

for request in range(10):
    print("Sending request %s .." % request)
    large_str = "".join([choice(ascii_letters + digits) for i in range(10485)])
    print(f"large_string : {large_str}")

    socket.send_string(large_str)
    message = socket.recv()
    print(f'Received reply : {message}')