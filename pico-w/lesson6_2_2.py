from machine import Pin, Timer

led25 = Pin("LED",Pin.OUT)

def second5(t):
    print("5th second")
    led25.toggle()
    
def second1(t):
    print("1st second")
    
tim = Timer(period=5000, mode=Timer.PERIODIC, callback=second5)
tim1 = Timer(period=1000, mode=Timer.ONE_SHOT, callback=second1)