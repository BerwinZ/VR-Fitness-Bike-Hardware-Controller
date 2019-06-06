import udp_manage
import serial_manage
import speed_detect
import time
import threading
import resistance_test

if __name__ == "__main__":
    try:
        udp_manage.start_receive_data()
        serial_manage.start_read_data()
        speed_detect.start_detect_speed()
        while True:
            udp_manage.send_data(speed_detect.speed_KPH, serial_manage.serial_data)
            print("Speed:", speed_detect.speed_KPH, " Angle: ", serial_manage.serial_data, "Resistance: ", udp_manage.resistance_level)
            resistance_test.add_force_level(udp_manage.resistance_level)
            time.sleep(0.1)
    except KeyboardInterrupt:
    	udp_manage.stop_receive_data()
    	serial_manage.stop_read_data()
    	speed_detect.stop_detect_speed()
    	print ("\nCtrl-C pressed.  Stopping")