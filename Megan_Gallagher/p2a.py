import serial, time
arduino = serial.Serial('COM4', 115200, timeout=.1)
time.sleep(1) #give the connection a second to settle

arduino.write("Hello from Python!".encode('utf-8'))
time.sleep(2)
while True:
	data = arduino.read()
	if data:
		data=data.decode('utf-8')
		print(data.rstrip('\n')) #strip out the new lines for now
		# (better to do .read() in the long run for this reason