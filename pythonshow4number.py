import tm1637,time
from machine import Pin
tm = tm1637.TM1637(clk=Pin(16),dio=Pin(17))
#tm.numbers(99,99)
number = 9999
while number != 0:
    tm.number(number)
    number = number - 1
    time.sleep(1)    