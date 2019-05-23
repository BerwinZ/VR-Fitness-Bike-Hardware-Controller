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
IO.setup(pin_speed, IO.IN)  # GPIO 14

cycle_second = 0.1
check_cycle = timedelta(seconds = cycle_second)
speed_KPH = 0
flag = True

def detect_speed():
    global speed_KPH
    while True:
        bg_time = datetime.now()
        cnt = 0
        pre_data, cur_data = IO.input(pin_speed), IO.input(pin_speed)
        while datetime.now() < bg_time + check_cycle:
            cur_data = IO.input(pin_speed)
            if cur_data != pre_data:
                cnt += 1
                pre_data = cur_data
        cycles = cnt / 40.0
        rotate_speed = cycles / check_cycle.total_seconds() # RPS
        speed_KPH = math.pi * (sensor_diameter / 1000.0) * rotate_speed * 3.6 # KPH
        speed_KPH = round(speed_KPH, 2)

thread = threading.Thread(target=detect_speed)

def start_detect_speed():
    thread.start()

def stop_detect_speed():
    thread.join()

if __name__ == "__main__":
    try:
        start_detect_speed()
        while True:
            print(speed_KPH)
    except KeyboardInterrupt:
        stop_detect_speed()
        print ("\nCtrl-C pressed.  Stopping")
