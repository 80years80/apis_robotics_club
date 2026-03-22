import time
from machine import Pin

# Your Actual Project Logic
led = Pin(2, Pin.OUT)

print("Main Application Started!")
count = 0
while True:
    #led.value(not led.value())
    time.sleep(1)
    
