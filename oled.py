from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep
from framebuf import FrameBuffer, MONO_HLSB


i2c = I2C(sda = Pin(8), scl = Pin(9), id = 0)
oled = SSD1306_I2C(128, 32, i2c)

def oled_pruebas(tiempo):
    oled.fill(0)
    oled.text('Tiempo', 50, 0)
    oled.text(tiempo, 20, 10)
    oled.show()
    
    
def abrir_imagen(ruta):
    doc = open(ruta, "rb")
    doc.readline()
    xy = doc.readline()
    x = int(xy.split()[0])
    y = int(xy.split()[1])
    imagen = bytearray(doc.read())
    doc.close()
    return FrameBuffer(imagen, x, y, MONO_HLSB)
    
