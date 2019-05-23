import socket
import json
import threading
import os

# Send
file_name = "VR_IP.txt"
VR_IP = ""
VR_PORT = 8888

def write_file():
    VR_IP = input("Please input new VR ip: ")
    ip_file = open(file_name, 'w')
    ip_file.write(VR_IP)
    ip_file.close()

if not os.path.isfile(file_name):
    write_file()
else:
    ip_file = open(file_name, 'r')
    VR_IP = ip_file.read()
    ip_file.close()
    print("The ip of VR is: ", VR_IP)
    ip_correct = input("Is the ip correct? (y/n): ")
    if 'n' in ip_correct:
        write_file()

send_sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

def send_data(speed, angle):
    data = {"speed": speed, "angle": angle}
    MESSAGE = bytes(json.dumps(data), encoding='utf-8')
    send_sock.sendto(MESSAGE, (VR_IP, VR_PORT))

# Receive
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
PI_IP =  IPAddr 
PI_PORT = 8888
print("The ip of Raspberry Pi is: ", PI_IP)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
receive_sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
receive_sock.bind((PI_IP, PI_PORT))

def receive_data():
    while True:
        data, addr = receive_sock.recvfrom(1024) # buffer size is 1024 bytes
        msg = json.loads(data)
        print("received message:", msg)

thread = threading.Thread(target=receive_data)

def start_receive_data():
    thread.start()

def stop_receive_data():
    thread.join()


if __name__ == "__main__":
    try:
        start_receive_data()
        
        while True:
            speed = input("Please input speed: ")
            angle = input("Please input angle: ")
            send_data(speed, angle)
    except KeyboardInterrupt:
        stop_receive_data()
        socket.shutdown(socket.SOCK_DGRAM)
        socket.close()
        print ("\nCtrl-C pressed.  Stopping")