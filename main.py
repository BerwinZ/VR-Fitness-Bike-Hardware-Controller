import udp_manage
import serial_manage

if __name__ == "__main__":
    try:
        udp_manage.start_receive_data()
        while True:
            speed_KPH = serial_manage.read_speed()
            print(speed_KPH)
            udp_manage.send_data(speed_KPH, 0)
    except KeyboardInterrupt:
        print ("\nCtrl-C pressed.  Stopping")