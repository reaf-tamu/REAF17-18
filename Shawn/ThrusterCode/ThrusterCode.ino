/*Skeleton Code for REAF AUV 2017-2018
Last Edit: Shawn Hinkle and Laura Austin 3/21/2018*/
#include <Servo.h>  //include Servo library for thrusters
int input;
int thrustnum;
int pwr;

Servo thruster1;    //instantiate thrusters 
Servo thruster2;
Servo thruster3;
Servo thruster4;
Servo thruster5;
Servo thruster6;
Servo thruster7;
Servo thruster8;

void setup() {
  Serial.begin(9600); //serial monitor start
  while (!Serial);  //wait until serial is ready
  delay(1000);    //1 second delay for intialization
  Serial.write("Serial begin:\n");  //FOR TESTING

  thruster1.attach(2);  //define pin that thruster is in
  thruster2.attach(3);
  thruster3.attach(4);
  thruster4.attach(5);
  thruster5.attach(6);
  thruster6.attach(7);
  thruster7.attach(8);
  thruster8.attach(9);
  
  thruster1.writeMicroseconds(1500); //send stop signal to ESC to intialize
  thruster2.writeMicroseconds(1500);
  thruster3.writeMicroseconds(1500);
  thruster4.writeMicroseconds(1500);
  thruster5.writeMicroseconds(1500);
  thruster6.writeMicroseconds(1500);
  thruster7.writeMicroseconds(1500);
  thruster8.writeMicroseconds(1500);
  delay(1000);  //1 second delay to allow ESC to recognize signal
}
int i = 0;
void loop() {
  char command[5];
  if (Serial.available()) {   //if something is in serial monitor
    
    for (int i = 0; i < 5; i++){
    input = Serial.read();    //read what is in serial monitor and store into input
    delay(500); //give time to read values
    command[i] = input; //store value into index of array
    }
    
    /*logic for translating communication
     * bit 0: thruster number (1-8)
     * bits 1-4: power (1100 - 1900)
    */
    
    thrustnum = command[0];               //thruster number should be first index of array
    Serial.write("Thruster Number: \n");  //print out thruster number
    Serial.write(thrustnum);             //print thruster number
    Serial.write("\nPower: \n");           //print out power
    Serial.write(command[1]);             //power is the last 4 bits
    Serial.write(command[2]);
    Serial.write(command[3]);
    Serial.write(command[4]);
     
    //Power is the array of the power, pwr is the int (unable to execute)

    Serial.write("\nPwr: \n"); //FOR TESTING
    Serial.write(command);      //FOR TESTING
    
    /*Thruster power key
     * 1100 = full power reverse 
     * 1499 = low power reverse
     * 1500 = stop
     * 1501 = low power forward
     * 1900 = full power forward
     */
     
     if ((pwr/1000 != 1)){                  //if power is greater than 1999 or less than 999
        Serial.write("\nError, ");  
        Serial.write(pwr);
        Serial.write(" is out of range"); //throw error, power out of range
        delay(5000);                         
     }
     
     else{                            //power is in correct range
         switch(thrustnum){           //switch dependent on thruster number
            case 1:
              thruster1.writeMicroseconds(pwr);   //send signal to thruster 1
              break;
            case 2:
              thruster2.writeMicroseconds(pwr);   //send signal to thruster 2
              break;
            case 3:
              thruster3.writeMicroseconds(pwr);   //send signal to thruster 3
              break;
            case 4:
              thruster4.writeMicroseconds(pwr);  //send signal to thruster 4
              break;
            case 5:
              thruster5.writeMicroseconds(pwr);  //send signal to thruster 5
              break;
            case 6:
              thruster6.writeMicroseconds(pwr);  //send signal to thruster 6
              break;
            case 7:
              thruster7.writeMicroseconds(pwr);   //send signal to thruster 7
              break;
            case 8:
              thruster8.writeMicroseconds(pwr);  //send signal to thruster 8
              break;
            default:
              break;

         }
     } 
     
  }

}

