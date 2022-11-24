import serial

baudRate = 9600
ser = serial.Serial('/dev/ttyS3', baudRate)
print(ser.name)
while(True):
    datastring = ser.readline()
    print(datastring)