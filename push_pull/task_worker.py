import sys
import time
import zmq


context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

print('Receiving task....')
# Process tasks forever
while True:
    
    s = receiver.recv_json()

    # Simple progress indicator for the viewer
    sys.stdout.write('.')
    sys.stdout.flush()
    print(f"task recieved : {s}")
    # Do the work
    time.sleep(int(s['time'])*0.01)
    s['workload'] = f"worker - {sys.argv[1]}"
    # Send results to sink
    print(f"sinking....")
    sender.send_json(s)