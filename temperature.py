from machine import Pin,ADC
import time
adc_pin = Pin(32)
adc = ADC(adc_pin)
adc.width(ADC.WIDTH_12BIT) # 9bit ,10bit,11bit,12bit
adc.atten(ADC.ATTN_11DB) #3.6v
#26 red 14 green
Pin26 = Pin(26,Pin.OUT)
Pin14 = Pin(14,Pin.OUT)
while True:
    try:
        vol = (adc.read()/4095)*3.6
        tem = (vol-0.5)*100
        print("now",tem)
        if(tem > 22):
            Pin26.value(1)
            Pin14.value(0)
        else:
            Pin26.value(0)
            Pin14.value(1)
        time.sleep(1)
    except Exception as e:
        print(e)
        break