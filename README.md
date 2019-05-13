# VRBike-Monitor

This repositoriy is used for the monitor part of project Cyclotron. 

## Description
* udp_manage.py  
  This script manages the udp send and receive between Raspberry Pi and VR client.
* speed_detect.py  
  This script collects the speed data from speed sensor.
* serial_manage.py   
  This script get the speed data from serial port which is sent from Arduino.
* main.py  
  This script handles the data collection and the send actions.