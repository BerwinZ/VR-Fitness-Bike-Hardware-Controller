import udp_manage
import serial_manage
import speed_detect
import time

if __name__ == "__main__":
    try:
        udp_manage.start_receive_data()
        serial_manage.start_read_data()
        speed_detect.start_detect_speed()
        while True:
            bike_angle = serial_manage.serial_data
            bike_speed = speed_detect.speed_KPH
            print("Speed:", bike_speed, " Angle: ", bike_angle)
            udp_manage.send_data(bike_speed, bike_angle)
            time.sleep(0.01)
    except KeyboardInterrupt:
    	udp_manage.stop_receive_data()
    	serial_manage.stop_read_data()
    	gyro_manage.stop_detect_angle()
    	print ("\nCtrl-C pressed.  Stopping")