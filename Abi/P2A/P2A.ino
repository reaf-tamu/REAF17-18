String string_trial = "";
int count = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()> 0){
    char data = Serial.read();
  
  
    char str[2];
    str[0] = data;
    str[1] = '\0';
  
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
    string_trial += data;
    count++;
  
    //Serial.print(str);

    // For testing!
    Serial.print(string_trial);
    Serial.print('\n');
    
    if (string_trial == "Hello from Python!"){
      Serial.print(string_trial);
      Serial.print('\n');
      string_trial = "";
    }
  }
  
}
