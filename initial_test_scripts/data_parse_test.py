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
        print(parsedata.timestamp)
        print(parsedata.latitude, parsedata.lat_dir)
        print(parsedata.longitude, parsedata.lon_dir)
        print(parsedata.altitude,parsedata.altitude_units)
        print(parsedata.horizontal_dil)
        print(parsedata.num_sats)
        print(parsedata.gps_qual)
        print(parsedata.ref_station_id)
        print(parsedata.geo_sep,parsedata.geo_sep_units)
    elif (datatype == 'GSA'):
        print('GSA')
    elif (datatype == 'RMC'):
        print('RMC')
    elif (datatype == 'GSV'):
        print('GSV')
    else:
        print(datastring)
    print('------------------------------')
    