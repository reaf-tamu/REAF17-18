import serial
arduino = serial.Serial('COM1', 115200, timeout=.1)
while True:
	data = arduino.readline()[:-2]
	if data:
		print(data)