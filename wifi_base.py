import socket
import network,utime
wifi= network.WLAN(network.STA_IF)
wifi.active(True)
while True:
    print("wificonnection")
    try:
        wifi.connect('wifi account','wifi password')
        if wifi.isconnected():
            print('Network Config=',wifi.ifconfig())
            data =wifi.ifconfig()
            break 
    except :
        print(error)
    utime.sleep(1)
print(data)