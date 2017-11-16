void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  float sensorValue = analogRead(A0);
  // Converting pressure from Bar to PSF
  float pressure = sensorValue*9.6;
  
  // Density of the fluid (lb/ft^3)
  float r = 1030;
  // Acceleration due to gravity (ft/s^2)
  float g = 32.2;
  // Atmospheric pressure in psf (lb/ft^2)
  float patm = 2116.8;
  float depth = (pressure - patm)/(r*g);
  Serial.println(depth,5);
  delay(500);
  
  

}
