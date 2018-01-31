void setup() {
  Serial.begin(115200); //uses same rate as python
  

}

void loop() {
  Serial.printIn("Hello world from Arduino!");
  delay(1000);
  

}
