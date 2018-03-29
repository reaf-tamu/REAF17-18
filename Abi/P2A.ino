String string_trial;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()){
  char data = Serial.read();
  
  char str[2];
  str[1] = data;
  str[2] = '\0';

  //String crap(str);
  
  //crap.trim();

  /*int sLen = crap.length();
  for(int s=0; s<sLen; s++)
  {
    Serial.print("crap[");
    Serial.print(s);
    Serial.print("] is {");
    Serial.print(crap[s]);
    Serial.print("} which has an ascii value of ");
    Serial.println(crap[s], DEC);
  }*/
  
  //if (crap == "Hello from Python!"){
    Serial.print(str);
  //}
  }
  
}
