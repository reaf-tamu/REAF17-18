void setup() {
    Serial.begin(9600);
    delay(1000);
}

void loop() {
  if (Serial.available() > 0) {
       char inputBuffer[18];
       int b = Serial.readBytes(inputBuffer, 17); 
       delay(500);
       char sendBack[2] = {'o', 'h'};
       Serial.write(inputBuffer, 17);
  }
}
