from machine import Pin, I2C

i2c = I2C(scl = Pin(8), sda = Pin(9), id = 0)
