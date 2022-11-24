import serial
import pynmea2
import io

baudRate = 9600
ser = serial.Serial('/dev/ttyS3', baudRate)
print(ser.name)
while(True):
    datastring = ser.readline()
    ##trim escape characters
    datastring = datastring.decode()
    print(datastring)
    parsedata = pynmea2.GGA.parse(datastring)
