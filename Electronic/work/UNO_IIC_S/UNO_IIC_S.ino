#include <Wire.h>
#include <Arduino.h>
#define LEFT_PIN 16
#define RIGHT_PIN 17

 // function that executes whenever data is received from master
void receiveEvent(int howMany) {
// while (0 <Wire.available()) {
    int c = Wire.read();  /* receive byte as a character */
    switch(c){
      case 1:
        digitalWrite(LEFT_PIN, HIGH);
        Serial.write("L");
        break;
      case 2:
        digitalWrite(RIGHT_PIN,HIGH);
        Serial.write("R");
        break;
      case 3:
//      stop_all();  
        Serial.write("S");
        break;

      default:
        stop_all();
        break;
        Serial.println();
    }          
//  }
             /* to newline */
}
 
// function that executes whenever data is requested from master
void requestEvent() {
 Wire.write("Hello NodeMCU");  /*send string on request */
}
void stop_all(){
   digitalWrite(LEFT_PIN, LOW);
   digitalWrite(RIGHT_PIN, LOW);
}
void setup() {
 Wire.begin(8);
 Wire.onReceive(receiveEvent);
 Wire.onRequest(requestEvent);
 pinMode(LEFT_PIN, "OUTPUT");
 pinMode(RIGHT_PIN, "OUTPUT");
 Serial.begin(115200);
}
 
void loop() {
 delay(100);
}
