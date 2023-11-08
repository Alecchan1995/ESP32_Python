from servo import Servo
from machine import Pin
import time

my_servo = Servo(Pin(26))
while True:
    my_servo.write_angle(0)
    time.sleep(1)
    my_servo.write_angle(90)
    time.sleep(1)
    my_servo.write_angle(180)
    time.sleep(1)
    my_servo.write_angle(90)
    time.sleep(1)
