#include <Wire.h>
#include <Arduino.h>
#define LEFT_PIN 4
#define RIGHT_PIN 5
#define ADDR 0x41
 // function that executes whenever data is received from master

void parseMovement(int instruct){
  Serial.println(instruct);
  switch(instruct){
      case 0x4C:
        digitalWrite(LEFT_PIN, HIGH);
//        Serial.write("L");
        break;
      case 0x52:
        digitalWrite(RIGHT_PIN,HIGH);
//        Serial.write("R");
        break;
      case 0x53:
      stop_all();  
//        Serial.write("S");
        break;

      default:
        stop_all();
        break;
//        Serial.println();
  }
}
void stop_all(){
   digitalWrite(LEFT_PIN, LOW);
   digitalWrite(RIGHT_PIN, LOW);
}
void setup() {
   Serial.begin(115200);
   pinMode(LEFT_PIN, OUTPUT);
   pinMode(RIGHT_PIN, OUTPUT);
 
}
 
void loop() {
  if (Serial.available()){
//    Serial.print(Serial.peek());
    if (Serial.read() == ADDR){
      Serial.print("Found ");
      delay(50);
      parseMovement(Serial.read());
    }
  }
}
