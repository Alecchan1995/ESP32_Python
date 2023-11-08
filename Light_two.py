from machine import Pin
import time
Pin16 = Pin(16,Pin.OUT)
Pin5 = Pin(5,Pin.OUT)
while True:
    Pin16.value(1)
    Pin5.value(1)
    time.sleep(1)
    Pin16.value(0)
    Pin5.value(0)
    time.sleep(1)