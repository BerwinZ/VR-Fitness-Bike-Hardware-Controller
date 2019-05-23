import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)
pin_speed = 14
IO.setup(pin_speed, IO.IN)  # GPIO 14 -> IR sensor as input
