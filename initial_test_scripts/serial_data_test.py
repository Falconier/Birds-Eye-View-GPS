import serial

baudRate = 9600
ser = serial.Serial('/dev/ttyS3', baudRate)
print(ser.name)
while(True):
    data = ser.readline()
    print(data)