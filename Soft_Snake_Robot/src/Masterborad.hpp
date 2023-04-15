#ifndef _MASTER_BORAD_HPP
#define _MASTER_BORAD_HPP

#define MASTER

#ifdef MASTER
#include <Arduino.h>
#include <Wire.h>

#define Left_pin 33
#define Right_pin 23
#define Mid_pin 32
#define pi 3.14159f

#define Speed 1.0f
#define Wavelengths 1.0f

#define TotalNumbers 4
float Shift = 2 * pi / TotalNumbers; // Phase lag between segments
#define id 0                         // 设备编号

void robot_run(int t);
void receive();
int char2int(char *p);
char *int2char(int x);
void send_data(int add, int t);

void masterfunction()
{
    Wire.begin(22, 19, 400000UL);

    pinMode(Left_pin, OUTPUT);
    pinMode(Right_pin, OUTPUT);
    pinMode(Mid_pin, OUTPUT);

    // Allow allocation of all timers
    Serial.begin(115200);
    for (;;)
    {
        // for (int i = 0; i <= 360; i++)
        // {
        //     for (int j = 1; j < TotalNumbers; j++)
        //     {
        //         send_data(j, i);
        //     }
        //     robot_run(i);
        //     delay(20);
        // }

        for (int i = 360; i >= 0; i--)
        {
            for (int j = 1; j < TotalNumbers; j++)
            {
                send_data(j, i);
            }
            robot_run(i);
            delay(15);
        }
    }
}

void send_data(int add, int t)
{
    Wire.beginTransmission(add);
    char *p1 = int2char(t);
    Wire.write((uint8_t *)p1, sizeof(int));
    free(p1);
    Wire.endTransmission();
}
void receive()
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

    Serial.println(x);
    free(p1);
}

char *int2char(int x)
{
    char *p_Char;
    p_Char = (char *)malloc(sizeof(int));
    memcpy(p_Char, &x, sizeof(int));
    return p_Char;
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
