import ssd1306
from machine import Pin, SoftI2C
i2c = SoftI2C(scl=Pin(12), sda=Pin(13), freq=10000)        
oled096=ssd1306.SSD1306_I2C(128, 64, i2c)
oled096.text("HELLO JIMI !!",0,0)
oled096.show()