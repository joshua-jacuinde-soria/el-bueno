from digital_clock import Digital_clock
from utime import sleep
from oled import oled_pruebas
from fsm import FSM
from random import randint

def clock_test():
    clock = Digital_clock(23, 59, 40)
    while True:
        h, m, s = clock.get_time()
        time = f'{h:02} : {m:02} : {s:02}'
        print(time)
        sleep(1)
        oled_pruebas(time)
        clock.incremento()
        
def prueba_fsm():
    fsm = FSM()
    eventos = {
        'incondicional':    0,
        'por_defecto':      1,
        'presionar_boton':  2,
        'boton':            3,
        'no_boton':         4,
        'no_tempo':         5
        #evento del tiempo fuera es manejado por el mecanismo de interrupcion del micro
    }
    fsm.mandar_regla_transicion(0, eventos['incondicional'], 1)
    fsm.mandar_regla_transicion(1,eventos['por_defecto'], 1)
    fsm.mandar_regla_transicion(1, eventos['presionar_boton'], 2)
    fsm.mandar_regla_transicion(2, eventos['boton'], 4)
    fsm.mandar_regla_transicion(2, eventos['no_boton'], 1)
    fsm.mandar_regla_transicion(4, eventos['no_tempo'], 5)
    fsm.mandar_regla_transicion(5, eventos['no_tempo'], 1)
    while True:
        estado = fsm.obtener_estado_concurrido()
        if estado == 0:
            print(f'estado concurrido {estado}')
            sleep(1)
            fsm.computar_siguiente_estado(eventos['incondicional'])
        elif estado == 1:
            print(f'estado concurrido {estado}')
            sleep(1)
            rnd = randint(eventos['por_defecto'],eventos['presionar_boton'])
            fsm.computar_siguiente_estado(rnd)
        elif estado == 2:
            print(f'estado concurrido {estado}')
            sleep(1)
            rnd = randint(eventos['boton'],eventos['no_boton'])
            fsm.computar_siguiente_estado(rnd)
        elif estado == 4:
            print(f'estado concurrido {estado}')
            sleep(1)
            fsm.computar_siguiente_estado(eventos['no_tempo'])
        elif estado == 5:
            print(f'estado concurrido {estado}')
            sleep(1)
            fsm.computar_siguiente_estado(eventos['no_tempo'])
        else:
            print('Estas bien??')
            break
            