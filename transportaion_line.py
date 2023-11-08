# red:26 yellow:12 green:16
from machine import Pin
import time
Pin16 = Pin(16,Pin.OUT)
Pin26 = Pin(26,Pin.OUT)
Pin12 = Pin(12,Pin.OUT)
while True:
    Pin26.value(1)
    Pin16.value(0)
    Pin12.value(0)
    time.sleep(1)
    Pin26.value(0)
    Pin16.value(0)
    Pin12.value(1)
    time.sleep(1)
    Pin26.value(0)
    Pin16.value(1)
    Pin12.value(0)
    time.sleep(1)