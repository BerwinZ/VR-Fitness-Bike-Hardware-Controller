import RPi.GPIO as IO
import time
import datetime
import udp_manage as udp

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2, IO.OUT)  # GPIO 2 -> Red LED as output
IO.setup(3, IO.OUT)  # GPIO 3 -> Green LED as output
IO.setup(14, IO.IN)  # GPIO 14 -> IR sensor as input

last_input = IO.input(14)
last_t = datetime.datetime.now()
sec = 0

while 1:
    current_input = IO.input(14)
    if current_input == 0 and current_input != last_input:
        delta_t = datetime.datetime.now() - last_t
        sec = delta_t.total_seconds()
        spd = 0.085 / sec * 3.6 * 0.62
        print(round(spd, 2))
        udp.send_data(round(spd, 2) * 10, 0)
        last_t = datetime.datetime.now()
        time.sleep(0.001)
    last_input = current_input
