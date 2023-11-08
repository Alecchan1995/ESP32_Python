from machine import Pin
import machine,ssd1306
import time
echoTimeout=23200
trigpin=Pin(17,mode=Pin.OUT)
echopin=Pin(16,mode=Pin.IN)

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def distance():
    trigpin.value(1)
    time.sleep_us(10)
    trigpin.value(0)
    pulseTime=machine.time_pulse_us(echopin,1,echoTimeout)
    if pulseTime >0:
        return pulseTime/58
    else:
        return pulseTime
    
while True:
    cm = distance()
    if cm >0:
        print("Distance :",cm)
        if cm <10:
            oled.fill(0) 
            oled.text("warnning", 30, 30)
            oled.show();
        else:
            oled.fill(0) 
            oled.text("Distance :"+str(cm), 30, 30)
            oled.show();
    else:
        print("error")
        oled.fill(0) 
        oled.text("Distance :"+str(cm), 30, 30)
        oled.show();
    time.sleep(1)
