import serial
import threading
import time

# Set up the serial port
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
# ser.open()

serial_data = 0

first_read_flag = True

# The speed read function
def read_data():
    global serial_data
    global first_read_flag
    while True:
        raw_data = ser.readline()
        if first_read_flag:
            print(raw_data)
            first_read_flag = False
        else:
            string_data = raw_data.decode("utf-8")
            serial_data = float(string_data) if string_data != "" else 0
            # print(serial_data)

thread = threading.Thread(target=read_data)

# Start the read threading
def start_read_data():
    thread.start()

# Stop the read threading
def stop_read_data():
    thread.join()

if __name__ == "__main__":
    try:
        start_read_data()
        while True:
            print(serial_data)
            time.sleep(0.1)
    except KeyboardInterrupt:
        stop_read_data()
        print ("\nCtrl-C pressed.  Stopping")