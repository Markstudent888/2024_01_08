from machine import ADC, Pin, Timer
adc = ADC(4)

def second1(t):
    print(adc.read_u16())
    
tim1 =Timer()
tim1.init(period=1000, callback =second1)