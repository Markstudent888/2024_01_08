from machine import Pin
import time

start_ticks1 = time.ticks_ms()
start_ticks2 = time.ticks_ms()
start_ticks3 = time.ticks_ms()
led25 = Pin("LED",Pin.OUT)
ledStatus = False

while True:
    if time.ticks_diff(time.ticks_ms(), start_ticks1) >= 1000:
        print("過1秒了")
        start_ticks1 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
        
    if time.ticks_diff(time.ticks_ms(), start_ticks2) >= 5000:
        print("過5秒了")
        start_ticks2 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
        
    if time.ticks_diff(time.ticks_ms(), start_ticks3) >= 10000:
        print("過10秒了")
        start_ticks3 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)