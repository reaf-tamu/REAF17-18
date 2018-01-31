import serial
arduino=serial.Serial('COM3',115200,timeout=.1)
while True:
    data=arduino.readline()[:-2]
    if data:
        print(data)


