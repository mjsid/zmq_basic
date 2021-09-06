import zmq
import random
import time
import json
import threading
from collections import defaultdict

class Ventilator:
    def __init__(self):
        context = zmq.Context()

        # Socket to send messages on
        self.sender = context.socket(zmq.PUSH)
        # Socket with direct access to the sink: used to synchronize start of batch
        self.sink = context.socket(zmq.PULL)
        self._initialize_bindings()

    def _initialize_bindings(self):
        self.sender.bind("tcp://*:5557")
        self.sink.bind("tcp://*:5558")


    def send_task(self):
        random.seed()
        for task_nbr in range(100):

            # Random workload from 1 to 100 msecs
            workload = f"Task-{task_nbr}"
            print(f"Sending task {task_nbr}...")
            random_time = random.randint(1, 100)
            data = {'workload': workload,
                    'time': random_time } 
            self.sender.send_json(data)
            time.sleep(random.randint(1,100)*0.0001)

    def recv_task(self):
        response = defaultdict(list)
        for task in range(100):
            obj = self.sink.recv_json()
            response[obj['workload']].append(obj)
        print(f"Collected response : {response}")


if __name__ == '__main__':
    

    vent = Ventilator()

    print("Press Enter when the workers are ready: ")
    _ = input()
    print("Sending tasks to workers...")

    task_thread = threading.Thread(target=vent.send_task)
    sink_thread = threading.Thread(target=vent.recv_task)

    task_thread.start()
    sink_thread.start()
    

