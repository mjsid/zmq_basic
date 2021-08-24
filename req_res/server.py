import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print(f"Recieved request : {message}")
    time.sleep(2)

    socket.send(b"OK")
