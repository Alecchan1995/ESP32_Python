import tm1637,time
from machine import Pin
tm = tm1637.TM1637(clk=Pin(16),dio=Pin(17))
tm.number(99)
time.sleep(1)
tm.number(1010)
time.sleep(1)
tm.number(0101)
time.sleep(1)
tm.numbers(-1,01)