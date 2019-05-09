import RPi.GPIO as IO
import time
from datetime import datetime, timedelta
import udp_manage as udp
import threading
import math

sensor_diameter = 30 # mm

IO.setwarnings(False)
IO.setmode(IO.BCM)
pin_speed = 14
IO.setup(pin_speed, IO.IN)  # GPIO 14 -> IR sensor as input

cycle_second = 0.1
check_cycle = timedelta(seconds = cycle_second) # check the speed every 5 seconds
speed = 0
flag = True

def detect_speed():
    global speed
    while flag:
        bg_time = datetime.now()
        ed_time = bg_time + check_cycle
        cnt = 0
        pre_data, cur_data = IO.input(pin_speed), IO.input(pin_speed)
        while datetime.now() < ed_time:
            cur_data = IO.input(pin_speed)
            if cur_data != pre_data:
                cnt += 1
                pre_data = cur_data
        cycles = cnt / 40
        rotate_speed = cycles / check_cycle.total_seconds()
        speed = math.pi * sensor_diameter / 1000.0 * rotate_speed * 36.0 / 10.0 # km/h
        speed = round(speed, 2)
        #speed = rotate_speed
        print(speed)
        udp.send_data(speed, 0)


thread = threading.Thread(target=detect_speed)

def start_detect_speed():
    thread.start()

def stop_detect_speed():
    flag = False
    thread.join()

if __name__ == "__main__":
    try:
        start_detect_speed()
    except KeyboardInterrupt:
        stop_detect_speed()
        print ("\nCtrl-C pressed.  Stopping")
