import serial
arduino = serial.Serial('COM4', 115200, timeout=.1)
while True:
	data = arduino.readline()[:-2].decode('utf-8') #the last bit gets rid of the new-line chars
	if data:
		print(data)