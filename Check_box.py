import esp32,time
from machine import Pin,PWM
buzzer = PWM(Pin(14,Pin.OUT),freq=0,duty=512)
while True:
    data = esp32.hall_sensor()
    print(data)
    time.sleep(0.1)
    if(data>0):
        buzzer.freq(380)
        pass
    else:
        buzzer.freq(0)