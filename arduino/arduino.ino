/*
Keyestudio smart home Kit for Arduino
Project 8
Fan
http://www.keyestudio.com
*/
#include <Servo.h>
#include <LiquidCrystal_I2C.h>

int incomingByte = 0;
int auto_leds = 0;

int fan = 7;
int fan_rotation = 6;
int white_led = 13;
int yellow_led = 5;
int buzzer = 3;
int button_1 = 4;
int photo_sensor = A1;
int motion_sensor = 2;
Servo servoDoor; // pin 9
Servo servoWindow; // pin 10
LiquidCrystal_I2C lcd (0x27,16,2);


void turn_leds(int state) {
  digitalWrite (5,  state);
  digitalWrite (13,  state);
}

void check_button() {
  if (digitalRead(button_1) == 0) {
    unsigned char i, j;
         for (i = 0; i <100; i ++) // output a frequency sound
         {
           digitalWrite (buzzer, HIGH); // Sound
           delay(1); // Delay 1ms
           digitalWrite (buzzer, LOW); // No sound
           delay(1); // Delay 1ms
         }
         for (i = 0; i <100; i ++) // output sound of another frequency
         {
           digitalWrite (buzzer, HIGH); // Sound
           delay(2); // delay 2ms
           digitalWrite (buzzer, LOW); // No sound
           delay(2); // delay 2ms
         }
  }
}

void check_photo_sensor() {
  if (auto_leds) {
    if (analogRead(photo_sensor) < 600) {
     turn_leds(1);
    } else {
      turn_leds(0);
    }
  }
}

void check_motion_sensor() {
  if (digitalRead(motion_sensor)) {
    lcd.setCursor(0, 0);
    lcd.print("Bienvenido!");
  } else {
    lcd.clear();
  }
}

void setup () {
   pinMode (fan, OUTPUT); //define D7 pin as output
   pinMode (fan_rotation, OUTPUT); //define  D6 pin as output
   pinMode (white_led, OUTPUT); //define  D6 pin as output
   pinMode (yellow_led, OUTPUT);
   pinMode(buzzer, OUTPUT);
   pinMode(button_1, INPUT);
   pinMode(photo_sensor, INPUT);
   pinMode(motion_sensor, INPUT);
   servoDoor.attach(9);
   servoDoor.write(0);
   servoWindow.attach(10);
   servoWindow.write(0);
   lcd.init ();
   lcd.backlight();
   Serial.begin(9600);
}

void loop () {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    
    if (incomingByte == (int)'a') {
      digitalWrite (fan, HIGH);
    } 
    
    if (incomingByte == (int)'b') {
      digitalWrite (fan, LOW);
    }

    if (incomingByte == (int)'c') {
      digitalWrite (white_led, HIGH);
      auto_leds = 0;
    }

    if (incomingByte == (int)'d') {
      digitalWrite (white_led, LOW);
      auto_leds = 0;
    }

    if (incomingByte == (int)'e') {
      digitalWrite (yellow_led,  HIGH);
      auto_leds = 0;
    }

    if (incomingByte == (int)'f') {
      digitalWrite (yellow_led,  LOW);
      auto_leds = 0;
    }

    if (incomingByte == (int)'g') {
      turn_leds(1);
      auto_leds = 0;
    }

    if (incomingByte == (int)'h') {
      turn_leds(0);
      auto_leds = 0;
    }

    if (incomingByte == (int)'i') {
      servoDoor.write(180);
    }
    
    if (incomingByte == (int)'j') {
      servoDoor.write(0);
    }

    if (incomingByte == (int)'k') {
      servoWindow.write(90);
    }
    
    if (incomingByte == (int)'l') {
      servoWindow.write(0);
    }

    if (incomingByte == (int)'m') {
      auto_leds = 1;
    }

    if (incomingByte == (int)'n') {
      auto_leds = 0;
    }
  }

  check_button();

  check_photo_sensor();

  check_motion_sensor();
}
//