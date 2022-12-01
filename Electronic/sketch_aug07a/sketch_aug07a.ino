#include <MPU6050_tockn.h>
#include <Wire.h>
MPU6050 mpu6050(Wire);
int red_light_pin= 9;
int green_light_pin = 10;
int blue_light_pin = 11;
void setup() {
  Serial.begin(9600);
//  // put your setup code here, to run once:
//  delay(1000);
//  myservo.attach(9);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("X: ");
  Serial.print(mpu6050.getAngleX());
  if (mpu6050.getAngleX()>3 || mpu6050.getAngleX()<-3){
    analogWrite(red_light_pin, 0);
  }else{
    analogWrite(red_light_pin, 255);
   }
  Serial.print("\tY: ");
  Serial.print(mpu6050.getAngleY());
  Serial.print("\tZ: ");
   if (mpu6050.getAngleY()>3 || mpu6050.getAngleY()<-3){
    analogWrite(green_light_pin, 0);
  }else{
    analogWrite(green_light_pin, 255);
   }
  Serial.println(mpu6050.getAngleZ());
  if (mpu6050.getAngleZ()>3 || mpu6050.getAngleZ()<-3){
    analogWrite(blue_light_pin, 0);
  }else{
    analogWrite(blue_light_pin, 255);
   }
  mpu6050.update();
}
