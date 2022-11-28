import sys
import serial
import glob

platform = sys.platform

if platform == 'linux':
    ports = glob.glob('/dev/tty[A-Za-z]*')
elif platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
else:
    raise EnvironmentError('Failed')

portList = []

for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        portList.append(port)
    except serial.SerialException:
        pass

print(platform)
print(portList)