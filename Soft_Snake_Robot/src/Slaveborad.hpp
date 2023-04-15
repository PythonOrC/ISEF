#ifndef _SLAVE_BORAD_HPP
#define _SLAVE_BORAD_HPP

// #define SLAVE

#ifdef SLAVE

#include <Arduino.h>
#include <Wire.h>

#define Left_pin 33
#define Right_pin 23
#define Mid_pin 32
#define pi 3.14159f

#define Speed 1.0f
#define Wavelengths 1.0f

#define TotalNumbers 4

// #define id 1 // 设备编号
// #define id 2 // 设备编号
#define id 3 // 设备编号
// #define id 4 // 设备编号
// #define id 5 // 设备编号

float Shift = 2 * pi / TotalNumbers; // Phase lag between segments

void robot_run(int t);
void receiveEvent(int n);
void requestEvent();
int char2int(char *p);
char *int2char(int x);

void slavefunction()
{
    Wire.begin(id, 22, 19, 400000UL);
    pinMode(Left_pin, OUTPUT);
    pinMode(Right_pin, OUTPUT);
    pinMode(Mid_pin, OUTPUT);

    Wire.onReceive(receiveEvent);
    Wire.onRequest(requestEvent);

    // Allow allocation of all timers
    Serial.begin(115200);

    for (;;)
    {
    }
}

void receiveEvent(int n)
{
    char c;
    int j;
    char *p1 = (char *)malloc(sizeof(int));
    for (j = 0; j < sizeof(int); j++)
    {
        // Serial.println(Wire.available());
        *(p1 + j) = Wire.read();
    }
    int x = char2int(p1);
    robot_run(x);
    Serial.println(x);
    free(p1);
}

void requestEvent()
{
    // char *p1 = int2char(adc);
    // Wire.write(p1, sizeof(int));
    // Serial.println(p1);
    // free(p1);
}

int char2int(char *p)
{
    int *p_Int;
    p_Int = (int *)malloc(sizeof(int));
    memcpy(p_Int, p, sizeof(int));
    int x = *p_Int;
    free(p_Int);
    return x;
}

char *int2char(int x)
{
    char *p_Char;
    p_Char = (char *)malloc(sizeof(int));
    memcpy(p_Char, &x, sizeof(int));
    return p_Char;
}

void robot_run(int t)
{
    if (t == 365)
    {
        digitalWrite(Mid_pin, LOW);
        digitalWrite(Left_pin, LOW);
        digitalWrite(Right_pin, LOW);
    }

    else if (t >= 0 && t <= 360)
    {
        float rads = t * pi / 180.0f;
        float K = sin(Speed * rads + id * Wavelengths * Shift);
        // Serial.println(K);
        if (K > 0.1)
        {
            digitalWrite(Left_pin, HIGH);
            digitalWrite(Mid_pin, LOW);
            digitalWrite(Right_pin, LOW);
        }
        if (K < -0.1)
        {
            digitalWrite(Left_pin, LOW);
            digitalWrite(Mid_pin, LOW);
            digitalWrite(Right_pin, HIGH);
        }
        if (K >= -0.1 && K <= 0.1)
        {
            digitalWrite(Left_pin, LOW);
            digitalWrite(Mid_pin, LOW);
            digitalWrite(Right_pin, LOW);
        }
    }
}

#endif // M

#endif // !_MASTBORAD_HPP
