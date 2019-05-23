import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import threading

SETTINGS_FILE = "RTIMULib"


print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)


position = 0

def detect_angle():
    global position
    prev = 99999999
    while True:
        if imu.IMURead():
            # x, y, z = imu.getFusionData()
            # print("%f %f %f" % (x,y,z))
            data = imu.getIMUData()
            fusionPose = data["gyro"]
            curr = -fusionPose[1]
            if prev == 99999999:
                position = 0
                # print("position: %f" % position)
            else:
                position += curr
                # print("position: %f" % position)
            # if (position < 30) and (position > -30):
            #     print("mid position: %f" % position)
            # elif position >= 30:
            #     print("left position: %f" % position)
            # else:
            #     print("right position: %f" % position)
            # udp.send_data(0, position)
            prev = curr
            position += 0.00001

            time.sleep(poll_interval*1.0/1000.0)

thread = threading.Thread(target=detect_angle)

def start_detect_angle():
    thread.start()

def stop_detect_angle():
    flag = False
    thread.join()

if __name__ == "__main__":
    try:
        start_detect_angle()
    except KeyboardInterrupt:
        stop_detect_angle()
        print ("\nCtrl-C pressed.  Stopping")
