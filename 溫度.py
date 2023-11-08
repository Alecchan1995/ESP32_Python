from machine import Pin,ADC,PWM
import time

adc_pin = Pin(32)
adc = ADC(adc_pin)
adc.width(ADC.WIDTH_12BIT) # 9bit ,10bit,11bit,12bit
adc.atten(ADC.ATTN_11DB) #3.6v
sg_pin = PWM(Pin(26),freq=50,duty=0)
d_zero=(int)(1023*0.025) #0.5ms
d_180=(int)(1023*0.12)  #2.4ms
while True:
    try:
        vol = (adc.read()/4095)*3.6
        tem = (vol-0.5)*100
        print("now",tem)
        if(tem > 24):
            sg_pin.duty(d_180)
        else:
            sg_pin.duty(d_zero)
        time.sleep(1)
    except Exception as e:
        print(e)
        sg_pin.deinit()
        break