import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)
time.sleep(1) #give the connection a second to settle

arduino.write("Hello from Python!".encode("utf-8"));

while True:
	data = arduino.readline()
	if data:
		print(data.decode("utf-8"))

