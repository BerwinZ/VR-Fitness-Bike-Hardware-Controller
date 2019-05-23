# VRBike-Monitor

This repositoriy is used for the monitor part of project Cyclotron. Files in the top folders are files used for Raspberry Pi. Files in the Arduino folders are files used for Arduino

## Description
* main.py  
  This script used other scripts to get speed of the bike(in KPH) and get the direction of the handle of the bike, and then transfer them to the VR client via UDP.
* udp_manage.py  
  This script gets the udp send and receive action between Raspberry Pi and VR client.
* speed_detect.py  
  This script collects the speed data from speed sensor with Raspberry Pi.
* serial_manage.py   
  This script gets the data from serial port which is sent from Arduino.
* gyro_manage.py
  This script gets the direction data from gyro sensor with Raspberry Pi.
* Arduion/speed_detect.ino
  This script gets the speed data from speed sensor with Arduino and then sent it via serial port. 
* Arduino/test_varistor.ino
  This script reads the data of the varistor with Arduino and then sent it via serial port.
