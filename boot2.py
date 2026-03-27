#in use
#https://forum.arduino.cc/t/webrepl-set-up-for-micropython/1280670
import network
import time
import webrepl

def wifi_connect():
    SSID = "APIS-PLS"
    PASSWORD = "apispls@2025"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep_ms(100)
    #import webrepl_setup
    
wifi_connect()

webrepl.start()