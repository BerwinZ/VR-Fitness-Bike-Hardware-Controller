import udp_manage
import serial_manage
import gyro_manage

if __name__ == "__main__":
    try:
        udp_manage.start_receive_data()
        serial_manage.start_read_data()
        gyro_manage.start_detect_angle()
        while True:
            speed_KPH = serial_manage.serial_data
            gyro_angle = gyro_manage.position
            print("Speed:", speed_KPH, " Angle: ", gyro_angle)
            udp_manage.send_data(speed_KPH, gyro_angle)
    except KeyboardInterrupt:
    	udp_manage.stop_receive_data()
    	serial_manage.stop_read_data()
    	gyro_manage.stop_detect_angle()
    	print ("\nCtrl-C pressed.  Stopping")