import time
import serial

######
# This currently (2/6/2018) works with arduinoComs.ino
# arduinoComs.ino reads 17 bytes for the string 'hello from Python'
# I got this number by printing out the bytesWritten variable in this code
######




#make sure that the com port is correct
ser = serial.Serial('COM4', 9600)
time.sleep(2)

while True:
    try:
        bytesWritten = ser.write('hello from Python'.encode('utf-8'))
        #print(bytesWritten)
        ser.flush()
        abc = ser.read(bytesWritten).decode('utf-8')
        print (abc)
        
        
    except KeyboardInterrupt:
        ser.close()
        break