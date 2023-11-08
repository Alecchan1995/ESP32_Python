import tm1637
from machine import Pin,PWM
import time

buzzer = PWM(Pin(23,Pin.OUT),freq=0,duty=512)
buzzer.freq(380)
time.sleep(1)
buzzer.freq(294)
time.sleep(1)
buzzer.deinit()