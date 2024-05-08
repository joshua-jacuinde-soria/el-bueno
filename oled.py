from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(scl = Pin(8), sda = Pin(9), id = 0)
oled = SSD1306_I2C(128, 32, i2c)

def oled_pruebas(tiempo):
    oled.text('Tiempo', 80, 0)
    oled.text(tiempo, 50, 10)
    oled.show()
