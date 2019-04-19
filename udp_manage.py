import socket
import json
import threading

# Send
VR_IP = "10.252.30.80"
VR_PORT = 8888
send_sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

def send_data(speed, angle):
    data = {"speed": speed, "angle": angle}
    MESSAGE = bytes(json.dumps(data), encoding='utf-8')
    send_sock.sendto(MESSAGE, (VR_IP, VR_PORT))

# Receive
PI_IP = "10.252.30.80"
PI_PORT = 1234
receive_sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
receive_sock.bind((PI_IP, PI_PORT))

def receive_data():
    while True:
        data, addr = receive_sock.recvfrom(1024) # buffer size is 1024 bytes
        msg = json.loads(data)
        print("received message:", msg)

def start_receive_data():
    threading.Thread(target=receive_data).start()


if __name__ == "__main__":
    try:
        start_receive_data()
        
        while True:
            speed = input("Please input speed: ")
            angle = input("Please input angle: ")
            send_data(speed, angle)
    except KeyboardInterrupt:
      print ("\nCtrl-C pressed.  Stopping")