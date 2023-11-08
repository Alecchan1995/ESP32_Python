from machine import Pin,PWM
import time
sg_pin = PWM(Pin(26),freq=50,duty=0)
d_90=(int)(1023*0.0725)
d_zero=(int)(1023*0.025) #0.5ms
d_180=(int)(1023*0.12)  #2.4ms
de_map=[d_90,d_zero,d_90,d_180]
try:
    while 1:
        for i in de_map:
            sg_pin.duty(i)
            time.sleep(1)
except Exception as e:
    print(e)
    sg_pin.deinit()