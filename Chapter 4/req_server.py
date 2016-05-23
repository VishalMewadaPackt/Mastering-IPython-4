import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  So everything does not happen too fast to see
    time.sleep(1)

    #  Send reply back to client
    socket.send("World")

