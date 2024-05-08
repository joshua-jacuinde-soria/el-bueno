from digital_clock import Digital_clock
from utime import sleep

def clock_test():
    clock = Digital_clock(23, 59, 40)
    while True:
        h, m, s = clock.get_time()
        time = f'{h:02} : {m:02} : {s:02}'
        print(time)
        sleep(1)
        clock.incremento()