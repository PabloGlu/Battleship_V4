import import_ipynb

import Battleship_V6_class as bs

import time

p1 = bs.Player()
m1 = bs.Machine()

# tab_at_p1 = bs.Player.crea_tablero(p1)
# tab_at_m1 = bs.Machine.crea_tablero(m1)



tab_def_p1 = bs.Player.create_p1_def(p1)
tab_def_m1 = bs.Machine.create_m1_def(m1)


n = 1
    
while True:
    print(f'Turno {n}: Ataca el P1')
    disparo_p1 = p1.disparar_p1_manual_v2(p1.tab_at_p1, m1.tab_def_m1, m1)
    time.sleep(1)

    if 'O' not in m1.tab_def_m1:
        print('JUGADOR 1 HAS GANADO')
        break

    print(f'Turno {n}: Ataca la maquina M1')
    disparo_m1 = m1.disparar_m1_v2_hard(m1.tab_at_m1, p1.tab_def_p1, m1.missile(), p1)
    n += 1
    time.sleep(1)

    if 'O' not in p1.tab_def_p1:
        print('JUGADOR 1 HAS PERDIDO')
        break

