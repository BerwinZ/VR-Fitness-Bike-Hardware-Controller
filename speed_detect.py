import RPi.GPIO as IO
import time
from datetime import datatime
import udp_manage as udp
import threading

IO.setwarnings(False)
IO.setmode(IO.BCM)
pin_speed = 14
IO.setup(pin_speed, IO.IN)  # GPIO 14 -> IR sensor as input

check_cycle = datatime(second = 5) # check the speed every 5 seconds
speed = 0
thread = threading.Thread(target=detect_speed)
flag = True

def start_detect_speed():
    thread.start()

def stop_detect_speed():
    flag = False
    thread.join()

def detect_speed():
    global speed
    while flag:
        bg_time = datetime.now()
        ed_time = bg_time + check_cycle
        cnt = 0
        pre_data, cur_data = 0, 0
        while datetime.now() < ed_time:
            cur_data = IO.input(pin_speed)
            if cur_data != pre_data:
                cnt += 1
                pre_data = cur_data
        cycles = cnt / 40
        rotate_speed = cycles / check_cycle
        speed = rotate_speed
        # speed = rotate_speed * k

if __name__ == "__main__":
    try:
        start_detect_speed()
        while True:
            print(speed)
    except KeyboardInterrupt:
        stop_receive_speed()
        print ("\nCtrl-C pressed.  Stopping")