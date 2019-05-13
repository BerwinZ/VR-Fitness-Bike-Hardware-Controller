import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
# ser.open()

def read_speed():
    raw_data = ser.readline()
    string_data = raw_data.decode("utf-8")
    speed_KPH = float(string_data) if string_data != "" else 0
    return speed_KPH

if __name__ == "__main__":
    try:
        while True:
            speed_KPH = read_speed()
            print(speed_KPH)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
    except KeyboardInterrupt:
        print ("\nCtrl-C pressed.  Stopping")