import machine
import time
from machine import Pin

led25 = Pin("LED", Pin.OUT)
while True:
    led25.value(1)
    time.sleep(1)
    led25.value(0)
    time.sleep(1)
    
