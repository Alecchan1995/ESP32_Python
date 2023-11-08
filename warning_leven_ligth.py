from machine import Pin
import time
PinRed = Pin(26,Pin.OUT)
PinYellow = Pin(14,Pin.OUT)
button_up = Pin(13,Pin.IN)
button_down = Pin(0,Pin.IN)
level = 0
while True:
    if level == 0:
        PinRed.value(0)
        PinYellow.value(0)
    elif level == 1:
        PinRed.value(1)
        PinYellow.value(0)
    elif level == 2:
        PinRed.value(0)
        PinYellow.value(1)
    elif level == 3:
        PinRed.value(1)
        PinYellow.value(1)
    if button_up.value() == 0:
        level += 1
        if level == 4:
            level = 1
    if button_down.value() == 0:
        level -= 1
        if level >= 0:
            level = 0
    time.sleep(0.2)