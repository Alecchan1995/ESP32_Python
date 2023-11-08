from machine import Pin,SoftI2C
import ssd1306
import time
button_up = Pin(27,Pin.IN,Pin.PULL_UP)
button_down = Pin(16,Pin.IN,Pin.PULL_UP)
number = 0
i2c = SoftI2C(scl=Pin(12), sda=Pin(13), freq=10000)        
oled096=ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled096.text(str(number),30,20)
    oled096.show()
    print("button_up   :",button_up.value())
    if button_up.value() == 0 and button_down.value() == 1:
        number += 1
        print("number",number)
        oled096.fill(0)
    elif button_down.value() == 0 and button_up.value() == 1:
        number -= 1
        oled096.fill(0)
        print("number",number)
    elif button_down.value() == 0 and button_up.value() == 0:
        number = 0
        oled096.fill(0)
        print("number",number)
    print("button_down :",button_down.value())
    time.sleep(0.5)