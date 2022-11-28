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
    if (datatype == 'GGA'):
        print('GGA')
        # print(parsedata.timestamp)
        # print(parsedata.latitude, parsedata.lat_dir)
        # print(parsedata.longitude, parsedata.lon_dir)
        # print(parsedata.altitude,parsedata.altitude_units)
        # print(parsedata.horizontal_dil)
        # print(parsedata.num_sats)
        # print(parsedata.gps_qual)
        # print(parsedata.ref_station_id)
        # print(parsedata.geo_sep,parsedata.geo_sep_units)
    elif (datatype == 'GSA'):
        print('GSA')
        # print(parsedata.mode)
        # print(parsedata.mode_fix_type)
        # print(parsedata.sv_id01)
        # print(parsedata.sv_id02)
        # print(parsedata.sv_id03)
        # print(parsedata.sv_id04)
        # print(parsedata.sv_id05)
        # print(parsedata.sv_id06)
        # print(parsedata.sv_id07)
        # print(parsedata.sv_id08)
        # print(parsedata.sv_id09)
        # print(parsedata.sv_id10)
        # print(parsedata.sv_id11)
        # print(parsedata.sv_id12)
        # print(parsedata.pdop)
        # print(parsedata.hdop)
        # print(parsedata.vdop)
    elif (datatype == 'RMC'):
        print('RMC')
        # print(parsedata.timestamp)
        # print(parsedata.status)
        # print(parsedata.latitude,parsedata.lat_dir)
        # print(parsedata.longitude,parsedata.lon_dir)
        # print(parsedata.spd_over_grnd)
        # print(parsedata.true_course)
        # print(parsedata.datestamp)
        # print(parsedata.mag_variation,parsedata.mag_var_dir)
    elif (datatype == 'GSV'):
        print('GSV')
        # print(parsedata.num_messages)
        # print(parsedata.msg_num)
        # print(parsedata.num_sv_in_view)
        # print(parsedata.sv_prn_num_1)
        # print(parsedata.elevation_deg_1)
        # print(parsedata.azimuth_1)
        # print(parsedata.snr_1)
        # print(parsedata.sv_prn_num_2)
        # print(parsedata.elevation_deg_2)
        # print(parsedata.azimuth_2)
        # print(parsedata.snr_2)
        # print(parsedata.sv_prn_num_3)
        # print(parsedata.elevation_deg_3)
        # print(parsedata.azimuth_3)
        # print(parsedata.snr_3)
        # print(parsedata.sv_prn_num_4)
        # print(parsedata.elevation_deg_4)
        # print(parsedata.azimuth_4)
        # print(parsedata.snr_4)
    else:
        print(datatype)
        print(datastring)
    print('------------------------------')
    