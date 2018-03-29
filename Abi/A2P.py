
import serial

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)

# for more precise non-blocking data grabbing -
# use read() 
# and use Serial.write() [for bytes] or Serial.print() [for ASCII chars) on the Arduino side
# NOTE - we will need to parse charcter by character

while True:
	data = arduino.readline()         
	if data:                       #readline() will occasionaly grab a blank line
		sample = data.decode("utf-8")
		print(sample)