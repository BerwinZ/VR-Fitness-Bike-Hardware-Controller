import serial
import threading

# Set up the serial port
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
# ser.open()

serial_data = 0

# The speed read function
def read_speed():
    global serial_data
    while True:
        raw_data = ser.readline()
        string_data = raw_data.decode("utf-8")
        serial_data = float(string_data) if string_data != "" else 0

thread = threading.Thread(target=read_speed)

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
    except KeyboardInterrupt:
        stop_read_data()
        print ("\nCtrl-C pressed.  Stopping")