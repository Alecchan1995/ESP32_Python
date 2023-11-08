from machine import Timer,Pin
import time
timl = Timer(1) #0~3
# red:26 yellow:12 green:16
Pin16 = Pin(16,Pin.OUT)
Pin26 = Pin(26,Pin.OUT)
Pin12 = Pin(12,Pin.OUT)
# mode=Timer.ONE_SHOT

time_line = 3
def changeLine(x):    
    global time_line
    if time_line % 3==0:
        Pin26.value(1)
    else:
        Pin26.value(0)
    if time_line % 3==1:
        Pin12.value(1)
    else:
        Pin12.value(0)
    if time_line % 3==2:
        Pin16.value(1)
    else:
        Pin16.value(0)
    time_line += 1
    time.sleep(1)
    
timl=Timer(1)
timl.init(period=1000,mode=Timer.PERIODIC,callback=changeLine)
try:
    while 1:
        pass
except:
    tim1.deinit()
    print('stopping')
