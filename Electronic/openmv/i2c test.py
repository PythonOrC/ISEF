# Untitled - By: ethan - Wed Aug 10 2022

import sensor, image, time
from pyb import I2C

i2c = I2C(2, I2C.MASTER)
slaves = i2c.scan()
print(slaves)
print(i2c.is_ready(0x08))
while(True):
    if i2c.is_ready(0x08):
        time.sleep(3)
        i2c.send(1, addr=0x08)
        time.sleep(3)
        i2c.send(2, addr=0x08)
        time.sleep(3)
        i2c.send(3, addr=0x08)
