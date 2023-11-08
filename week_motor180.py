from servo import Servo
from machine import Pin,Timer
import time

my_servo = Servo(Pin(26))
def changemotor(x):
    my_servo.write_angle(0)
    time.sleep(1)
    my_servo.write_angle(90)
    time.sleep(1)
    my_servo.write_angle(180)
    time.sleep(1)
    my_servo.write_angle(90)
    time.sleep(1)

    
timl=Timer(1)
timl.init(period=1000,mode=Timer.PERIODIC,callback=changemotor)
try:
    while 1:
        pass
except:
    tim1.deinit()
    print('stopping')
