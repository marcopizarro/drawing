# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=115200, timeout=.1)

while True:
    value = arduino.readline()
    value = int.from_bytes(value, "big") 
    print(value) # printing the value
    time.sleep(.05)