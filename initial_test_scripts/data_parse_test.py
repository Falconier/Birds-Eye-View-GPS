import serial
import pynmea2
import io

baudRate = 9600
ser = serial.Serial('/dev/ttyS3', baudRate)
print(ser.name)
## skip first line in case we only capture a partial message
ser.readline()
## begin data collection loop
while(True):
    datastring = ser.readline()
    ##trim escape characters
    datastring = datastring.decode()
    parsedata = pynmea2.parse(datastring)
    datatype = datastring[3:6]
    print(datatype)
    print(parsedata)
    if (datatype == 'GGA'):
        print(parsedata.lon)
        print(parsedata.lat)
        print(parsedata.timestamp)
    elif (datatype == 'GSA'):
        print('GSA')
    elif (datatype == 'RMC'):
        print('RMC')
    elif (datatype == 'GSV'):
        print('GSV')
    else:
        print(datastring)
    print('------------------------------')
    