from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep


i2c = I2C(sda = Pin(8), scl = Pin(9), id = 0)
oled = SSD1306_I2C(128, 32, i2c)

def oled_pruebas(tiempo):
    oled.text('Tiempo', 50, 0)
    oled.text(tiempo, 20, 10)
    oled.show()
    sleep(1)
    
