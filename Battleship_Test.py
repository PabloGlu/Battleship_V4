import import_ipynb

import Battleship_V4 as bs

import time


tab_at_p1 = bs.crea_tablero(10)
tab_at_m1 = bs.crea_tablero(10)


tab_def_p1 = bs.create_p1_def()

tab_def_m1 = bs.create_m1_def()

n = 1
while True:
    print(f'Turno {n}: Ataca el P1')
    disparo_p1 = bs.disparar_p1(tab_at_p1, tab_def_m1, bs.missile())
    time.sleep(1)

    if 'O' not in tab_def_m1:
        print('JUGADOR 1 HAS GANADO')
        break

    print(f'Turno {n}: Ataca la maquina M1')
    disparo_m1 = bs.disparar_m1(tab_at_m1, tab_def_p1, bs.missile())
    n += 1
    time.sleep(1)

    if 'O' not in tab_def_p1:
        print('JUGADOR 1 HAS PERDIDO')
        break

