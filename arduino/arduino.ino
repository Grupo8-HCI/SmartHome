/*
Keyestudio smart home Kit for Arduino
Project 8
Fan
http://www.keyestudio.com
*/
#include <Servo.h>
int incomingByte = 0;
Servo servoPuerta;


void setup () {
   pinMode (7, OUTPUT); //define D7 pin as output
   pinMode (6, OUTPUT); //define  D6 pin as output
   pinMode (13, OUTPUT); //define  D6 pin as output
   pinMode (5, OUTPUT); 
   digitalWrite (7, LOW);
   digitalWrite (6, LOW); // Reverse rotation of the motor
   servoPuerta.attach(9);
   Serial.begin(9600);
}
void loop () {
  char c;

  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    
    if (incomingByte == (int)'a') {
      digitalWrite (7, HIGH);
    } 
    
    if (incomingByte == (int)'b') {
      digitalWrite (7, LOW);
    }

    if (incomingByte == (int)'c') {
      digitalWrite (13, HIGH);
    }

    if (incomingByte == (int)'d') {
      digitalWrite (13, LOW);
    }

    if (incomingByte == (int)'e') {
      digitalWrite (5,  HIGH);
    }

    if (incomingByte == (int)'f') {
      digitalWrite (5,  LOW);
    }

    if (incomingByte == (int)'g') {
      digitalWrite (5,  HIGH);
      digitalWrite (13,  HIGH);
    }

    if (incomingByte == (int)'h') {
      digitalWrite (5,  LOW);
      digitalWrite (13,  LOW);
    }

    if (incomingByte == (int)'i') {
      servoPuerta.write(180);
    }
    if (incomingByte == (int)'j') {
      servoPuerta.write(0);
    }
  }
}
//