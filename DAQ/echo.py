import serial
import time

text = 'abc'
path = '/dev/cu.usbserial-FTCBGW24'
try:
    port = serial.Serial(path, 9600)
    bytesWritten = port.write(text)
    if bytesWritten == len(text):
        print('Wrote to port: %s' % port.name)
    else:
        print('Error when writing to port: %s' % port.name)

    echo = port.read(bytesWritten)

    if bytesWritten == len(echo):
        print('Read from port: %s ' % echo)
    else:
        print('Error when reading to port: %s' % port.name)

    time.sleep(.1)
    port.close()
except IOError:
    print('Unable to open the port with path: %s' % path)
except:
    print('Unknown error')
