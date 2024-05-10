from machine import Pin
from utime import sleep

current_state: int  = 0

def button_isr(pin:Pin)-> None:
    global current_state
    current_state += 1
    if current_state > 2:
        current_state = 0    
    print(f'pin {pin} interrupst th program - ', current_state)
    
def main():
    global current_state
    button = Pin(0, Pin.IN, Pin.PULL_UP)
    led = Pin('LED', Pin.OUT)
    button.irq(trigger = Pin.IRQ_RISING, handler=button_isr)
    print('LED start flashing ..')
    while True:
        if current_state == 0:
            led.toggle()
            sleep(1)
        elif current_state == 1:
            led.off()
        else:
            led.on()

if __name__ == "__main__":
    main()
    